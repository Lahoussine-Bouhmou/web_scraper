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
    """Test that parse_repositories correctly handles a large HTML with multiple repositories."""
    html = """
    <html>
        <body>
            <li class="mb-3">
                <span class="repo">Repo1</span>
                <span class="Label Label--secondary">Public</span>
                <p class="pinned-item-desc">Description of Repo1</p>
                <span itemprop="programmingLanguage">Python</span>
                <a href="/user/repo1/stargazers" class="pinned-item-meta Link--muted"> 10 </a>
                <a href="/user/repo1/forks" class="pinned-item-meta Link--muted"> 5 </a>
            </li>
            <li class="mb-3">
                <span class="repo">Repo2</span>
                <span class="Label Label--secondary">Private</span>
                <p class="pinned-item-desc">Description of Repo2</p>
                <span itemprop="programmingLanguage">JavaScript</span>
                <a href="/user/repo2/stargazers" class="pinned-item-meta Link--muted"> 20 </a>
                <a href="/user/repo2/forks" class="pinned-item-meta Link--muted"> 10 </a>
            </li>
            <li class="mb-3">
                <span class="repo">Repo3</span>
                <span class="Label Label--secondary">Public</span>
                <p class="pinned-item-desc">Description of Repo3</p>
                <span itemprop="programmingLanguage">Ruby</span>
                <a href="/user/repo3/stargazers" class="pinned-item-meta Link--muted"> 15 </a>
                <a href="/user/repo3/forks" class="pinned-item-meta Link--muted"> 7 </a>
            </li>
        </body>
    </html>
    """

    # Parse the repositories from the HTML
    repo_data = parse_repositories(html)

    # Assertions
    assert len(repo_data) == 3  # We expect three repositories to be parsed

    # Test for the first repository
    assert repo_data[0]['Repository Name'] == 'Repo1'
    assert repo_data[0]['Visibility'] == 'Public'
    assert repo_data[0]['Description'] == 'Description of Repo1'
    assert repo_data[0]['Programming Language'] == 'Python'
    assert repo_data[0]['Stars'] == 10
    assert repo_data[0]['Forks'] == 5

    # Test for the second repository
    assert repo_data[1]['Repository Name'] == 'Repo2'
    assert repo_data[1]['Visibility'] == 'Private'
    assert repo_data[1]['Description'] == 'Description of Repo2'
    assert repo_data[1]['Programming Language'] == 'JavaScript'
    assert repo_data[1]['Stars'] == 20
    assert repo_data[1]['Forks'] == 10

    # Test for the third repository
    assert repo_data[2]['Repository Name'] == 'Repo3'
    assert repo_data[2]['Visibility'] == 'Public'
    assert repo_data[2]['Description'] == 'Description of Repo3'
    assert repo_data[2]['Programming Language'] == 'Ruby'
    assert repo_data[2]['Stars'] == 15
    assert repo_data[2]['Forks'] == 7

