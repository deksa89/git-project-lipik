import os
import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

journey_title = []
price = []
duration_days = []
travel_begins = []



options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.delete_all_cookies()
driver.start_client()

time.sleep(1)

driver.get("https://www.mondotravel.hr/europska-putovanja")


time.sleep(2)

try:
    driver.find_element_by_xpath("/html/body/div[2]/div/a[2]").click()
except:
    print("nisi pogodio")

time.sleep(2)

try:
    driver.find_element_by_xpath("//*[@id=\"loadMoreTripsApp\"]/div[2]/a/span").click()
except:
    print("nevalja")


gradovi = driver.find_elements_by_class_name("title-2.cl-1")
for gr in gradovi:
    journey_title.append(gr.text)

# trajanje = driver.find_elements_by_class_name("tag.has-icon.cl-4.inner-margin-0")
# for tr in trajanje:
#     duration_days.append(tr.text)
#
# cijena = driver.find_elements_by_class_name("cl-3")
# for c in cijena:
#     price.append(c.text)
#
# overlays = driver.find_elements_by_class_name("overlay")
# lista = []
# for ov in overlays:
#     hover = ActionChains(driver).move_to_element(ov)
#     hover.perform()
#     pocetak = driver.find_elements_by_class_name("info-wrap.center")
#
#     #print(pocetak.text)
#     sub = []
#     for p in pocetak:
#         if p.text == '':
#             pass
#         else:
#             sub.append(p.text)
#     lista.append(sub)
#
# for p in lista:
#     if p == []:
#         pass
#     else:
#         travel_begins.append(p)

print(journey_title)
# print(price)
# print(duration_days)
# print(travel_begins)



# putovanje = pd.DataFrame({'Ime putovanja': journey_title,
#                         'Cijena': price,
#                         'Trajanje putovanja': duration_days,
#                         'Početak putovanja': travel_begins,
#                         })
#
#
# print(putovanje.head())
