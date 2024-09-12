LinkedIn Scraper with Selenium
This repository contains a Python script that uses Selenium to scrape data from LinkedIn.

Table of Contents
Prerequisites
Installation
Usage
Code Explanation
Prerequisites
Python 3.6 or higher
Selenium WebDriver (e.g. ChromeDriver)
pip (Python package manager)
Visual Studio Code (VSCode)
A LinkedIn account (username and password)
Installation
Clone this repository using git clone https://github.com/hichri-mo/data-TWH-selenium.git
Install the required packages by running pip install -r requirements.txt in the terminal
Download the Selenium WebDriver for your preferred browser (e.g. ChromeDriver) and add it to your system's PATH
Create a .env file in the root directory and add your LinkedIn username and password as environment variables:
email=your_email
password=your_password
		
Usage
Open the repository in VSCode
Run the script by clicking the "Run Code" button or pressing F5
The script will open a browser window and navigate to the LinkedIn login page
The script will then login to LinkedIn using the credentials in the .env file
The script will then navigate to the specified LinkedIn company page and scrape the data
The scraped data will be saved to a file named scraped_data.txt in the root directory
Code Explanation
This script uses Selenium to:

Login to LinkedIn using the provided credentials
Navigate to the specified LinkedIn company page
Scrape the data from the page using CSS selectors
Save the scraped data to a file
The script uses the following environment variables:

email: your LinkedIn email address
password: your LinkedIn password
Note: This script is for educational purposes only and should not be used for commercial purposes without permission from LinkedIn. Also, make sure to check LinkedIn's terms of use and robots.txt file before scraping data.

License
This repository is licensed under the MIT License. See LICENSE for details.
