from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_olx_items(query_url, scroll_count=5):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=options)

    driver.get(query_url)
    time.sleep(4)

    # Scroll multiple times to load all listings
    for _ in range(scroll_count):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    listings = soup.find_all("li", {"data-aut-id": lambda x: x and x.startswith("itemBox")})
    print(f"🔍 Found {len(listings)} listings.")

    results = []

    for li in listings:
        try:
            title = li.find("span", {"data-aut-id": "itemTitle"})
            price = li.find("span", {"data-aut-id": "itemPrice"})
            location = li.find("span", {"data-aut-id": "item-location"})
            link = li.find("a", href=True)
            image = li.find("img")

            results.append({
                "Title": title.text.strip() if title else "N/A",
                "Price": price.text.strip() if price else "N/A",
                "Location": location.text.strip() if location else "N/A",
                "URL": "https://www.olx.in" + link['href'] if link else "N/A",
                "Image": image['src'] if image and image.has_attr('src') else "N/A"
            })
        except Exception as e:
            continue

    if results:
        print(f"\n✅ {len(results)} listings extracted.")
        pd.DataFrame(results).to_csv("olx_scraped_results.csv", index=False)
        print("📁 Data saved to 'olx_scraped_results.csv'.")
    else:
        print("❌ No results extracted. Try increasing scroll count or verifying selectors.")

if __name__ == "__main__":
    # Example search: OLX Car Covers (can be changed)
    scrape_olx_items("https://www.olx.in/spare-parts_c1585/q-car-cover", scroll_count=7)
