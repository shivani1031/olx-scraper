#  OLX Car Cover Scraper

This Python project uses **Selenium** to scrape car cover listings from [OLX India](https://www.olx.in/) and saves the extracted data into a CSV file.

##  Features

- Scrapes product **titles**, **prices**, **locations**, and **listing links**
- Saves results to a CSV file (`olx_scraped_results.csv`)
- Automatically scrolls to load more results
- Designed to work with the OLX search results page for `car cover`

##  Technologies Used

- Python 3.11+
- Selenium
- Chrome WebDriver
- Pandas

##  Output

The script generates a CSV file named `olx_scraped_results.csv` containing:
- `Title`
- `Price`
- `Location`
- `Date`
- `Link`

##  Getting Started

### 1. Clone the repo

git clone https://github.com/YOUR_USERNAME/olx-scraper.git
cd olx-scraper


### 2. Install dependencies
Make sure you have pip and run:

pip install -r requirements.txt

If you don’t have a requirements.txt, install manually:
pip install selenium pandas
