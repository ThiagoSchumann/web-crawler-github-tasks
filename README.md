# Web Crawler GitHub Tasks

[Leia em português](README-ptbr.md)

## Description

This project automates the process of creating tasks on GitHub Projects using Selenium. It reads predefined tasks from a data file and uses Selenium to log in to GitHub and add these tasks to a specified project.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Important Files and Directories](#important-files-and-directories)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Structure

```plaintext
[project-root]/
├── .gitignore
├── README.md
├── README-ptbr.md
├── config.py
├── main.py
├── requirements.txt
├── driver/
│   ├── chromedriver
│   └── chromedriver.exe
├── services/
│   ├── selenium_service.py
│   └── __init__.py
├── data/
│   ├── cards.py
│   └── __init__.py
```

## Setup

### Installation

1. **Clone the repository:**
    
    ```bash
    git clone https://github.com/ThiagoSchumann/web-crawler-github-tasks
    cd web-crawler-github-tasks
    ```
    
2. **Install the required packages:**
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Download WebDriver:**
    
    Download the appropriate WebDriver for your browser and operating system, and place it in the `driver/` directory. Update the path in `config.py` if necessary.

### Configuration

1. **Create a `.env` file:**
    
    Create a `.env` file in the root directory with your necessary environment variables:
    
    ```env
    EMAIL=your_github_email
    PASSWORD=your_github_password
    ```
    
2. **Update `config.py`:**
    
    Ensure `config.py` has the correct paths and URLs:
    
    ```python
    from decouple import config

    EMAIL = config("EMAIL")
    PASSWORD = config("PASSWORD")
    DRIVER_PATH = "driver/chromedriver.exe"  # Adjust this path if using a different OS
    GITHUB_LOGIN_URL = "https://github.com/login"
    PROJECT_URL = "https://github.com/users/ThiagoSchumann/projects/10"
    ```

## Usage

1. **Run the main script:**
    
    ```bash
    python main.py
    ```
    
2. **Automated Tasks:**
    
    The script will log in to GitHub, navigate to the specified project, and add tasks defined in `data/cards.py`.

## Important Files and Directories

- **main.py**: The main script that runs the Selenium automation.
- **config.py**: Loads environment variables and configuration settings.
- **services/selenium_service.py**: Contains the Selenium logic for interacting with GitHub.
- **data/cards.py**: Contains the card data to be used in the project.

## Features

- **Automated Login**: Logs in to GitHub using provided credentials.
- **Task Addition**: Adds predefined tasks to a specified GitHub project.

## Technologies Used

- **Backend**: Python, Selenium
- **Configuration Management**: Python-Decouple

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For support or feedback, please contact [thiagoarturschumann@gmail.com](mailto:thiagoarturschumann@gmail.com).