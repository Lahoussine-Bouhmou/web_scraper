# web_scraper/__main__.py

from web_scraper.scraper import fetch_html, parse_repositories, save_to_csv

def scrape(url):
    """Main scraping function to fetch HTML, parse it, and save to CSV."""
    html = fetch_html(url)
    if html:
        repository_data = parse_repositories(html)
        save_to_csv(repository_data)

def main():
    """CLI entry point to scrape repositories from a given URL."""
    # Prompt the user for the GitHub username
    username = input("Enter the GitHub username to scrape: ").strip()
    
    if username:  # Proceed only if a username is entered
        url = f"https://github.com/{username}"
        scrape(url)
    else:
        print("No username entered. Exiting.")

if __name__ == "__main__":
    main()

