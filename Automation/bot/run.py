from seleniumEasy.booking import Booking
from seleniumEasy.constants import BASE_URL
import time

with Booking() as bot:
    bot.land_first_page()
    bot.close_pop_up()
    # bot.change_currency(currency='USD')
    bot.set_place('Villa General Belgrano')
    bot.select_dates(check_in_date='2023-05-29', check_out_date='2023-06-07') # Be aware that this only works in the same month.
    bot.select_adults(2)
    bot.submit_btn()