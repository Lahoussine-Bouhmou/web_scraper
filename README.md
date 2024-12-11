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

## Features
- Extracts detailed repository data from GitHub profiles.
- Saves data to a structured CSV file.
- Automated code quality checks with [Pylint](https://pylint.pycqa.org/) and [pre-commit hooks](https://pre-commit.com/).
- Enhanced logging for better debugging and tracking.
- Comprehensive documentation and tutorial.
- Automatically generates reference documentation using [Sphinx](https://www.sphinx-doc.org/).

---

## Prerequisites

Ensure the following are installed before using the project:

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency management and packaging)
- [Make](https://www.gnu.org/software/make/) (for automating tasks via Makefile)
- Optional: [pre-commit](https://pre-commit.com/) for pre-commit hooks

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

### Step 3: Install Pre-commit Hooks
Pre-commit hooks are automatically set up during `poetry install`. To set them up manually:
```bash
make hooks
```
Alternatively, you can run:
```bash
poetry run pre-commit install
```

---

## Static Code Analysis

This project uses [Pylint](https://pylint.pycqa.org/) for static code analysis.

### Step 1: Run Static Code Analysis
To manually run static code analysis, you can use either of these commands:

- Using `make`:
  ```bash
  make lint
  ```
- Alternatively, using Poetry:
  ```bash
  poetry run pylint web_scraper/
  ```

---

## Documentation

This project includes auto-generated reference documentation using [Sphinx](https://www.sphinx-doc.org/). You can generate the documentation by running:
```bash
make html
```
The generated documentation will be available at `_build/html/index.html`.

Additionally, a tutorial is available to guide you through the project setup and usage, located at: `docs/tutorials/tutorial.md`.

---

## Usage

### Step 1: Run the Scraper
To run the scraper and extract data from a GitHub user profile, execute the following command:
```bash
make run
```
You will be prompted to enter the GitHub username (e.g., `octocat`):
```plaintext
Enter the GitHub username to scrape: octocat
```

After entering the username, the scraper will fetch the repository details from the specified GitHub profile.

### Step 2: View Extracted Data
The extracted data is saved as a CSV file in the project directory. The filename will include the username, for example: `octocat_repositories.csv`.

#### Example CSV Format
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
Note: You’ll need PyPI credentials to publish.

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

```
web_scraper/
├── Makefile                  # Automates common tasks (install, test, run, clean, etc.)
├── README.md                 # Project documentation
├── dist/                     # Built distribution packages
├── poetry.lock               # Lock file for dependencies
├── pyproject.toml            # Project configuration file
├── tests/                    # Unit tests for the scraper
│   ├── __init__.py
│   └── test_scraper.py       # Test suite
├── web_scraper/              # Main application code
│   ├── __init__.py           # Package initialization
│   ├── __main__.py           # Entry point
│   └── scraper.py            # Core logic for scraping
├── _build/                   # Generated Sphinx documentation
├── _static/                  # Static assets for documentation
├── _templates/               # Templates for documentation
├── .pre-commit-config.yaml   # Pre-commit hooks configuration
├── .pylintrc                 # Pylint configuration
├── conf.py                   # Sphinx configuration
├── index.rst                 # Sphinx documentation index
├── repositories.csv          # Example output file
├── docs                      # Documentation files
│   └── tutorials             # Directory containing the tutorial
│       └── tutorial.md       # The project's tutorial documentation
```

### Explanation of Key Components:
- **Makefile**: Contains commands to simplify tasks, such as `make install`, `make test`, and `make run`.
- **README.md**: Documentation for the project, including usage and setup instructions.
- **dist/**: Automatically generated folder for distribution packages after building the project with `make build`.
- **poetry.lock** and **pyproject.toml**: Files used by Poetry to manage dependencies and package configuration.
- **tests/**: Contains unit tests to ensure the scraper functions as expected.
- **test_scraper.py**: Tests the functionality of `scraper.py` to validate scraping accuracy.
- **web_scraper/**: Core Python package for the project.
  - **__init__.py**: Initializes the package.
  - **__main__.py**: Entry point script to run the scraper (`python -m web_scraper`).
  - **scraper.py**: Contains the logic for fetching and processing repository data from GitHub profiles.
- **_build/**: Generated Sphinx documentation.
- **_static/**: Static assets for documentation.
- **_templates/**: Templates for documentation.
- **.pre-commit-config.yaml**: Pre-commit hooks configuration.
- **.pylintrc**: Pylint configuration file.
- **conf.py**: Sphinx configuration.
- **index.rst**: Sphinx documentation index.
- **docs/tutorials/tutorial.md**: The project's tutorial documentation.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add YourFeature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request on GitHub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

Have questions or suggestions? Feel free to open an issue or contact me via email: lahessine.bouhmou@gmail.com.
