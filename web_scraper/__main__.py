from .scraper import fetch_html, parse_repositories, save_to_csv

def main():
    username = "Lahoussine-Bouhmou"  # Replace with the GitHub username you want to scrape
    url = f"https://github.com/{username}"
    
    # Fetch HTML content from the GitHub user's repositories page
    html = fetch_html(url)
    
    if html:
        # Parse the repositories from the HTML content
        repos = parse_repositories(html)
        
        if repos:
            # Save the repository names to a CSV file
            save_to_csv(repos)
        else:
            print(f"No repositories found for {username}")
    else:
        print("Failed to fetch the HTML content.")

if __name__ == "__main__":
    main()

