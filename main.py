from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_olx_car_covers():
    # Setup headless Chrome
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    url = "https://www.olx.in/items/q-car-cover"
    driver.get(url)

    # Let page load
    time.sleep(5)

    # Parse HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    results = []

    # Find all item containers
    listings = soup.find_all("li", {"data-aut-id": "itemBox"})

    for item in listings:
        try:
            title = item.find("span", {"data-aut-id": "itemTitle"}).text.strip()
            price = item.find("span", {"data-aut-id": "itemPrice"}).text.strip()
            location = item.find("span", {"data-aut-id": "item-location"}).text.strip()
            results.append({"Title": title, "Price": price, "Location": location})
        except:
            continue

    # Save to CSV
    df = pd.DataFrame(results)
    df.to_csv("olx_car_covers.csv", index=False)
    print("Scraped", len(results), "results. Saved to olx_car_covers.csv.")

if __name__ == "__main__":
    scrape_olx_car_covers()
