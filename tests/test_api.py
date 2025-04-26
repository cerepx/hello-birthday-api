"""
API integration tests for the Hello Birthday API service.
Tests endpoints: /health, /hello/<username>.
"""

import os
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")

def test_health_check():
    """
    Ensure the /health endpoint returns 200 OK.
    """
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    assert response.status_code == 200
    assert response.text == "OK"

def test_invalid_username():
    """
    Ensure non-alphabetic usernames are rejected.
    """
    response = requests.put(
        f"{BASE_URL}/hello/Constatin123",
        json={"dateOfBirth": "1990-01-01"},
        timeout=5
    )
    assert response.status_code == 400

def test_future_date_of_birth():
    """
    Ensure that dateOfBirth in the future is rejected.
    """
    response = requests.put(
        f"{BASE_URL}/hello/Constatin",
        json={"dateOfBirth": "2999-01-01"},
        timeout=5
    )
    assert response.status_code == 400

def test_valid_put_and_get():
    """
    Save a valid user and then retrieve the birthday message.
    """
    username = "Constantin"
    dob = "1985-04-16"
    put_response = requests.put(
        f"{BASE_URL}/hello/{username}",
        json={"dateOfBirth": dob},
        timeout=5
    )
    assert put_response.status_code == 204

    get_response = requests.get(f"{BASE_URL}/hello/{username}", timeout=5)
    assert get_response.status_code == 200
    assert "message" in get_response.json()
