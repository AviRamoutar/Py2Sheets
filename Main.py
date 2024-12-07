import gspread
from google.oauth2.service_account import Credentials


def load_credentials_from_file(file_path):
    try:
        creds = Credentials.from_service_account_file(file_path, scopes=scope)
        return creds
    except Exception as e:
        raise ValueError(f"Failed to load credentials from {file_path}: {e}")


scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]


#CHANGE FILE PATH HERE!!!!!
credits = load_credentials_from_file(r"Your\File\Path\Here")
client = gspread.authorize(credits)

#Replace 'TEST' with Sheet name
sheet = client.open('TEST').sheet1


#Accesor Methods use within scope of sheet

print(sheet.get_all_records())
print(sheet.row_values(4))
print(sheet.col_values(3))
print(sheet.cell(3,3).value)

#Editor Methods
sheet.insert_row(["TestText",56,"Hello",True],5)
sheet.delete_rows(5)
#sheet.update_cell(3,1,"TEST")

"""
Finds first appreance of given text and stores it's value/location
"""
#search = sheet.find("TestText")
#print(search.value) returns "TestText"
#print(search.row)
#print(search.col)

