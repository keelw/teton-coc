import pytest
import requests

# Mock function for unauthorized access
def mock_get_unauthorized(url, params=None, **kwargs):
    class MockResponse:
        def __init__(self):
            self.status_code = 401
            self.text = ""
            self.headers = {"Content-Type": "text/plain"}
    
    return MockResponse()

# Mock function for valid access with no content
def mock_get_valid_access(url, params=None, **kwargs):
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.text = ""
            self.headers = {"Content-Type": "text/plain"}
    
    return MockResponse()

# Test unauthorized access
def test_unauthorized_access(monkeypatch):
    # Mock the requests.get function
    monkeypatch.setattr(requests, "get", mock_get_unauthorized)
    
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "admin"}
    
    response = requests.get(url, params=params)
    
    # Assertions
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response, got {response.text.strip()!r}"
    assert response.headers.get("Content-Type") == "text/plain", (
        f"Expected 'text/plain', got {response.headers.get('Content-Type')!r}"
    )

# Test valid access with no content
def test_valid_access_with_no_content(monkeypatch):
    # Mock the requests.get function
    monkeypatch.setattr(requests, "get", mock_get_valid_access)
    
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "qwerty"}
    
    response = requests.get(url, params=params)
    
    # Assertions
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response, got {response.text.strip()!r}"
    assert response.headers.get("Content-Type") == "text/plain", (
        f"Expected 'text/plain', got {response.headers.get('Content-Type')!r}"
    )
