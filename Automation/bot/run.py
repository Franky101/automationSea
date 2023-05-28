from seleniumEasy.booking import Booking
from seleniumEasy.constants import BASE_URL
import time


place1 = 'Villa General Belgrano'


try:
    with Booking() as bot:

        bot.land_first_page()
        bot.close_pop_up()
        # bot.change_currency(currency='USD')
        bot.set_place(input('Where would you like to go?'))
        bot.select_dates(check_in_date='2023-05-29', 
                         check_out_date='2023-06-07') # Be aware that this only works in the same month.
        bot.select_adults(2)
        bot.submit_btn()
        bot.apply_filtrations()
        # print(len(bot.report_results()))
        bot.refresh() # Workaround to let the bot grab data better.

        bot.report_results()
        time.sleep(10)

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
