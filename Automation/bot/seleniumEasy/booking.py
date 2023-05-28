import seleniumEasy.constants as const
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from seleniumEasy.booking_filtration import BookingFiltration
from seleniumEasy.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown # Not working. reason unknown
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        options.add_experimental_option('excludeSwitches', ['enable-logging']) # To skip DEVICE_logging errors.
        service = ChromeService(ChromeDriverManager().install())  # Instantiate ChromeService
        
        super(Booking, self).__init__(service=service, options=options, desired_capabilities=None)
        self.implicitly_wait(5)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit() # Not Working...
    
    def land_first_page(self):
        self.get(const.BASE_URL)
        time.sleep(1)

    def close_pop_up(self):
        try:
            close_btn = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Ignorar información sobre el inicio de sesión."]'
            )
            close_btn.click()
        except:
            print("Pop-up didn't show up.")

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        selected_currency_element = self.find_element(
            By.XPATH, f'//div[contains(text(), "{currency}")]'
        )
        selected_currency_element.click()
    
    def set_place(self, place_to_go):
        search_field = self.find_element(
            By.ID, ':Ra9:'
        )
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_option_location = self.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div/div[2]/ul/li[1]'
        )
        first_option_location.click()
        time.sleep(1)
    
    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]'
        )
        check_in_element.click()
        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]'
        )
        check_out_element.click()
        
    def select_adults(self, count=1):
        selection_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]'
        )
        selection_element.click()
        # Reduce the value to 1
        # If value of adults reaches 1, then we should get out of the loop
        while True:
            decrease_element = self.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]'
            )
            adult_count_element = self.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/span'
            )
            if int(adult_count_element.text) == 1:
                break
            decrease_element.click()

        increase_button_element = self.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]'
        )
        for _ in range(count - 1):
            increase_button_element.click()

    def submit_btn(self):
        search_button = self.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        )
        search_button.click()

    
    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self) # instance
        filtration.apply_start_rating(3,5)
        filtration.sort_price_low()
        time.sleep(3)


    def report_results(self):
        
        hotel_boxes = self.find_element(
            By.CLASS_NAME, 'd4924c9e74'
        )
        report = BookingReport(hotel_boxes)
        print(report.pull_deal_box_attributes())

        table = PrettyTable ()
        table.field_names = ['Name','Price','Score']
        table.add_rows(report.pull_deal_box_attributes())
        table.align = 'l'
        table.border = True
        print(table)
'''     
        table = PrettyTable(
            field_names = ['Hotel Name','Hotel Price','Hotel Score']
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)

'''

        



        
    



        


