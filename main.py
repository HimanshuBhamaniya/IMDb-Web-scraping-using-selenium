from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service   

driver = webdriver.Chrome()
file = 0
driver.get("https://www.imdb.com/chart/top/?ref_=hm_nv_menu")
elems = driver.find_elements(By.CLASS_NAME,"ipc-metadata-list-summary-item__c")
print(f"{len(elems)} elements found")
for elem in elems:
    d = elem.get_attribute("outerHTML")
    with open(f"data/IMDB_{file}.html", "w", encoding="utf-8") as f:
        f.write(d)
        file += 1
driver.close()