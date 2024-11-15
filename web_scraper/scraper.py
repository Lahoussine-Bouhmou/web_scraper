import requests
from bs4 import BeautifulSoup
import csv

def fetch_html(url):
    """
    Fetches the HTML content from the provided URL.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return None
    return response.content

def parse_repositories(html):
    """
    Parses the HTML content to extract repository names, visibility, description, programming languages,
    and the number of stars from the GitHub user profile page.
    """
    soup = BeautifulSoup(html, 'html.parser')
    repos = soup.find_all('li', class_='mb-3')  # Find all pinned repo blocks

    repo_data = []

    for repo in repos:
        # Extract repository name
        name_tag = repo.find('span', class_='repo')
        name = name_tag.text.strip() if name_tag else 'Unknown'

        # Extract visibility (Public or Private)
        visibility_tag = repo.find('span', class_='Label--secondary')
        visibility = visibility_tag.text.strip() if visibility_tag else 'Unknown'

        # Extracting description
        description_tag = repo.find('p', class_='pinned-item-desc')
        description = description_tag.get_text(strip=True) if description_tag else 'No description'

        # Extract programming language
        language_tag = repo.find('span', itemprop='programmingLanguage')
        language = language_tag.get_text(strip=True) if language_tag else 'Not specified'

        # Extracting number of stars
        stars_tag = repo.find('a', class_='pinned-item-meta Link--muted', attrs={'aria-label': 'stars'})
        stars = stars_tag.get_text(strip=True) if stars_tag else '0'  # Default to 0 if no stars tag found

        # Extracting number of forks
        forks_tag = repo.find('a', class_='pinned-item-meta Link--muted', attrs={'aria-label': 'forks'})
        forks = forks_tag.get_text(strip=True) if forks_tag else '0'  # Default to 0 if no forks tag found

        # Append repository details to the list
        repo_data.append((name, visibility, description, language, stars, forks))

    return repo_data

def save_to_csv(data, filename="repositories.csv"):
    """
    Saves the list of repository names, visibility, description, programming languages,
    and number of stars and forks to a CSV file.
    """
    if data:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            file.write("Repository Name,Visibility,Description,Programming Language,Stars,Forks\n")  # Write header
            for repo in data:
                file.write(f"{repo[0]},{repo[1]},{repo[2]},{repo[3]},{repo[4]},{repo[5]}\n")  # Write name, visibility, description, language, stars, forks
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")
