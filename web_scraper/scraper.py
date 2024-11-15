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
    Parses the HTML content to extract repository names from the GitHub user profile page.
    Now looking for <span class="repo">...</span> to get repository names.
    """
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all the <span> elements with class 'repo' that contain repository names
    repos = soup.find_all('span', class_='repo')

    repo_names = []
    for repo in repos:
        repo_names.append(repo.text.strip())  # Append the repo name to the list
    
    return repo_names

def save_to_csv(data, filename="repositories.csv"):
    """
    Saves the list of repository names to a CSV file.
    """
    if data:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            file.write("Repository Name\n")  # Write header
            for repo in data:
                file.write(f"{repo}\n")  # Write each repository name on a new line
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

