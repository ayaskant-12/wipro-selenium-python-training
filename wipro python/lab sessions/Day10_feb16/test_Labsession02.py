import pytest
import requests

BASE_URL = "https://reqres.in/api/users"

headers = {
    "x-api-key": "reqres_32dc7acface54bae88055671dfb6565e"
}

customer_id = None


# ============================================================
# POST – Create Customer
# ============================================================

def test_create_customer():

    global customer_id

    payload = {
        "name": "Ayaskant Dash",
        "email": "ayaskant@test.com",
        "balance": 5000
    }

    response = requests.post(BASE_URL, json=payload, headers=headers)

    print(response.text)

    assert response.status_code == 201

    data = response.json()

    assert "id" in data

    customer_id = data["id"]

    print("Customer created:", customer_id)


# ============================================================
# GET – Retrieve Customer
# ============================================================

def test_get_customer():

    response = requests.get(f"{BASE_URL}/{customer_id}", headers=headers)

    print(response.text)

    assert response.status_code == 200


# ============================================================
# PUT – Update Customer
# ============================================================

def test_update_customer():

    payload = {
        "name": "Ayaskant Dash",
        "email": "newemail@test.com"
    }

    response = requests.put(
        f"{BASE_URL}/{customer_id}",
        json=payload,
        headers=headers
    )

    print(response.text)

    assert response.status_code == 200


# ============================================================
# DELETE
# ============================================================

def test_delete_customer():

    response = requests.delete(
        f"{BASE_URL}/{customer_id}",
        headers=headers
    )

    assert response.status_code == 204


# ============================================================
# GET after delete
# ============================================================

def test_get_deleted_customer():

    response = requests.get(
        f"{BASE_URL}/{customer_id}",
        headers=headers
    )

    print(response.text)

    # reqres may still return 200
    assert response.status_code in [200, 404]