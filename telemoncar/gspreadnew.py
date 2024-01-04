import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Replace 'path/to/your/credentials.json' with the path to your generated JSON file
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('lofty-fragment-409309-dc159bba07fc.json', scope)

# Authorize the client
client = gspread.authorize(credentials)
# print(client)

# Open a spreadsheet by name
sheet = client.open('usedet')

# Or open by URL
# sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1Yohr18J_x-qwIz7Cc4r47yZZVYKoWIcFQxE66GHfxRA/edit?usp=sharing')
# Get the first sheet
worksheet = sheet.sheet1

# Read data from a specific cell
cell_value = worksheet.cell(1, 1).value
print(cell_value)
# Get all values from a range
all_values = worksheet.get_all_values()
print(all_values)
insertRow = ["Zayn","Malik",12,20]
worksheet.insert_row(insertRow,6)

data = worksheet.get_all_values()
num_rows_filled = len(data)
print(num_rows_filled)
for row in data:
    print(row)
row = 3
col = 2  # B column
value = "Hello, World!"

worksheet.update_cell(row, col, value)