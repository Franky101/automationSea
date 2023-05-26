from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

# Notas for Frank of the future: This code might not work in double screen! I would need to set_window_position(2000,0) to make it work and the maximize_window() and then time.sleep(x)

# Open the website
driver.get("https://www.booking.com/")




print('STARTING TESTS')
time.sleep(3)
print('Sleeped for 3 seconds already')
title = driver.title
print('    ' + title)

# Pressing ESCAPE on body
print("Pressing ESCAPE on body element")
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

print('SELECTING LOCATION')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ce45093752")))\
        .send_keys('Villa General Belgrano')

time.sleep(1)

ActionChains(driver).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()

time.sleep(1)

print('SELECTING DATES')
desired_start_date = '2023-05-24'
desired_end_date = '2023-06-03'

start_locator = f'//span[@data-date="{desired_start_date}"]'
end_locator = f'//span[@data-date="{desired_end_date}"]'

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[1]")))\
        .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[1]")))\
        .click()

WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, start_locator))).click()
WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, end_locator))).click()

print('ADDING PEOPLE')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.d47738b911 b7d08821c3".replace(' ', '.'))))\
        .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]")))\
        .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc63351294 a822bdf511 e2b4ffd73d f7db01295e c938084447 a9a04704ee d285d0ebe9".replace(' ', '.'))))\
        .click()


print('PRESSING BUTTON FOR SEARCH')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc63351294 a822bdf511 d4b6b7a9e7 cfb238afa1 c938084447 f4605622ad aa11d0d5cd".replace(' ', '.'))))\
        .click()



print('PICKING PLACES TEST')

# Find all the cards on the current page
cards1 = driver.find_elements(By.CLASS_NAME, "a826ba81c4.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942")

print('CARDS FOUND:')
print(cards1)

# Iterate through each card and extract information for "Villa General Belgrano"
place = "Villa General Belgrano"
place_location = '//span[@data-testid="address"]'
price_location = '//span[@data-testid="price-and-discounted-price"]'
title_location = '//div[@data-testid="title"]'

for card in cards1:
    place_name = card.find_element(By.XPATH, place_location).text
    if place in place_name:
        # Extract and save the desired information from the card
        place = card.find_element(By.XPATH, place_location).text
        price = card.find_element(By.XPATH, price_location).text
        title = card.find_element(By.XPATH, title_location).text
        print("-----------------")
        print('Place: ' + place)
        print('Name: ' + title)
        print('Price: ' + price)
        print("-----------------")
        # Save the extracted information to a file or perform further processing
        



'''
places = driver((By.CSS_SELECTOR, 'div.d4924c9e74'))
places = places.text
print(places)
'''

# Wait before finish
time.sleep(300)
print('Sleeped for 3 seconds already')
driver.quit