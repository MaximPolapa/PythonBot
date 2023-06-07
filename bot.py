import telebot 
import config
import gspread

from oauth2client.service_account import ServiceAccountCredentials
from telebot import types


bot = telebot.TeleBot('5911233509:AAHdzz3YdO8S3Q9iEYE-gEVjbGjzeioCIV8')
scopes = [
    "https://www.googleapis.com/auth/cloud-platform",
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("D:\\myproject\\Python\\tgbot\\pybot-387910-1661a17b56b4.json", scopes=scopes)
file = gspread.authorize(creds)
workbook = file.open("Gumanitarka")
sheet = workbook.sheet1



row = 2
column = 1
name = ''
last_name = ''
surname = ''
address = ''
baby = ''
phone = ''
message = ''
numberPeople = ''

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Привіт, для заповнення анкети введи /reg. Якщо виникнуть якісь питання пиши /help') #Change
    
@bot.message_handler(commands=['reg'])   
def welcome(pm):
    global id
    global column

    id = pm.chat.id
    sheet.update_cell(row,column,id)
    column += 1
    sent_msg = bot.send_message(pm.chat.id, "Ваше ім'я?") #Change
    bot.register_next_step_handler(sent_msg, name_handler)    

def name_handler(pm):
    global name
    global column

    name = pm.text
    sheet.update_cell(row,column,name)
    column += 1
    sent_msg = bot.send_message(pm.chat.id, f"Ваше прізвище?") #Change
    bot.register_next_step_handler(sent_msg, last_name_handler, name) 

def last_name_handler(pm,name):
    global last_name
    global column

    last_name = pm.text
    sheet.update_cell(row,column,last_name)
    column += 1
    sent_msg = bot.send_message(pm.chat.id, f"Ваше по батькові?") #Change
    bot.register_next_step_handler(sent_msg, surname_handler, last_name) 

def surname_handler(pm,last_name):
    global surname
    global column

    surname = pm.text
    sheet.update_cell(row,column,surname)
    column += 1
    sent_msg = bot.send_message(pm.chat.id, f"Напишіть свою адресу(Наприклад: м.Полтава вул Шевченка 4А)?") #Change
    bot.register_next_step_handler(sent_msg, address_handler, address) 


def address_handler(pm,surname):
    global address
    global column
    
    address = pm.text
    sheet.update_cell(row,column,address)
    column += 1
    sent_msg = bot.send_message(pm.chat.id, f"Чи є у вас діти(Напишіть так або ні)") #Change
    bot.register_next_step_handler(sent_msg, baby_handler, baby)

def baby_handler(pm,address):
    global baby
    global column
    
    
    baby = pm.text
    sheet.update_cell(row,column,baby)
    column += 1 
    sent_msg = bot.send_message(pm.chat.id, f"Введіть свій номер телефона:") #Change
    bot.register_next_step_handler(sent_msg, phone_handler, phone) 

def phone_handler(pm,baby):
    global phone
    global column
    global row
    
    phone = pm.text
    sheet.update_cell(row,column,phone)
    column = 1 
    row += 1 
    sent_msg = bot.send_message(pm.chat.id, f"Дякую за реєстрацію, чекайте, з вами зв'яжуться. Слава Україні") #change 


@bot.message_handler(commands=['messagepeople'])
def input_number(pm):
    sent_message = bot.send_message(pm.chat.id, "Введіть айдішки людей через , (Наприклад: 5678,3457834567,5678905678995)") #Change 
    bot.register_next_step_handler(sent_message,input_message,numberPeople)

def input_message(pm,number):
    global numberPeople

    numberPeople = pm.text
    sent_message = bot.send_message(pm.chat.id, "Введіть текст який хочете відправити:") #Поміняти текст 
    bot.register_next_step_handler(sent_message,message_handler,numberPeople)

    


def message_handler(pm,num):
    global message
    global numberPeople

    message = pm.text
    number = ''
    iterator = 0
    
    for i in numberPeople:
        if iterator == len(numberPeople)-1:
            number += i
            bot.send_message(number,message)
            iterator += 1
        if  i != ',':
            iterator += 1
            number += i
        if i == ',':
            iterator += 1
            bot.send_message(number,message)
            number = ''
        


#RUN
bot.polling()