import time

import pandas as pd
import undetected_chromedriver.v2 as webdriver
from webdriver_manager.chrome import ChromeDriverManager

# pip install undetected-chromedriver
# mozda treba napraviti folder -> C:\chrome_temp
# python=3.10.0


destination = []
price = []
airline = []
departure_date = []
date_of_arrival = []

if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.user_data_dir = "C:\chrome_temp"
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')

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

    gradovi = driver.find_elements_by_class_name(
        "BpkText_bpk-text__1KKbW.BpkText_bpk-text--xl__2xBzx.DealCard_DealCard__placeName__1CMcr")
    for grad in gradovi:
        destination.append(grad.text)

    cijene = driver.find_elements_by_class_name(
        "BpkText_bpk-text__1KKbW.BpkText_bpk-text--lg__212sq.DealCard_DealCard__price__1O9CP")
    for cijena in cijene:
        price.append(cijena.text)

    sub = []
    letovi = driver.find_elements_by_class_name("BpkText_bpk-text__1KKbW.BpkText_bpk-text--base__1zXAn")
    for let in letovi:
            sub.append(let.text)
    bus = []
    for s in sub:
        if len(s) > 4:
            bus.append(s)

    for bu, ba in enumerate(bus):
        if bu % 2 == 0:
            departure_date.append(ba)
        else:
            date_of_arrival.append(ba)

    prijevoznik = driver.find_elements_by_class_name("BpkText_bpk-text__1KKbW.BpkText_bpk-text--xs__11Wpt.DealCard_DealCard__carrier__2Sox7")
    for pr in prijevoznik:
        airline.append(pr.text)


    # print(len(destination))
    # print((destination))
    #
    # print(len(price))
    # print(price)
    #
    # print(len(departure_date))
    # print(departure_date)
    #
    # print(len(date_of_arrival))
    # print(date_of_arrival)

    # print(len(airline))
    # print(airline)

    letovi = pd.DataFrame({
        "Destination" : destination,
        "Prices" : price,
        "Departure date:" : departure_date,
        "Date of Arrival:" : date_of_arrival,
        "Airline" : airline
    })

    print(letovi.head())

    letovi.to_csv('letovi.csv')