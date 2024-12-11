import re
import csv
import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """Fetch HTML content from the given URL."""
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )
    }
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
        return response.text

    # else: Failed to retrieve data
    print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
    return None

def parse_repositories(html):
    """Parse HTML content and extract repository information."""
    soup = BeautifulSoup(html, 'html.parser')
    repos = soup.find_all('li', class_='mb-3')
    repository_data = []

    for repo in repos:
        # Repository Name
        repo_span = repo.find('span', class_='repo')
        repo_name = repo_span.get_text(strip=True) if repo_span else 'Unknown'

        # Visibility
        visibility_tag = repo.find('span', class_=re.compile(r'^Label Label--secondary'))
        visibility = visibility_tag.get_text(strip=True) if visibility_tag else 'Unknown'

        # Description
        description_tag = repo.find('p', class_='pinned-item-desc')
        description = description_tag.get_text(strip=True) if description_tag else 'No description'

        # Programming Language
        language_tag = repo.find('span', itemprop='programmingLanguage')
        language = language_tag.get_text(strip=True) if language_tag else 'Not specified'

        # Stars
        stars_tag = repo.find('a', href=re.compile(r'.*/stargazers$'))
        stars = int(stars_tag.get_text(strip=True)) if stars_tag else 0

        # Forks
        forks_tag = repo.find('a', href=re.compile(r'.*/forks$'))
        forks = int(forks_tag.get_text(strip=True)) if forks_tag else 0

        # Append all extracted data to repository_data list
        repository_data.append({
            "Repository Name": repo_name,
            "Visibility": visibility,
            "Description": description,
            "Programming Language": language,
            "Stars": stars,
            "Forks": forks
        })

    return repository_data

def save_to_csv(data, filename="repositories.csv"):
    """Save the parsed repository data to a CSV file."""
    if data:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename}.")
    else:
        print("No data to save.")
