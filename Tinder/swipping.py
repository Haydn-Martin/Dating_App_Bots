import random
import time
import pandas as pd
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

# boys names csv
name_df = pd.read_csv('name_gender_dataset.csv', header=0)

# Set comprehension
# new_set = {set.lower() for item in old_set}

### Swiping ###

# TODO
# Set profile to bisexual
    # See how effective it is
    # Add to swipping_click
# Messaging
    # At end of round --> review new matches
    # Get name and send name all in caps until no matches left
    # Then start new round
# Hacks
    # Go to different location
    # Reset account
    # Message straight away

# Functions

def click_mouse(counter):
    if counter % 2 == 0:
        pyaut.moveRel(0, 30)
    else:
        pyaut.moveRel(0, -30)
    pyaut.click()

def name_gender():
    name_xpath = '//*[@id="q-401777178"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[1]/div/div/span | //*[@id="q-401777178"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[4]/div/div[1]/div/div[1]/span | //*[@id="q-401777178"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[1]/div/div[1]/span' #find name
    name_location = driver.find_element(by='xpath', value=name_xpath) #find the name
    prof_name = name_location.text #save the name
    try:
        return name_df[name_df['Name'] == prof_name]['Gender'].iloc[0]
    except:
        return 'M' # If can't find name, treat as man

def swipe_right():
    like_xpath = '//button//span[text()="Like"]'  # like button element
    like_location = driver.find_element(by='xpath', value=like_xpath)  # find the like button
    driver.execute_script("arguments[0].click();", like_location)  # click on like

def swipe_left():
    nope_xpath = '//button//span[text()="Nope"]'
    nope_location = driver.find_element(by='xpath', value=nope_xpath)
    driver.execute_script("arguments[0].click();", nope_location)

def close_match_pu():
    close_match_xpath = '//*[@id="q-71405977"]/main/div/div[1]/div/div[4]/button/svg/path'
    close_match_window = driver.find_element(by='xpath', value=close_match_xpath)
    close_match_window.click()

def close_pu():
    pop_up_close_txt_xpath = '//button/span[text()="Maybe Later"] | //button/span[text()="Not interested"] | //button/span[text()="No Thanks"]'
    close_pop_up = driver.find_element(by='xpath', value=pop_up_close_txt_xpath)
    close_pop_up.click()

#like_ratio_rand = random.randint(10, 20)
swipe_sesh = 100
need_click = True

while True:
    i = 0
    driver.get(web)  # open tinder in chrome
    time.sleep(3)
    for i in range(swipe_sesh):
        try:
            if name_gender() == 'M':
                swipe_left()
            else:
                #score = random.randint(0, 100)  # attractiveness - rand for now
                #if score > like_ratio_rand:
                swipe_right()
                # closing match box
                time.sleep(1)
                close_match_pu()
            # pause between actions
            sleep_time = random.randint(1, 2)
            time.sleep(sleep_time)  # pause from a random amount of seconds to stop bot protection
            # click mouse to keep laptop active
            if need_click:
                click_mouse(i)
            i += 1
        except:
            try:
                close_pu()
            except:
                pass