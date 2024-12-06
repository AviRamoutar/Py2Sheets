import gspread
from oauth2client.service_account import ServiceAccountCredentials

#print("Hello World")

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

#Warframe reference
credits = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\Avi\IdeaProjects\untitled\Definetly-Not-a-Key.json",scope)

client = gspread.authorize(credits)


sheet = client.open('TEST').sheet1