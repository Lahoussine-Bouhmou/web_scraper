from .scraper import fetch_html, parse_repositories, save_to_csv

def main():
    # Ask the user to input the GitHub username
    username = input("Enter the GitHub username to scrape repositories: ")
    
    # Construct the GitHub URL for the user's repositories
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

