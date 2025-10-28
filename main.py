from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Configuration
URL = "https://member.emedny.org/pharmacy/search-locations"
OUTPUT_FILE = "pharmacies.csv"

# Selenium Setup
driver = webdriver.Chrome()
driver.get(URL)

wait = WebDriverWait(driver, 15)

# Select All Pharmacy Providers
service_select_elem = wait.until(EC.presence_of_element_located((By.ID, "serviceName")))
service_select = Select(service_select_elem)
service_select.select_by_value("ALL PHARMACY PROVIDERS")
print("Selected 'ALL PHARMACY PROVIDERS'")

# Get County Dropdown
county_select_elem = wait.until(EC.presence_of_element_located((By.ID, "countyName")))
county_select = Select(county_select_elem)

#Get Search Button
search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Search']")))

# Get county values
counties = [opt.get_attribute("value") for opt in county_select.options if opt.get_attribute("value")]

# Prepare csv file
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["County", "Name", "Category", "Address", "City, State", "Phone"])

    # Loop through each county
    for county in counties:
        print(f"\nScraping county: {county}")

        try:
            # Select the county
            county_select.select_by_value(county)

            # Click Search
            search_button.click()

            # Wait for results to appear
            wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".pad_5.page_container_color.mar_bot5.mar_left5")
            ))

            # Hack for rendering to page
            time.sleep(1.5)

            # Get all pharmacy entries
            pharmacy_divs = driver.find_elements(By.CSS_SELECTOR, ".pad_5.page_container_color.mar_bot5.mar_left5")

            for div in pharmacy_divs:
                lines = div.find_elements(By.CSS_SELECTOR, ".text")
                name = lines[0].text.strip() if len(lines) > 0 else ""
                category = lines[1].text.strip() if len(lines) > 1 else ""
                address = lines[2].text.strip() if len(lines) > 2 else ""
                city_state = lines[3].text.strip() if len(lines) > 3 else ""
                phone = lines[4].text.replace("Phone:", "").strip() if len(lines) > 4 else ""

                writer.writerow([county, name, category, address, city_state, phone])

            print(f"Extracted {len(pharmacy_divs)} pharmacies from {county.title()}")

        except Exception as e:
            print(f"Error scraping {county}: {e}")
            continue

print("\nAll counties saved to", OUTPUT_FILE)
driver.quit()

