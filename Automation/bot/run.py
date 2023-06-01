from seleniumEasy.booking import Booking
from seleniumEasy.constants import BASE_URL
import time

'''
This code will interact and test reservation functionalities in booking.com

- It will open the website
- It will close the pop-up
- It will select the place
- It will select the dates
- It will select the number of adults
- It will submit the search
- It will apply filtrations
- It will report the results
- It will close the browser
'''


place1 = 'Villa General Belgrano'


try:
    with Booking() as bot:

        bot.land_first_page()
        bot.close_pop_up()
        # bot.change_currency(currency='USD')
        # bot.set_place(input('Where would you like to go?'))
        bot.set_place('Villa General Belgrano')
        bot.select_dates(check_in_date='2023-05-29', 
                         check_out_date='2023-06-07') # Be aware that this only works in the same month.
        bot.select_adults(2) # If we add an input here, it must be passed to INT since input creates an STR
        bot.submit_btn()
        bot.apply_filtrations()
        # print(len(bot.report_results()))
        bot.refresh() # Workaround to let the bot grab data better.
        bot.report_results()
        # bot.select_card()
        bot.go_back()
        time.sleep(60)

except Exception as e:
    # Catching exception msg... just a practice, not needed in this case.
    if 'in PATH' in str(e):
        print('Problem running program from command line.\n'
              'Check that you are using WebDriver Manager to solve this issue.\n'
              'If you want to use the webdriver file, add the path. \n'
              'Windows: \n'
              '     set PATH=%PATH%;C:path-to-your-file-folder \n \n'
              'Linux: \n'
              '     PATH=$PATH:/path/to/your/folder \n'
              ) # Problem solved with WebDriver Manager :)
    else:
        raise
