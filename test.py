from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# Add your options here
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

file = 0

# Load the webpage
for i in range(1, 21):
    driver.get(f"https://www.amazon.com/s?k=laptop&i=electronics&rh=n%3A172282%2Cp_123%3A219979%7C308445%7C391242&dc&page={i}&crid=I8G9EC239QAO&qid=1734139461&rnid=85457740011&sprefix=lap%2Caps%2C118&ref=sr_pg_1")
    # Locate the element
    try:
        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        print(f"Number of elements: {len(elems)}")
        for elem in elems:
            d = elem.get_attribute("outerHTML")
            with open(f"data/laptop_{file}.html","w",encoding="utf-8") as f:
                f.write(d)
                file += 1

    except Exception as e:
        print("Error locating element:", e)

    # Keep the browser open for observation
    time.sleep(10)
driver.close()