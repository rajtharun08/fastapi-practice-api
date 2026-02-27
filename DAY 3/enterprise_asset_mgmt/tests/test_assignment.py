def test_full_workflow(client, employee_token, admin_token, db_session):
    # 1. Employee creates a request
    headers = {"Authorization": f"Bearer {employee_token}"}
    req_res = client.post("/employee/request-asset", json={"asset_type": "Laptop", "reason": "Work"}, headers=headers)
    assert req_res.status_code == 200
    req_id = req_res.json()["id"]

    # 2. Admin creates an available asset
    from app.models.asset import Asset, AssetStatus
    asset = Asset(asset_tag="WORK-01", asset_type="Laptop", brand="Dell", model="XPS", purchase_date="2026-01-01", status=AssetStatus.AVAILABLE, department_id=1)
    db_session.add(asset)
    db_session.commit()

    # 3. Admin approves request
    admin_headers = {"Authorization": f"Bearer {admin_token}"}
    approve_res = client.post(f"/itadmin/requests/{req_id}/approve?asset_id={asset.id}", headers=admin_headers)
    assert approve_res.status_code == 200