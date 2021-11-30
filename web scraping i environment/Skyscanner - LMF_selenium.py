import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver




destination = []
price = []
airline = []
departure_date = []
date_of_arrival = []


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.delete_all_cookies()
driver.start_client()
time.sleep(1)
driver.get("https://www.skyscanner.net/hr/en-gb/hrk/flights/last-minute-deals/")
time.sleep(2)
try:
    driver.find_element_by_xpath("//*[@id=\"acceptCookieButton\"]").click()
except:
    print("No Cookie")
time.sleep(5)
while True:
    try:
        driver.find_element_by_xpath("//*[@id=\"flight-deals-root\"]/div/div[2]/button").click()
        time.sleep(1)
    except:
        break

gradovi = driver.find_elements_by_class_name("DealCard_DealCard__imageContent__1m7ud")
for grad in gradovi:
    destination.append(grad.text)

cijena = driver.find_elements_by_class_name("DealCard_DealCard__fromPrice__3oxcA")
print(cijena[1].text)
# for cj in cijena:
#     print(cj.text)



print("end")
