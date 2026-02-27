def test_create_asset_authorized(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    asset_data = {
        "asset_tag": "LP-FIX-001",
        "asset_type": "Laptop",
        "brand": "Dell",
        "model": "XPS",
        "purchase_date": "2026-02-27", 
        "department_id": 1
    }
    response = client.post("/itadmin/assets", json=asset_data, headers=headers)
    assert response.status_code == 200