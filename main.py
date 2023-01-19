from datetime import date
import telebot
from telebot import types
import gspread
from keys import my_token, my_googlesheet_id, path_to_file

bot_token = my_token
googlesheet_id = my_googlesheet_id
bot = telebot.TeleBot(bot_token)
gc = gspread.service_account(filename=path_to_file)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Введите расход через дефис в виде [КАТЕГОРИЯ-ЦЕНА]")

@bot.message_handler(commands=['month'])
def send_month(message):
    button_months = types.InlineKeyboardMarkup(row_width=4)
    Dec = types.InlineKeyboardButton(text='December', callback_data='Dec')
    Sep = types.InlineKeyboardButton(text='September', callback_data='Sep')
    Mar = types.InlineKeyboardButton(text='March', callback_data='Mar')
    Apr = types.InlineKeyboardButton(text='April', callback_data='Apr')
    Jan = types.InlineKeyboardButton(text='January', callback_data='Jan')
    May = types.InlineKeyboardButton(text='May', callback_data='May')
    Jun = types.InlineKeyboardButton(text='June', callback_data='Jun')
    Jul = types.InlineKeyboardButton(text='July', callback_data='Jul')
    Aug = types.InlineKeyboardButton(text='August', callback_data='Aug')
    Feb = types.InlineKeyboardButton(text='February', callback_data='Feb')
    Oct = types.InlineKeyboardButton(text='October', callback_data='Oct')
    Nov = types.InlineKeyboardButton(text='November', callback_data='Nov')
    button_months.add(Dec, Mar, Jun, Sep, Jan, Apr, Jul, Oct, Feb, May, Aug, Nov)
    bot.send_message(message.chat.id, 'Выберите месяц', reply_markup=button_months)

@bot.callback_query_handler(func=lambda call: call.data=='Jan' or call.data=='Feb' or call.data=='Mar' or call.data=='Apr' or call.data=='May' or call.data=='Jun' or call.data=='Jul' or call.data=='Aug' or call.data=='Sep' or call.data=='Oct' or call.data=='Nov' or call.data=='Dec')
def callback_query_month(call):
    if call.data == 'Jan':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Январь :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('J6'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('J15'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('J25'))
    elif call.data =='Feb':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Февраль :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('J8'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('J17'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('J27'))
    elif call.data == 'Mar':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Март :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('K4'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('K13'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('K23'))
    elif call.data == 'Apr':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Апрель :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('K6'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('K15'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('K25'))
    elif call.data == 'May':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Май :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('K8'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('K17'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('K27'))
    elif call.data == 'Jun':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Июнь :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('H4'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('H13'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('H23'))
    elif call.data == 'Jul':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Июль :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('H6'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('H15'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('H25'))
    elif call.data == 'Aug':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Август :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('H8'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('H17'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('H27'))
    elif call.data == 'Sep':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Сентябрь :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('I4'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('I13'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('I23'))
    elif call.data == 'Oct':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Октябрь :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('I6'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('I15'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('I25'))
    elif call.data == 'Nov':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Ноябрь :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('I8'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('I17'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('I27'))
    elif call.data == 'Dec':
        sh = gc.open_by_key(googlesheet_id)
        bot.send_message(call.message.chat.id, "За Декабрь :")
        bot.send_message(call.message.chat.id, "RUB")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('J4'))
        bot.send_message(call.message.chat.id, "USD")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('J13'))
        bot.send_message(call.message.chat.id, "EUR")
        bot.send_message(call.message.chat.id, sh.worksheet('Sheet2').get('J23'))

@bot.message_handler(commands=['summ'])
def send_summ(message):
    sh = gc.open_by_key(googlesheet_id)
    bot.send_message(message.chat.id, "RUB")
    bot.send_message(message.chat.id, sh.worksheet('Sheet2').get('G2'))
    bot.send_message(message.chat.id, "USD")
    bot.send_message(message.chat.id, sh.worksheet('Sheet2').get('G11'))
    bot.send_message(message.chat.id, "EUR")
    bot.send_message(message.chat.id, sh.worksheet('Sheet2').get('G21'))

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        today = date.today().strftime("%d.%m.%Y")
        category, price = message.text.title().split("-", 1)
        price = float(price)
        text_message = f'На {today} в таблицу расходов добавлена запись: категория {category}, сумма {price}'
        bot.send_message(message.chat.id, text_message)

        button_currency = types.InlineKeyboardMarkup()
        RUB = types.InlineKeyboardButton(text='RUB', callback_data='RUB')
        USD = types.InlineKeyboardButton(text='USD', callback_data='USD')
        EUR = types.InlineKeyboardButton(text='EUR', callback_data='EUR')
        button_currency.add(RUB, USD, EUR)
        bot.send_message(message.chat.id, 'Ваша валюта', reply_markup=button_currency)

        global trans
        trans = []
        trans.clear()
        trans.append(today)
        trans.append(category)
        trans.append(price)
    except:
        bot.send_message(message.chat.id, 'ОШИБКА! Неправильный формат данных!')

@bot.callback_query_handler(func=lambda call: call.data == 'RUB' or call.data == 'USD' or call.data == 'EUR')
def callback_query_currency(call):
    if call.data == 'RUB':
        currency = 'RUB'
        bot.send_message(call.message.chat.id, 'RUB')
    elif call.data == 'USD':
        currency = 'USD'
        bot.send_message(call.message.chat.id, 'USD')
    elif call.data == 'EUR':
        currency = 'EUR'
        bot.send_message(call.message.chat.id, 'EUR')
    trans.append(currency)

    button_payment = types.InlineKeyboardMarkup()
    cash = types.InlineKeyboardButton(text='Наличка', callback_data='cash')
    card = types.InlineKeyboardButton(text='Карта', callback_data='card')
    button_payment.add(cash, card)
    bot.send_message(call.message.chat.id, 'Способ оплаты', reply_markup=button_payment)

@bot.callback_query_handler(func=lambda call: call.data == 'cash' or call.data == 'card')
def callback_query_payment(call):
    if call.data == 'cash':
        payment = 'Наличка'
        bot.send_message(call.message.chat.id, 'Наличка')
    elif call.data == 'card':
        payment = 'Карта'
        bot.send_message(call.message.chat.id, 'Карта')
    trans.append(payment)

    sh = gc.open_by_key(googlesheet_id)
    sh.sheet1.append_row(trans)

if __name__ == '__main__':
    bot.polling(none_stop=True)