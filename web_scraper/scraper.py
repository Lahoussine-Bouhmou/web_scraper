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
    Parses the HTML content to extract repository names and visibility 
    (Public or Private) from the GitHub user profile page.
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
        
        # Append both the repo name and visibility to the list
        repo_data.append((name, visibility))
    
    return repo_data

def save_to_csv(data, filename="repositories.csv"):
    """
    Saves the list of repository names and visibility to a CSV file.
    """
    if data:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            file.write("Repository Name,Visibility\n")  # Write header
            for repo in data:
                file.write(f"{repo[0]},{repo[1]}\n")  # Write name and visibility on a new line
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

