
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement # This one is needed for the auto-completion of boxes_section_element
from selenium.webdriver.common.by import By


'''
This file will have the methods that will parse
specific data needed from each card box.
'''

class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        )
    
    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling hotel name
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            
            
            # Pulling hotel price
            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]'
            ).get_attribute('innerHTML').strip()
            

            # Pulling hotel score
            hotel_score = deal_box.find_element(
                By.CSS_SELECTOR, 'div[aria-label$="de 5"]'
            ).get_attribute(
                'aria-label'
            ).strip()
            
            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection
