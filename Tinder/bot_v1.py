import random
import time
import pyautogui as pyaut

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

### Accessing tinder in chrome ###

# chrome driver info
chrome_driver_path = '/Users/hmartin6/Repos_Support/Dating_App_Bots/Tinder/chromedriver'
service = Service(executable_path=chrome_driver_path)

options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222") #chrome debugger info

driver = webdriver.Chrome(service=service, options=options)

# web address
web = 'https://tinder.com/'

### Swiping ###

# TODO
# Exit the match screen to prevent failures when pop up

like_ratio_rand = random.randint(10, 20)
swipe_sesh = 20

while True:
    i = 0
    driver.get(web)  # open tinder in chrome
    time.sleep(5)
    for i in range(swipe_sesh):
        try:
            score = random.randint(0, 100) #attractiveness - rand for now
            if score > like_ratio_rand:
                # liking someone
                like_xpath = '//button//span[text()="Like"]' #like button element
                like_location = driver.find_element(by='xpath', value=like_xpath) #find the like button
                driver.execute_script("arguments[0].click();", like_location) #click on like
            else:
                # noping someone
                nope_xpath = '//button//span[text()="Nope"]'  # like button element
                nope_location = driver.find_element(by='xpath', value=nope_xpath)  # find the like button
                driver.execute_script("arguments[0].click();", nope_location)  # click on like

            # moving mouse and clicking
            if i % 2 == 0:
                pyaut.moveRel(0, 30)
            else:
                pyaut.moveRel(0, -30)
            pyaut.click()
            i+=1

            # pause between swipes
            sleep_time = random.randint(2, 4)
            time.sleep(sleep_time)  # pause from a random amount of seconds to stop bot protection

            # closing match pop up
            close_match_xpath = '//button[@title=Back to Tinder"]'
            close_match_window = driver.find_element(by='xpath', value =close_match_xpath)
            close_match_window.click()
            time.sleep(1)

        except:
            try:
                # closing pop ups
                pop_up_close_txt_xpath = '//button/span[text()="Maybe Later"] | //button/span[text()="Not interested"] | //button/span[text()="No Thanks"]'
                close_pop_up = driver.find_element(by='xpath', value=pop_up_close_txt_xpath)
                close_pop_up.click()
            except:
                pass
