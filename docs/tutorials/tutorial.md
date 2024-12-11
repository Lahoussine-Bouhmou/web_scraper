# **Web Scraper Project Tutorial**

Welcome to the tutorial for the **Web Scraper Project**! This guide will walk you through the steps to set up, run, and extend the project. By the end of this tutorial, you'll be able to scrape GitHub user repository data, analyze it, and understand how to contribute to the project.

---

## **Table of Contents**

1. [Prerequisites](#prerequisites)
2. [Getting Started](#getting-started)
   - [Step 1: Clone the Repository](#step-1-clone-the-repository)
   - [Step 2: Install Dependencies](#step-2-install-dependencies)
   - [Step 3: Install Pre-commit Hooks](#step-3-install-pre-commit-hooks)
3. [Running the Web Scraper](#running-the-web-scraper)
   - [Step 1: Execute the Scraper](#step-1-execute-the-scraper)
   - [Step 2: Enter GitHub Username](#step-2-enter-github-username)
   - [Step 3: View the Output](#step-3-view-the-output)
4. [Understanding the Code](#understanding-the-code)
   - [1. `scraper.py`](#1-scraperpy)
   - [2. Logging](#2-logging)
5. [Testing the Project](#testing-the-project)
   - [Step 1: Run Unit Tests](#step-1-run-unit-tests)
   - [Step 2: Analyze the Results](#step-2-analyze-the-results)
6. [Extending the Project](#extending-the-project)
   - [Add New Features](#add-new-features)
   - [Improve Documentation](#improve-documentation)
7. [Best Practices](#best-practices)
   - [1. Code Quality](#1-code-quality)
   - [2. Pre-commit Hooks](#2-pre-commit-hooks)
   - [3. Logging](#3-logging)
8. [FAQs](#faqs)
   - [1. Why is my CSV file empty?](#1-why-is-my-csv-file-empty)
   - [2. How do I run the scraper for another GitHub username?](#2-how-do-i-run-the-scraper-for-another-github-username)
   - [3. Can I scrape private repositories?](#3-can-i-scrape-private-repositories)
9. [Contributing](#contributing)
10. [Conclusion](#conclusion)

---

## **Prerequisites**

Before starting, ensure you have the following installed on your system:
- **Python 3.10+**
- **[Poetry](https://python-poetry.org/docs/#installation)** (for dependency management)
- **[Make](https://www.gnu.org/software/make/)** (optional but recommended for easier task automation)

---

## **Getting Started**

### **Step 1: Clone the Repository**

Begin by cloning the project repository:

```bash
git clone https://github.com/your-username/web_scraper.git
cd web_scraper
```

### **Step 2: Install Dependencies**

Now, install the required project dependencies using `Makefile`:

```bash
make install
```

Alternatively, if you prefer to use **Poetry** directly, you can run:

```bash
poetry install
```

This will create a virtual environment and install all necessary libraries for the project.

### **Step 3: Install Pre-commit Hooks**

Pre-commit hooks automate static code checks before committing your changes. To install the pre-commit hooks, run:

```bash
make hooks
```

---

## **Running the Web Scraper**

### **Step 1: Execute the Scraper**

To run the scraper, you can use the following command from the terminal:

```bash
make run
```

Alternatively, use Python directly:

```bash
poetry run python -m web_scraper
```

### **Step 2: Enter GitHub Username**

When prompted, enter the GitHub username whose repositories you want to scrape. For example:

```plaintext
Enter the GitHub username to scrape: octocat
```

### **Step 3: View the Output**

The scraper will fetch the repository data and save it to a CSV file named `<username>_repositories.csv`. For example, if you scraped the user `octocat`, the file would be named `octocat_repositories.csv`.

#### Example Output:

```csv
Repository Name,Visibility,Description,Programming Language,Stars,Forks
awesome-project,Public,An awesome project,Python,42,10
another-repo,Private,,JavaScript,10,2
```

The CSV will contain:
- **Repository Name**: The name of the repository.
- **Visibility**: Whether the repository is public or private.
- **Description**: A short description of the repository.
- **Programming Language**: The language used for the repository.
- **Stars**: Number of stars the repository has.
- **Forks**: Number of forks of the repository.

---

## **Understanding the Code**

### **1. `scraper.py`**

This file contains the core scraping logic, including:
- **`fetch_html(url: str)`**: Fetches the HTML content of a given GitHub profile URL.
- **`parse_repositories(html: str)`**: Parses the HTML to extract relevant repository information.
- **`save_to_csv(data: list, filename: str)`**: Saves the extracted repository data into a CSV file.

### **2. Logging**

The scraper uses **logging** to track and report on its operations. The logs are stored in `scraper_logging.log`.

#### Logging Levels:
- **DEBUG**: Detailed developer-level information (e.g., HTTP request status, response times).
- **INFO**: High-level operation details (e.g., successful fetch of HTML content).
- **WARNING**: Recoverable issues (e.g., missing repository descriptions).
- **ERROR**: Serious issues affecting functionality (e.g., HTTP errors).
- **CRITICAL**: Severe issues that prevent the program from running (e.g., failure to save data).

You can check this log file for insights into any potential issues with the scraping process.

---

## **Testing the Project**

### **Step 1: Run Unit Tests**

To verify that everything is functioning correctly, run the unit tests:

```bash
make test
```

### **Step 2: Analyze the Results**

After running the tests, you should see a summary similar to this:

```plaintext
================== test session starts ==================
collected 4 items

tests/test_scraper.py .....                             [100%]

=================== 4 passed in 1.02s ===================
```

This indicates that all tests passed successfully. If there are issues, pytest will display details of the failed tests.

---

## **Extending the Project**

### **Add New Features**

If you want to add new features to the project, follow these steps:
1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/NewFeature
   ```
2. Modify the `scraper.py` file or add new modules in the `web_scraper/` directory.
3. Write unit tests in the `tests/` directory to validate your changes.

### **Improve Documentation**

To improve or extend the documentation, edit files in the `docs/` directory. After making changes, regenerate the HTML documentation with:

```bash
make html
```

The generated documentation will be available in the `_build/html` directory.

---

## **Best Practices**

### **1. Code Quality**

Run static code analysis to ensure the quality of your code:

```bash
make lint
```

### **2. Pre-commit Hooks**

Pre-commit hooks are an essential tool for maintaining consistent code quality. Ensure they are installed and active:

```bash
make hooks
```

### **3. Logging**

Use the logging functionality to capture important information, especially when debugging or troubleshooting. Check the `scraper_logging.log` file for detailed logs.

---

## **FAQs**

### **1. Why is my CSV file empty?**

This can happen for the following reasons:
- The GitHub profile has no public repositories.
- The scraper encountered an error while fetching the HTML content. Check the `scraper_logging.log` file for more details.

### **2. How do I run the scraper for another GitHub username?**

Simply rerun the scraper and provide a new username when prompted.

### **3. Can I scrape private repositories?**

No, the current scraper only works with public repositories. Private repositories require proper authentication, which isn't part of this scraper.

---

## **Contributing**

We welcome contributions to this project! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them.
4. Push your changes to your fork:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request on GitHub.

---

## **Conclusion**

Congratulations! You've successfully learned how to set up, run, and extend the Web Scraper Project. Happy coding and scraping!
