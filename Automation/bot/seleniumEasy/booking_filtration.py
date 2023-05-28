'''
This file will include a class with instance methods.
That will be responsble to interact with our website
After we have some results, to apply filtrations.
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_start_rating(self, *star_values): # * Creates an arbitrary argument, similar to *args
        start_filtration_box = self.driver.find_element(
            By.ID, 'filter_group_class_:R14q:'
        )
        # Filter throught start_filtration_box
        start_child_elements =  start_filtration_box.find_elements(
            By.CSS_SELECTOR, '*'
        )
        # Adding one star_values
        for star_value in star_values:    
            for start_element in start_child_elements:
                if str(start_element.get_attribute('innerHTML')).strip() == f'{star_value} estrellas': # Convention to find inner element of html file.
                    start_element.click()
    def sort_price_low(self):
        # Open dropdown of filters
        element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'
        )
        element.click()
        
        # Selecting low price filter
        element_low_price = self.driver.find_element(
            By.XPATH, f'//span[contains(text(), "Precio (más bajo primero)")]'
        )
        element_low_price.click()

    

