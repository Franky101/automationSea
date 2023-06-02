import requests
from prettytable import PrettyTable
import re

# GET request to the API from dummyjson.com
api_url = 'https://dummyjson.com/users'
response = requests.get(api_url)

# Assigning the JSON response to a variable
api_response = response.json()

# Verify the API response
assert api_response['total'] == 100
assert len(api_response['users']) <= 50
assert api_response['users'][0]['firstName'] == 'Terry'
assert api_response['users'][0]['lastName'] == 'Medhurst'
# No empty fields
for user in api_response['users']:
    assert user['username'] != ''
    assert user['username'] != ' '
    assert user['firstName'] != ''
    assert user['lastName'] != ''
# Correct email formats
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
for user in api_response['users']:
    assert re.match(email_pattern, user['email']) is not None
    

# Create a PrettyTable instance
table = PrettyTable()
table.field_names = ['ID', 'First Name', 'Last Name', 'Email']
table.align = 'l'
table.border = True


# Populate the table with user data
for user in api_response['users']:
    table.add_row([user['id'], user['firstName'], user['lastName'], user['email']])

# Print the formatted table
print(table)