from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


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

'''
This is the automation framework for basic unit test.
'''


class testNro1HappyPath:
    def testNro1(self):
        # Open webpage
        driver.get("https://rootstack.com/es")
        time.sleep(3)
        # Close PopUp
        closePopUp = driver.find_element(By.CSS_SELECTOR, "span[aria-hidden='true']")
        closePopUp.click()
        # Reject Cookies
        cookie = driver.find_elements(By.CSS_SELECTOR,'button[class$="btn-secondary"]')
        cookie[1].click()
        # Change Lenguage to English:
        switchEnglish = driver.find_element(By.CSS_SELECTOR, ".inactive-lang-option")
        switchEnglish.click()
        # Go to form
        #goForms = driver.find_element(By.CSS_SELECTOR, "")
        time.sleep(3)

        # VARIABLES to use
        # X = driver.find_element(By.CSS_SELECTOR, "input[name='1963']")
        # X = driver.find_element(By.CSS_SELECTOR, "select[name='1963']")
        # X = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # Y = driver.find_element(By.CSS_SELECTOR, "")
        
        # INPUTS to use
        # X.send-keys("Luis")
        # Y.send-keys("allakssd@gmail.com")
        # Y.select_by_value("VE")
        # Y.select_by_visible_text("VE")
        # Skills = driver.find_elements(By.CSS_SELECTOR,'#react-select-2-input')
        # Skills.send-keys("Test")
        # Skills.send-keys(Keys.ENTER)
        # Skills.send-keys("Python")
        # Skills.send-keys(Keys.ENTER)
        # Skills.send-keys("React")
        # Skills.send-keys(Keys.ENTER)
        # SubmitBtn.click()
        # time.sleep(5)

        # assert driver.current_url == "https://webpage.com/es"





