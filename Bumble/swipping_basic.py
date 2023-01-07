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
web = 'https://bumble.com/app'

# loan bumble
driver.get(web)