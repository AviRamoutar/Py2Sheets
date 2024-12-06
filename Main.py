import gspread
from google.oauth2.service_account import Credentials



#Just read the name dawg it aint complicated
def load_credentials_from_file(file_path):
    try:
        creds = Credentials.from_service_account_file(file_path, scopes=scope)
        return creds
    except Exception as e:
        raise ValueError(f"Failed to load credentials from {file_path}: {e}")


scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

#Warframe reference
#CHANGE FILE PATH HERE!!!!!
credits = load_credentials_from_file(r"Your\File\Path\Here")

client = gspread.authorize(credits)


sheet = client.open('TEST').sheet1

#Accesor Methods

#print(sheet.get_all_records())
#print(sheet.row_values(4))
#print(sheet.cell(3,3).value)