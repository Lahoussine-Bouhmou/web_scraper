# Web Scraper Project

This project is a Python-based web scraper that extracts popular repositories' information from a GitHub user profile. The scraper fetches repository details, including:

- Name  
- Visibility (public/private)  
- Description  
- Programming language  
- Stars  
- Forks  

The extracted data is saved into a CSV file for easy access and analysis.

---

## Project Setup

This project uses **Poetry** as the build tool for dependency management, project versioning, and packaging. Poetry automates tasks such as managing dependencies, setting up the virtual environment, and packaging the project.

---

## Prerequisites

Ensure the following are installed before using the project:

- [Python 3.10+](https://www.python.org/downloads/)  
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency management and packaging)  
- [Make](https://www.gnu.org/software/make/) (for automating tasks via Makefile)  

---

## Installation

Follow these steps to set up the project locally:

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/web_scraper.git
cd web_scraper
```

### Step 2: Install Dependencies

Install dependencies listed in `pyproject.toml`:

```bash
make install
```

This uses Poetry to create and activate a virtual environment with the required dependencies. Alternatively, you can use `poetry install` directly if you prefer.

---

## Usage

### Step 1: Run the Scraper

To run the scraper and extract data from a GitHub user profile, execute the following command:

```bash
make run
```

You will be prompted to enter the GitHub username (e.g., `octocat`):

```
Enter the GitHub username to scrape: octocat
```

After entering the username, the scraper will fetch the repository details from the specified GitHub profile.

### Step 2: View Extracted Data

The extracted data is saved as a CSV file in the project directory. The filename will include the username, for example: `octocat_repositories.csv`.

---

## Example CSV Format

Here’s an example of the output CSV format:

```csv
Repository Name,Visibility,Description,Programming Language,Stars,Forks
TB-project,Public,first github repository,Not specified,0,0
JavaSpringFirstProject,Public,,Java,0,0
Lahoussine-Bouhmou,Public,,Not specified,0,0
lahoussine-bouhmou.github.io,Public,,HTML,0,0
Github-Scraper,Public,,Not specified,0,0
web_scraper,Public,,Python,0,0
```

---

## Testing

Run tests to ensure the scraper functions as expected:

```bash
make test
```

This command runs all tests defined in `tests/test_scraper.py` using `pytest`.

---

## Build and Publish (Optional)

### Step 1: Build the Package

To create a distribution package, run:

```bash
make build
```

This generates a `.tar.gz` or `.whl` file in the `dist/` directory.

### Step 2: Publish to PyPI

To publish the package to PyPI, use:

```bash
make publish
```

> **Note**: You’ll need PyPI credentials to publish.

---

## Clean-up

To remove temporary files and clean the environment:

```bash
make clean
```

This will delete the virtual environment and temporary files.

---

## Project Structure

The project is organized as follows:

```plaintext
web_scraper/
├── Makefile                  # Automates common tasks (install, test, run, clean, etc.)
├── README.md                 # Project documentation
├── dist/                     # Contains built distribution packages (after running `make build`)
├── poetry.lock               # Lock file for dependency management
├── pyproject.toml            # Project configuration and dependency file for Poetry
├── tests/                    # Unit tests for the scraper
│   ├── __init__.py
│   └── test_scraper.py       # Test suite for the scraper logic
└── web_scraper/              # Main application code
    ├── __init__.py           # Marks this directory as a Python package
    ├── __main__.py           # Entry point for running the scraper
    └── scraper.py            # Core logic for scraping repository data
```

### Explanation of Key Components:

- **Makefile**: Contains commands to simplify tasks, such as `make install`, `make test`, and `make run`.  
- **README.md**: Documentation for the project, including usage and setup instructions.  
- **dist/**: Automatically generated folder for distribution packages after building the project with `make build`.  
- **poetry.lock** and **pyproject.toml**: Files used by Poetry to manage dependencies and package configuration.  
- **tests/**: Contains unit tests to ensure the scraper functions as expected.  
  - `test_scraper.py`: Tests the functionality of `scraper.py` to validate scraping accuracy.  
- **web_scraper/**: Core Python package for the project.  
  - `__init__.py`: Initializes the package.  
  - `__main__.py`: Entry point script to run the scraper (`python -m web_scraper`).  
  - `scraper.py`: Contains the logic for fetching and processing repository data from GitHub profiles.  

---

## Features

- Extracts detailed repository data from GitHub profiles.  
- Saves extracted data into a well-structured CSV file.  
- Configurable scraping target via simple modifications (prompts for GitHub username).  
- Includes unit tests to ensure reliable performance.  
- Automates project setup, testing, and packaging via Makefile and Poetry.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/YourFeature`).  
3. Commit your changes (`git commit -m 'Add YourFeature'`).  
4. Push to the branch (`git push origin feature/YourFeature`).  
5. Open a pull request on GitHub.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

Have questions or suggestions? Feel free to [open an issue](https://github.com/Lahoussine-Bouhmou/web_scraper/issues) or contact me via email: `lahessine.bouhmou@gmail.com`.
