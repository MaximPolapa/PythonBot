import gspread

from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    "https://www.googleapis.com/auth/cloud-platform",
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("D:\\myproject\\Python\\tgbot\\pybot-387910-1661a17b56b4.json", scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("Gumanitarka")
sheet = workbook.sheet1



#rowCount = len(sheet.get_all_values)\
#sheet.append_row('tkmhk','A5')

massive = sheet.get_all_values()
print(massive)







