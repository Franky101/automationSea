from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigator options (Maximized, extensions disabled)
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(5) # This applies to all elements! If something is not found, the test will finish in 5 sec.

assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title

print(driver.title)
'''
# FINDING ELEMENT AND SEND ACTIONS
selectSearch = driver.find_element(By.CSS_SELECTOR, 'input[title="Enter the terms you wish to search for."]')
selectSearch.click()
selectSearch.send_keys("Python tutorial")
'''
try:
    no_button = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    no_button.click()
except:
    print('No element with this class name, Skipping ...')


enterMessage = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="message"]')
enterMessage.send_keys("RockPapperBobWasHere")

btnShowMessage = driver.find_element(By.CSS_SELECTOR, 'button[onclick="showInput();"]')
btnShowMessage.click()

enterValue1 = driver.find_element(By.CSS_SELECTOR, 'input[name="sum1"]')
enterValue1.send_keys("561")

enterValue2 = driver.find_element(By.CSS_SELECTOR, 'input[name="sum2"]')
enterValue2.send_keys("655")

btnGetTotal = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btnGetTotal.click()

# CHANGING TO NEXT PAGE
driver.get("http://demo.seleniumeasy.com/basic-checkbox-demo.html")



'''
# WEBDRIVER WAIT TO SOMETHING SHOW UP
WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'button[type="submit"]') , # Element Filtration
        'Complete' # The Expected text
    )
)

'''

time.sleep(10)



# progress_element = driver.find_element(By.CLASS_NAME, "progress-label")