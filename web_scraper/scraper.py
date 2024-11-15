import requests
from bs4 import BeautifulSoup
import csv

def fetch_html(url):
    """
    Fetches the HTML content from the provided URL.
    """
    response = requests.get(url)
    # Check if the request was successful (status code 200)
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
    
    # Find all the <span> elements with class 'repo' that contain repository names
    repos = soup.find_all('span', class_='repo')

    repo_data = []
    
    for repo in repos:
        # Extract repository name
        name = repo.text.strip()
        
        # Default visibility is 'Public'
        visibility = 'Public'
        
        # Find the visibility (Public or Private) - look for the label for 'Private'
        visibility_tag = repo.find_parent('a').find_next('span', class_='Label--secondary')
        if visibility_tag and 'private' in visibility_tag.text.lower():
            visibility = 'Private'
        
        # Find the programming language using the new HTML element with itemprop="programmingLanguage"
        language_tag = repo.find_parent('a').find_next('span', itemprop='programmingLanguage')
        
        if language_tag:
            language = language_tag.text.strip()
        
        # Append the repository name, visibility, and language to the list
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

