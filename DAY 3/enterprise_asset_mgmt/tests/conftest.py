import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database.session import get_db
from app.database.base import Base
from app.services.auth_service import create_access_token, get_password_hash
from app.models.user import User

# Use a clean SQLite file
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_assets.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture
def client(db_session):
    app.dependency_overrides[get_db] = lambda: db_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

@pytest.fixture
def admin_token(db_session):
    # Ensure User is in DB so get_current_user doesn't return 401
    user = User(name="Admin", email="admin@test.com", password=get_password_hash("test"), role="IT Admin", department_id=1)
    db_session.add(user)
    db_session.commit()
    return create_access_token(data={"sub": user.email, "role": user.role})