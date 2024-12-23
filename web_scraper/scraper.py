import re
import csv
import requests
import logging
from bs4 import BeautifulSoup

# Set up logging configuration
logging.basicConfig(
    filename='scraper_logging.log',  # Log to this file
    filemode='w',
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO  # For development you can set it to DEBUG
)
logger = logging.getLogger(__name__)

def fetch_html(url: str) -> str:
    """
    Fetch HTML content from the given URL.

    Args:
        url (str): The URL of the webpage to fetch the HTML content from.

    Returns:
        str: The HTML content of the webpage, or None if the request fails.

    Logs:
        Logs relevant messages at each stage of fetching the HTML, including success and failure.
    """
    logger.debug("Attempting to fetch HTML content from URL: %s", url)

    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        logger.info("Successfully fetched HTML content from %s. Status code: %d", url, response.status_code)
        return response.text

    except requests.exceptions.HTTPError as http_err:
        logger.error("HTTP error occurred while fetching %s: %s", url, http_err)
    except requests.exceptions.RequestException as req_err:
        logger.error("Error occurred while fetching %s: %s", url, req_err)

    logger.warning("Failed to retrieve data from %s. Returning None.", url)
    return None

def parse_repositories(html: str) -> list:
    """
    Parse HTML content and extract repository information.

    Args:
        html (str): The HTML content to parse for repository data.

    Returns:
        list: A list of dictionaries containing parsed repository data.
        
    Logs:
        Logs the process of parsing the HTML and any issues encountered (e.g., missing data).
    """
    logger.debug("Parsing HTML content to extract repository data.")

    soup = BeautifulSoup(html, 'html.parser')
    repos = soup.find_all('li', class_='mb-3')
    repository_data = []

    if not repos:
        logger.warning("No repositories found in the HTML content.")

    for repo in repos:
        logger.debug("Parsing repository details.")

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

    logger.info("Parsed %d repositories from HTML.", len(repository_data))
    return repository_data

def save_to_csv(data: list, filename: str = "repositories.csv"):
    """
    Save the parsed repository data to a CSV file.

    Args:
        data (list): A list of dictionaries containing repository data to be saved.
        filename (str): The name of the file to save the data to (default: 'repositories.csv').

    Logs:
        Logs information about the success or failure of saving the data to a CSV file.
    """
    if data:
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            logger.info("Data saved to %s.", filename)
            print(f"Data saved to {filename}.")
        except requests.exceptions.RequestException as e:
            logger.critical("Critical error while saving data to CSV: %s", str(e))

    else:
        logger.warning("No data to save.")
