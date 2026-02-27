import pytest

def test_health_check(client):
    """Verify the server is up and responding."""
    response = client.get("/")
    assert response.status_code == 200

def test_docs_accessible(client):
    """Verify Swagger UI is generated."""
    response = client.get("/docs")
    assert response.status_code == 200

def test_unauthorized_access(client):
    """Verify that protected routes reject requests without tokens."""
    response = client.get("/itadmin/assets")
    assert response.status_code == 401 # Unauthorized

def test_employee_rbac_restriction(client, employee_token):
    """Verify that an Employee cannot access IT Admin routes."""
    headers = {"Authorization": f"Bearer {employee_token}"}
    response = client.get("/itadmin/assets", headers=headers)
    assert response.status_code == 403 # Forbidden (RBAC working)

def test_login_validation(client):
    response = client.post("/auth/login", data={"username": "", "password": ""})
    assert response.status_code == 422