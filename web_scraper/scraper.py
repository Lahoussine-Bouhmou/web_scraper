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
    Parses the HTML content to extract repository names, visibility, and programming languages
    from the GitHub user profile page.
    """
    soup = BeautifulSoup(html, 'html.parser')
    repos = soup.find_all('li', class_='pinned-item-list-item')  # Find all pinned repo blocks

    repo_data = []
    
    for repo in repos:
        # Extract repository name
        name_tag = repo.find('span', class_='repo')
        name = name_tag.text.strip() if name_tag else 'Unknown'

        # Extract visibility (Public or Private)
        visibility_tag = repo.find('span', class_='Label--secondary')
        visibility = visibility_tag.text.strip() if visibility_tag else 'Unknown'
        
        # Extract programming language
        language_tag = repo.find('span', itemprop='programmingLanguage')
        language = language_tag.text.strip() if language_tag else 'Not specified'

        # Append repository details to the list
        repo_data.append((name, visibility, language))
    
    return repo_data

def save_to_csv(data, filename="repositories.csv"):
    """
    Saves the list of repository names, visibility, and programming languages to a CSV file.
    """
    if data:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            file.write("Repository Name,Visibility,Programming Language\n")  # Write header
            for repo in data:
                file.write(f"{repo[0]},{repo[1]},{repo[2]}\n")  # Write name, visibility, and language
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

