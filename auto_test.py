from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.magicbricks.com/property-for-sale-rent-in-Mumbai/residential-real-estate-Mumbai/?mbtracker=google_paid_brand_other&ccode=brand_1_sem&gad_source=1&gad_campaignid=300989217&gbraid=0AAAAADtFk5UyS-Wvr8gYkMiicaZmvgMeC&gclid=CjwKCAiAnoXNBhAZEiwAnItcG-bvcR8B0lsyNxzO3xjTxg1x9O75diMn5uH_zaAwU5BqPjXmdD1H5hoC4LwQAvD_BwE")

time.sleep(2)

see_all_properties = driver.find_element(By.XPATH, '//*[@id="owner-properties"]/div/section/div[1]/a')
see_all_properties.click()

time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])

print("Now URL is:", driver.current_url)
time.sleep(5)

# properties = driver.find_elements(By.XPATH,"//h2[contains(@class,'mb-srp__card--title')]")


# for prop in properties:
#     text = prop.text.strip()
#     if text != "":
#         print(text)

# prices = driver.find_elements(By.CLASS_NAME, "mb-srp__card__price--amount")

# for pr in prices:
#     text = " ".join(pr.text.split())   # removes newline automatically
#     print(text)

property_dict = {}

cards = driver.find_elements(By.XPATH, "//div[contains(@class,'mb-srp__card')]")

print("Total cards found:", len(cards))

for card in cards:
    try:
        # Property Name
        name = card.find_element(
            By.XPATH,
            ".//h2[contains(@class,'mb-srp__card--title')]"
        ).text.strip()

        # Price
        price = card.find_element(
            By.CLASS_NAME,
            "mb-srp__card__price--amount"
        ).text
        
        price = " ".join(price.split())
        if name and price:
            property_dict[name] = price

    except:
        continue

# Print dictionary
print("\nProperty Dictionary:\n")
print(property_dict)

print("\nTotal stored:", len(property_dict))