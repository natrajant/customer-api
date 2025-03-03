from fastapi.testclient import TestClient
from src.main import app
import json

client = TestClient(app)

customer_count = 0
customer_id = ''

def test_index_0():
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Customers API'}

def test_get_customers_1():
    response = client.get("/api/v1/customers")
    global customer_count 
    customer_count = len(response.json())
    assert response.status_code == 200

def test_create_customer_2():
    data = {"first_name": "Jane", "last_name": "Doe", "phone": "8675309", "email": "jane.doe@gmail.com"}
    response = client.post(
        "/api/v1/customers",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )
    assert 200 == response.status_code
    assert response.json().get("message") == "Customer created"

    global customer_id 
    customer_id = response.json().get("id")

    response = client.get(f"/api/v1/customers/{customer_id}")
    assert response.json().get("email") == data["email"]

def test_patch_customer_3():
    data = {"last_name": "Austen"}
    response = client.patch(
        f"/api/v1/customers/{customer_id}",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )
    assert 200 == response.status_code
    assert response.json().get("message") == "Customer updated"

    response = client.get(f"/api/v1/customers/{customer_id}")
    assert response.json().get("last_name") == data["last_name"]

def test_delete_customer_4():
    data = {"last_name": "Austen"}
    response = client.delete(
        f"/api/v1/customers/{customer_id}",
        headers={"Content-Type": "application/json"},
    )
    assert 200 == response.status_code
    assert response.json().get("message") == "Customer deleted"
