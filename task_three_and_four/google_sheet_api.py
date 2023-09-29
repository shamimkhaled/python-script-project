import gspread
import pandas as pd
import gspread_dataframe

# Authenticate using service account credentials to set the file path of secret_key.json
gc = gspread.service_account(filename=r"C:\Users\iamkh\OneDrive\Desktop\task_three_and_four\secret_key.json")

# Define the google sheet key
google_sheet_key = '1rr7KhC6JAVwdJ7m6KRzMxN8-Dt6dbzjPJYpnWrssNQw'

# Open to the google sheet
work_sheet = gc.open_by_key(google_sheet_key)

# Display the how many worksheet in the Google Sheet
print(work_sheet.worksheets())

# Access to the specific worksheet
current_sheet = work_sheet.worksheet('Sheet1')

print(current_sheet.get_all_records())

# To get a cell value
print( current_sheet.acell('B2').value)

# To update a cell value - update_cell(row_number, column_number, value)
current_sheet.update_cell(5, 4, 'test_value')

# Ready to data for dataframe
data = {
    "entry1": {"BookTitle": "A Light in the Attic", "StarRating": "Three", "Price": 51.77},
    "entry2": {"BookTitle": "Tipping the Velvet", "StarRating": "One", "Price": 53.74},
    "entry3": {"BookTitle": "Soumission", "StarRating": "One", "Price": 50.1},
    "entry4": {"BookTitle": "Sharp Objects", "StarRating": "Four", "Price": 47.82},
    "entry5": {"BookTitle": "Sapiens: A Brief History of Humankind", "StarRating": "Five", "Price": 54.23},
    "entry6": {"BookTitle": "The Requiem Red", "StarRating": "One", "Price": 22.65}
}

# convert dict into a dataframe
df = pd.DataFrame.from_dict(data, orient="index")

# Clear the worksheet
current_sheet.clear()

# Write and save the dataframe to worksheet
gspread_dataframe.set_with_dataframe(current_sheet, df)

print("DataFrame successfully written to the Google Sheet")	

print(" ")
print("=================Retrieving the all records from WorkSheet==================")

# Getting the all records from worksheet			
print(current_sheet.get_all_records())		
			
			
			