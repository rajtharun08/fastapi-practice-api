def test_login_success(client, db_session):
    from app.services.auth_service import get_password_hash
    from app.models.user import User
    
    hashed_pw = get_password_hash("password123")
    user = User(name="Tharun", email="test@eams.com", password=hashed_pw, role="Employee", department_id=1)
    db_session.add(user)
    db_session.commit()

    response = client.post("/auth/login", data={"username": "test@eams.com", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_protected_route_unauthorized(client):
    """Verify that accessing an admin route without a token fails with 401."""
    response = client.get("/itadmin/assets")
    assert response.status_code == 401