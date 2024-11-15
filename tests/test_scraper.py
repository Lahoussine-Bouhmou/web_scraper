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


def test_parse_repositories():
    """Test that parse_repositories correctly extracts data from HTML."""
    html = """
    <html>
        <body>
            <li class="mb-3">
                <span class="repo">seas</span>
                <span class="Label Label--secondary">Public</span>
                <p class="pinned-item-desc">Project about seas</p>
                <span itemprop="programmingLanguage">Java</span>
                <a href="/thesmartenergy/seas/stargazers" class="pinned-item-meta Link--muted"> 12 </a>
                <a href="/thesmartenergy/seas/forks" class="pinned-item-meta Link--muted"> 13 </a>
            </li>
        </body>
    </html>
    """
    repo_data = parse_repositories(html)
    assert len(repo_data) == 1  # We expect one repository to be parsed
    assert repo_data[0]['Repository Name'] == 'seas'
    assert repo_data[0]['Visibility'] == 'Public'
    assert repo_data[0]['Description'] == 'Project about seas'
    assert repo_data[0]['Programming Language'] == 'Java'
    assert repo_data[0]['Stars'] == 12
    assert repo_data[0]['Forks'] == 13

