from selenium import webdriver
from datetime import datetime
import time

driver = webdriver.Chrome(r'chromedriver.exe')

# Load Whatsapp Web page
driver.get("https://web.whatsapp.com/")

name="Niharika"
time.sleep(30)
try:
        chat=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div")
        chat.click()
        time.sleep(2)
        search=driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]')
        search.click()
        time.sleep(2)
        search.send_keys(name)
        time.sleep(2)
        open=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div")
        open.click()
        time.sleep(2)


        while True: # This loop continues forever. Even If internet connection breaks and reconnects, this will help to find for the status again.
            try:
                status = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span').text
                print("status \n")
                print("{0}".format(status))
                now = datetime.now()

                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)
                time.sleep(10)
            except:
                pass

except:
            pass