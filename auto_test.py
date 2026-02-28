from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from openpyxl import Workbook

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

for i in range(10):
    driver.execute_script("window.scrollBy(0, 3000);")
    time.sleep(2)

cards = driver.find_elements(
    By.XPATH,
    "//div[contains(@class,'mb-srp__card')]"
)
# properties = driver.find_elements(By.XPATH,"//h2[contains(@class,'mb-srp__card--title')]")


# for prop in properties:
#     text = prop.text.strip()
#     if text != "":
#         print(text)

# prices = driver.find_elements(By.CLASS_NAME, "mb-srp__card__price--amount")

# for pr in prices:
#     text = " ".join(pr.text.split())   # removes newline automatically
#     print(text)

# property_dict = {}

# cards = driver.find_elements(By.XPATH, "//div[contains(@class,'mb-srp__card')]")

# print("Total cards found:", len(cards))

# for card in cards:
#     try:
#         # Property Name
#         name = card.find_element(
#             By.XPATH,
#             ".//h2[contains(@class,'mb-srp__card--title')]"
#         ).text.strip()

#         # Price
#         price = card.find_element(
#             By.CLASS_NAME,
#             "mb-srp__card__price--amount"
#         ).text

#         price = " ".join(price.split())

        
#         if name and price:
#             property_dict[name] = price

#     except:
#         continue
# property_dict = {}

# for card in cards:
#     try:
#         name = card.find_element(
#             By.XPATH,
#             ".//h2[contains(@class,'mb-srp__card--title')]"
#         ).text.strip()

#         price = card.find_element(
#             By.CLASS_NAME,
#             "mb-srp__card__price--amount"
#         ).text
#         price = " ".join(price.split())

#         # Owner
#         owner_elements = card.find_elements(
#             By.CLASS_NAME,
#             "mb-srp__card__ads--name"
#         )

#         if owner_elements:
#             owner = owner_elements[0].text.strip()
#             owner = owner.replace("Owner:", "").strip()
#         else:
#             owner = "Owner Not Available"

#         if name and price:
#             property_dict[name] = price

#             print("Owner:", owner)
#             print({name: price})
#             print("-" * 50)

#     except:
#         continue

# # Print dictionary
# print("\nProperty Dictionary:\n")
# print(property_dict)

# print("\nTotal stored:", len(property_dict))

# wb = Workbook()
# ws = wb.active
# ws.title = "MagicBricks Data"

# # Add headers
# ws.append(["Property Name", "Price"])

# # Add data
# for name, price in property_dict.items():
#     ws.append([name, price])

# # Save file
# wb.save("magicbricks_properties1.xlsx")

# print("Excel file created successfully!")
# print("Total stored:", len(property_dict))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?cityName=Mumbai")

time.sleep(5)

# Scroll 10 times
for i in range(10):
    driver.execute_script("window.scrollBy(0, 3000);")
    time.sleep(2)

# Get all property cards
cards = driver.find_elements(
    By.XPATH,
    "//div[contains(@class,'mb-srp__card')]"
)

print("Total cards found:", len(cards))

# Dictionary: Owner → List of properties
property_dict = {}

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

        # Owner
        owner_elements = card.find_elements(
            By.CLASS_NAME,
            "mb-srp__card__ads--name"
        )

        if owner_elements:
            owner = owner_elements[0].text.strip()
            owner = owner.replace("Owner:", "").strip()
        else:
            owner = "Owner Not Available"

        # Store data
        if owner not in property_dict:
            property_dict[owner] = []

        property_dict[owner].append({
            "Property Name": name,
            "Price": price
        })

    except:
        continue

# Print dictionary
print("\nFinal Dictionary:\n")
print(property_dict)

print("\nTotal Owners:", len(property_dict))

# ===============================
# Save to Excel
# ===============================

wb = Workbook()
ws = wb.active
ws.title = "MagicBricks Data"

# Headers
ws.append(["Owner Name", "Property Name", "Price"])

for owner, properties in property_dict.items():
    for prop in properties:
        ws.append([owner, prop["Property Name"], prop["Price"]])

wb.save("magicbricks_properties.xlsx")

print("\nExcel file created successfully!")
driver.quit()