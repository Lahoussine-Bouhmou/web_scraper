# tests/test_scraper.py

import pytest
from web_scraper.scraper import fetch_html, parse_repositories, save_to_csv

# Mocking the 'requests.get' method to simulate fetching HTML
def test_fetch_html_success(monkeypatch):
    """Test that fetch_html correctly fetches HTML content."""
    
    class MockResponse:
        def __init__(self, status_code, text):
            self.status_code = status_code
            self.text = text
    
    # Mocking the get function
    def mock_get(url, headers=None):  # Add headers argument to the mock_get function
        return MockResponse(200, "<html><body>Mocked HTML</body></html>")
    
    # Monkeypatch requests.get to use the mock_get
    monkeypatch.setattr('requests.get', mock_get)
    
    url = "https://github.com/someuser/somerepo"
    result = fetch_html(url)
    
    # Assertions to verify the function behavior
    assert result is not None  # HTML content should be returned
    assert "<html><body>Mocked HTML</body></html>" in result


def test_fetch_html_failure(monkeypatch):
    """Test that fetch_html handles failed requests."""
    class MockResponse:
        def __init__(self, status_code, text):
            self.status_code = status_code
            self.text = text

    # Mocking the requests.get method
    def mock_get(url, headers):
        return MockResponse(404, "Not Found")

    monkeypatch.setattr('requests.get', mock_get)

    url = "https://github.com/someuser/somerepo"
    result = fetch_html(url)
    assert result is None  # In case of failure, it should return None

