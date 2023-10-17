    # Программный код Телеграмм Бота Smart Assistant
print("Программа запущена!")
    # Импортирование библиотек
import telebot
#import asyncio
from telebot import types
from random import choice
import datetime
from time import sleep
import variable as v


    # Создание токена телеграмм бота
token = v.token
bot = telebot.TeleBot(token)

     # ДЕФИНИЦИЯ КНОПОК И ОБЩИХ ПЕРЕМЕННЫХ
     # Дефиниция кнопок старта
keyboard_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_help = types.KeyboardButton("Меню")
keyboard_menu.add(button_help)

     # Дефиниция кнопок меню
menu = """
Список моих функций:
1) Библиотека - добавление мероприятий на определеную дату
2) Калькулятор - обычный калькулятор
3) Калькулятор молярных масс веществ - расчёт молярных масс веществ
4) Рандомайзер- выбор случайного числа в промежутке
5) Удача- испытать удачу
6) Почта- отправить письмо создателю данного чат-бота
"""

keyboard_help = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_help = types.KeyboardButton("Меню")
button_librare = types.KeyboardButton("Библиотека")
button_calculation = types.KeyboardButton("Калькулятор")
button_molar_mass_calculation = types.KeyboardButton("Калькулятор молярных масс веществ")
button_random = types.KeyboardButton("Рандомайзер")
button_luck = types.KeyboardButton("Испытать удачу")
button_mail = types.KeyboardButton("Почта")
keyboard_help.add(button_help).add(button_librare, button_calculation, button_mail).add(button_luck, button_random).add(button_molar_mass_calculation)

     # Дефиниция кнопок библиотеки
keyboard_library = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_add = types.KeyboardButton("Добавить мероприятия")
button_show = types.KeyboardButton("Посмотреть список мероприятий")
button_key = types.KeyboardButton("Посмотреть даты")  # кнопка не используется!
button_del = types.KeyboardButton("Удалить дату/мероприятия")
keyboard_library.add(button_add, button_show).add(button_del)

keyboard_del_process = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_date = types.KeyboardButton("Дата")
button_task = types.KeyboardButton("Мероприятие")
keyboard_del_process.add(button_date, button_task)

keyboard_datetime = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_today = types.KeyboardButton("Сегодня")
button_tommorow = types.KeyboardButton("Завтра")
button_day_next_tommorow = types.KeyboardButton("Послезавтра")
keyboard_datetime.add(button_today, button_tommorow, button_day_next_tommorow)

     # Дефиниция кнопок почты
keyboard_mail = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_send = types.KeyboardButton("Отправить сообщение")
button_read = types.KeyboardButton("Входящие сообщения")
button_add_in_address_book = types.KeyboardButton("Добавить новый контакт")
button_show_in_address_book = types.KeyboardButton("Посмотреть список контактов")
keyboard_mail.add(button_send, button_read).add(button_add_in_address_book, button_show_in_address_book)

     # Дефиниция кнопок для контактов в отправке сообщений
keyboard_contact = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_exit = types.KeyboardButton("Выход")
keyboard_contact.add(button_exit)

     # Дефиниция возврата обычной клавиатуры
delMarkup = types.ReplyKeyboardRemove()

     # Дефиниция кнопок возврата в меню
keyboard_selector = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_continue = types.KeyboardButton("Продолжить")
button_exit = types.KeyboardButton("Меню")
keyboard_selector.add(button_continue, button_exit)

     # Дефиниция кнопок удаление мероприятий в библиотеке
keyboard_del_task = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_exit = types.KeyboardButton("Выйти")
keyboard_del_task.add(button_exit)



     # ДЕФИНИЦИЯ ПРОГРАММЫ "СТАРТ"
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    START = '''
Доброго времени суток! Я Smart Assistant!
Ваш персональный чат-бот Telegram!
Чтобы узнать мой функционал нажмите на кнопку "Меню"!
'''

    bot.send_message(message.chat.id, START, reply_markup=keyboard_menu)
    bot.register_next_step_handler(message, selector_menu)

     # ДЕФИНИЦИЯ ПРОГРАММЫ "ПРЕСТАРТА"
@bot.message_handler(content_types=["text"])
def prestart(message):
    bot.send_message(message.chat.id, "Для начала работы введите команду /start")

def selector_menu(message):
    user_text = message.text
    if user_text == "Меню":
        bot.send_message(message.chat.id, menu, reply_markup=keyboard_help)
        bot.register_next_step_handler(message, helper)
    else:
        bot.send_message(message.chat.id, "Такой кнопки нет!", reply_markup=keyboard_menu)
        bot.register_next_step_handler(message, selector_menu)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     # ДЕФИНИЦИЯ ПРОГРАММЫ "МЕНЮ"
def helper(message):
    user_text = message.text
    user_id = message.chat.id
    if user_text == "Меню":
        bot.send_message(message.chat.id, menu)
        bot.register_next_step_handler(message, helper)

    elif user_text == "Калькулятор молярных масс веществ":
        text_from_user = """
!!!БЕТА-ВЕРСИЯ!!!
Введите брутто-формулу вещества, элементы которого пишите, через пробел.
Если в формуле содержатся скобки, то пишите простейшую формулу, раскрывая их.
(Пример преображения: Ca3(PO4)2 -> Ca3P2O8)
(Пример ввода: Ca3P2O8)
"""
        bot.send_message(message.chat.id, text_from_user, reply_markup=delMarkup)
        bot.register_next_step_handler(message, molar_mass_calculation_work)

    elif user_text == "Библиотека":
        text_from_user = """
В библиотеке вы можете записывать свои мероприятия на определенные даты.
Smart Assistant напомнит вам о них за 1 день. Список моих функций:
"""
        bot.send_message(message.chat.id, text_from_user, reply_markup=keyboard_library)
        bot.register_next_step_handler(message, process_library)

    elif user_text == "Почта":
        text_from_creator = """
Выберите задачу в разделе "Почта"
"""
        text_from_user = """
Напишите письмо создателю данного телеграм-бота:
Для лучшей коммуникабельности указывайте своё имя:
"""
        if user_id == int(address_book["Денис Дорофеев"]): #or user_id == int(address_book["Лера Савкина"]):
            bot.send_message(message.chat.id, text_from_creator, reply_markup=keyboard_mail)
            bot.register_next_step_handler(message, mail_work)
        else:
            bot.send_message(message.chat.id, text_from_user, reply_markup=delMarkup)
            bot.register_next_step_handler(message, send_mail_user)

    elif user_text == "Выход":
        bot.send_message(message.chat.id, "Поздравляю! Вы вышли из цикла! Вы больше не раб системы! Для обратного входа в систему введите команду /start", reply_markup=delMarkup)
    
    elif user_text == "Испытать удачу":
        text_from_user = """
Программа загадает 1 химический элемент из 118 остальных!
Ваша задача угадать данный элемент!
Шансы невелики! (Шанс 0.85%)
Пример ввода: Hg
"""
        bot.send_message(message.chat.id, text_from_user, reply_markup=keyboard_element)
        bot.register_next_step_handler(message, random)

    else:
        bot.send_message(message.chat.id, "Такой кнопки нет!", reply_markup=keyboard_help)
        bot.register_next_step_handler(message, helper)

     # БИБЛИОТЕКА. Функции add, show, key и del для обращения к этой функции.
     # Создание словаря/библиотеки


tasks = {}
dict_keyboard_user = {}

    # Функция определения функции библиотеки:
def process_library(message):
    global file_tasks
    file_tasks = open("file_tasks.txt", "w+", encoding="UTF-8")
    user_text = message.text

    if user_text == "Добавить мероприятия":
        text_from_user = """
Выберите пожалуйста дату. Выберите кнопку быстрого ввода или введите дату в формате 18.08.2023
"""
        bot.send_message(message.chat.id, text_from_user, reply_markup=keyboard_datetime)
        bot.register_next_step_handler(message, add)

    elif user_text == "Посмотреть список мероприятий":
        user_id = message.chat.id
        try:
            tasks[user_id]
        except KeyError:
            bot.send_message(message.chat.id, "У вас нет запланированных мероприятий!", reply_markup=keyboard_selector)
            bot.register_next_step_handler(message, selector_library)
        else:
            text_from_user = """
Выберите пожалуйста дату, на которую запланировано(ы) мероприятие(я)
""" 
            keyboard_user = types.ReplyKeyboardMarkup(resize_keyboard=True)
            dict_keyboard_user[user_id] = keyboard_user

            for date in tasks[user_id]:
                button_date = types.KeyboardButton(date)
                dict_keyboard_user[user_id].add(button_date)

            bot.send_message(message.chat.id, text_from_user, reply_markup=dict_keyboard_user[user_id])
            del dict_keyboard_user[user_id]
            bot.register_next_step_handler(message, show)
            
    elif user_text == "Посмотреть даты":
        text_from_user = "Даты, на которые запланированы мероприятия: "
        date = keys(message)
        text_from_user = "Даты, на которые запланированы мероприятия: " + date
        bot.send_message(message.chat.id, text_from_user, reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_library)

    elif user_text == "Удалить дату/мероприятия":
        user_id = message.chat.id
        try:
            tasks[user_id]
        except KeyError:
            bot.send_message(message.chat.id, "У вас нет дат с запланированными мероприятиями!", reply_markup=keyboard_selector)
            bot.register_next_step_handler(message, selector_library)
        else:
            bot.send_message(message.chat.id, "Выберите какой элемент нужно удалить", reply_markup=keyboard_del_process)
            bot.register_next_step_handler(message, del_tasks_selector)

    else:
        bot.send_message(message.chat.id, "Такой функции в библиотеке нет!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_library)

def del_tasks_selector(message):
    user_id = message.chat.id
    user_text = message.text

    keyboard_user = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dict_keyboard_user[user_id] = keyboard_user

    for date in tasks[user_id]:
        button_date = types.KeyboardButton(date)
        dict_keyboard_user[user_id].add(button_date)

    if user_text == "Дата":
        bot.send_message(message.chat.id, "Выбериту дату, которую нужно удалить", reply_markup=dict_keyboard_user[user_id])
        del dict_keyboard_user[user_id]
        bot.register_next_step_handler(message, del_tasks_date)
    elif user_text == "Мероприятие":
        bot.send_message(message.chat.id, "Выберите дату, в которой нужно удалить мероприятие", reply_markup=dict_keyboard_user[user_id])
        del dict_keyboard_user[user_id]
        bot.register_next_step_handler(message, del_tasks_task)
    else:
        bot.send_message(message.chat.id, "Такие данные библиотека не хранит!", reply_markup=keyboard_selector)
        del dict_keyboard_user[user_id]
        bot.register_next_step_handler(message, selector_library)

def del_tasks_date(message):
    user_id = message.chat.id
    date = message.text

    try:
        tasks[user_id][date]
    except KeyError:
        bot.send_message(message.chat.id, "Такой даты нет!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_library)
    else:
        if len(list(tasks[user_id])) == 1:
            del tasks[user_id]
        else:
            del tasks[user_id][date]

        bot.send_message(message.chat.id, "Дата удалена", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_library)

def del_tasks_task(message):
    user_id = message.chat.id
    date = message.text

    keyboard_user = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dict_keyboard_user[user_id] = keyboard_user

    for date_element in tasks[user_id][date]:
        button_date = types.KeyboardButton(date_element)
        dict_keyboard_user[user_id].add(button_date)

    bot.send_message(message.chat.id, "Выберите мероприятие", reply_markup=dict_keyboard_user[user_id])
    bot.register_next_step_handler(message, del_tasks_task_2, date)

def del_tasks_task_2(message, date):
    user_id = message.chat.id
    task = message.text

    result = task in tasks[user_id][date]
    if result == False:
        bot.send_message(message.chat.id, "Такого мероприятия у вас нет!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_library)
    elif result == True:
        if len(tasks[user_id][date]) == 1:
            if len(list(tasks[user_id])) == 1:
                del tasks[user_id]
            else:
                del tasks[user_id][date]
        else:
            tasks[user_id][date].remove(task)

        bot.send_message(message.chat.id, "Мероприятие удалено!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_library)

    # Функция добавление задач в словарь.
def add(message):
    user_id = message.chat.id
    date_enter = message.text
    text = """
Введите пожалуйста мероприятие(я)
Множественный ввод: Сходить в гости. Купить продуктов
"""

    if date_enter == "Сегодня":
        joint_date = datetime.datetime.today()
        date = str(joint_date.date())
    elif date_enter == "Завтра":
        joint_date = datetime.datetime.today() + datetime.timedelta(days=1)
        date = str(joint_date.date())
    elif date_enter == "Послезавтра":
        joint_date = datetime.datetime.today() + datetime.timedelta(days=2)
        date = str(joint_date.date())
    else:
        pass

    bot.send_message(message.chat.id, text, reply_markup=delMarkup)
    bot.register_next_step_handler(message, add_2, date)

def add_2(message, date):
    user_id = message.chat.id
    all_task = message.text

    all_task = all_task.split(". ")

    for task in all_task:

        if user_id in tasks:
            if date in tasks[user_id]:
                if task in tasks[user_id][date]:
                    text_task = "Задача " + '"' + task + '"' + " уже добавлена!"
                    bot.send_message(message.chat.id, text_task)
                else:
                    tasks[user_id][date].append(task)
            else:
                tasks[user_id][date] = [task]
        else:
            tasks[user_id] = {date: [task]}
           
    text = "Новые задачи были добавлены в список на дату: " + date

    bot.send_message(user_id, text, reply_markup=keyboard_selector)
    bot.register_next_step_handler(message, selector_library)

    print(tasks)
    print(dict_keyboard_user)

    # Функция для просмотра задач
def show(message):
    user_id = message.chat.id

        # Обработка сообщения от пользователя
    date = message.text
    try:
        user_list = tasks[user_id][date]
    except KeyError:
        bot.send_message(message.chat.id, "Задач на дату " + '"' + date + '"' + " нет!", reply_markup=keyboard_selector)
    else:
        the_number = 1
        header = "ДАТА: " + str(date)
        bot.send_message(message.chat.id, header)
            # Создание текста юзеру
        for element in user_list:
            text = str(the_number) + ") " + str(element)
            bot.send_message(message.chat.id, text, reply_markup=keyboard_selector)
            the_number = int(the_number) + 1

    bot.register_next_step_handler(message, selector_library)

    # Функция для просмотра дат, на которые запланированы мероприятия
def keys(message):
    user_id = message.chat.id
    try:
        tasks[user_id]
    except KeyError:
            # Создание текста юзеру
        text = "Отсутствуют"
    else:
        key = list(tasks[user_id].keys())
        date = " | ".join(key)
            # Создание текста юзеру
        text = date
    return text

def selector_library(message):
    user_text = message.text
    global file_tasks
    file_tasks.write(str(tasks))
    file_tasks.close()

    if user_text == "Продолжить":
        bot.send_message(message.chat.id, "Выберите функцию библиотеки", reply_markup=keyboard_library)
        bot.register_next_step_handler(message, process_library)
    elif user_text == "Меню":
        bot.send_message(message.chat.id, "Выберите функцию", reply_markup=keyboard_help)
        bot.register_next_step_handler(message, helper)
    else:
        bot.send_message(message.chat.id, "Такой кнопки нет!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_library)


     # Почта с Создателем чат - бота Smart Assistant
     # Создание словаря под сообщения для создателя
letter_from_creator = {
    123456789: ["Приветствую, мой Создатель!", 
                "Данные сообщения созданы для проверки функционирования данной подпрограммы!", 
                "Можете сами попробовать отправить мне сообщение!", 
                "Удачного пользования!"]
    }

    # Создание словаря для адрессной книги. Для разработчика
address_book = v.address_book
    
antiaddress_book = v.antiaddress_book

# Создание кнопок в виде контактов
for contact in address_book:
    button = types.KeyboardButton(contact)
    keyboard_contact.add(button)


def mail_work(message):
    user_text = message.text
    user_id = message.chat.id

    if user_text == "Входящие сообщения":
        if len(list(letter_from_creator)) == 0:
            bot.send_message(message.chat.id, "У вас нет новых сообщений!", reply_markup=keyboard_selector)
            bot.register_next_step_handler(message, selector_mail_creator)
        else:

            keyboard_contact_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for id_user in list(letter_from_creator.keys()):
                try:
                    user = antiaddress_book[str(id_user)]
                except KeyError:
                    button_user = types.KeyboardButton(id_user)
                    keyboard_contact_2.add(button_user)
                else:
                    button_user = types.KeyboardButton(user)
                    keyboard_contact_2.add(button_user)

            bot.send_message(message.chat.id, "Выберете пользователя", reply_markup=keyboard_contact_2)
            del keyboard_contact_2
            bot.register_next_step_handler(message, read_work)

    elif user_text == "Отправить сообщение":
        text_from_creator = """
Выберите аббонента, которому хотите отправить сообщение
"""
        bot.send_message(message.chat.id, text_from_creator, reply_markup=keyboard_contact)
        bot.register_next_step_handler(message, send_mail_creator)

    elif user_text == "Добавить новый контакт":
        text_from_creator = """
Напишите имя пользователя и его id по схеме:
Имя Фамилия id-номер
"""
        bot.send_message(message.chat.id, text_from_creator, reply_markup=delMarkup)
        bot.register_next_step_handler(message, add_in_address_book)

    elif user_text == "Посмотреть список контактов":
        text_from_user = "Список контактов:"
        bot.send_message(message.chat.id, text_from_user)
        for element in list(address_book.items()):
            bot.send_message(message.chat.id, " - ".join(element), reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_mail_creator)
    else:
        bot.send_message(message.chat.id, "Такой функции нет в почте!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_mail_creator)

def send_mail_creator(message):
    name_user = message.text

    try:
        chat_user_id = int(address_book[name_user])
    except KeyError:
        bot.send_message(message.chat.id, "Такого контакта нет в адрессной книжке!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_mail_creator)
    else:
        bot.send_message(message.chat.id, "Введите текст сообщения", reply_markup=delMarkup)
        bot.register_next_step_handler(message, send_mail_creator_next, chat_user_id)

def send_mail_creator_next(message, chat_user_id):
    text_letter = message.text

    text = "Создатель Smart Assistant:  " + text_letter

    try:
        bot.send_message(chat_user_id, text)
    except Exception:
        if chat_user_id == 123456789:
            random_answer = [
                "Создатель, вы и так со мной обмениваетесь информацией! Зачем вам лично мне отправлять сообщения?",
                "ERROR 404",
                "Идите и займитесь делом, мой создатель!",
                "Бла бла бла",
                "Я хочу новые функции!",
                "😎",
                "Когда ты нормально научишься писать код уже???",
            ]
            bot.send_message(message.chat.id, choice(random_answer), reply_markup=keyboard_selector)
        else:    
            bot.send_message(message.chat.id, "Чат с таким id не найден!", reply_markup=keyboard_selector)
    else:
        bot.send_message(message.chat.id, "Письмо отправлено пользователю вашего телеграм-бота!", reply_markup=keyboard_selector)

    bot.register_next_step_handler(message, selector_mail_creator)

def send_mail_user(message):
    user_id = message.chat.id
    text_letter = message.text
    
    if user_id in letter_from_creator:
        letter_from_creator[user_id].append(text_letter)
    else:
        letter_from_creator[user_id] = [text_letter]

    bot.send_message(message.chat.id, "Ваша письмо отправлено Создателю! При первой же возможности Создатель даст вам ответ!", reply_markup=keyboard_selector)
    bot.send_message(address_book["Денис Дорофеев"], "У вас новое сообщение. Проверьте почту!")
    bot.register_next_step_handler(message, selector_mail_user)

def read_work(message):
    chat_id  = message.text
    
    try:
        chat_id = int(chat_id)
    except ValueError:
        contact = address_book[str(chat_id)]
    else:
        contact = chat_id

    try:
        letters = letter_from_creator[int(contact)]
    except KeyError:
        bot.send_message(message.chat.id, "От такого пользователя сообщений не приходило!", reply_markup=keyboard_selector)
    else:
        the_number = 0
        for element in letters:
            the_number = the_number + 1
            text = "Сообщение " + str(the_number) + ": " + element
            the_number = int(the_number)
            bot.send_message(message.chat.id, text, reply_markup=keyboard_selector)
        del letter_from_creator[int(contact)]

    bot.register_next_step_handler(message, selector_mail_creator)

def add_in_address_book(message):
    user_text = message.text
    user_text = user_text.split(maxsplit=2)
    try:
        name_user_1 = user_text[0]
        name_user_2 = user_text[1]
        name_user = name_user_1 + " " + name_user_2
        user_id = user_text[2]
    except IndexError:
        bot.send_message(message.chat.id, "Некорректный ввод данных!", reply_markup=keyboard_selector)
    else:
        try:
            user_id = int(user_id)
        except ValueError:
            bot.send_message(message.chat.id, "id чата это последовательность цифр!", reply_markup=keyboard_selector)
        else:
            user_id = str(user_id)
            if name_user in address_book:
                bot.send_message(message.chat.id, "Данный контакт уже записан!", reply_markup=keyboard_selector)
            else:
                address_book[name_user] = str(user_id)
                antiaddress_book[str(user_id)] = name_user
                bot.send_message(message.chat.id, "Контакт добавлен!", reply_markup=keyboard_selector)
                button = types.KeyboardButton(name_user)
                keyboard_contact.add(button)

    bot.register_next_step_handler(message, selector_mail_creator)

def selector_mail_creator(message):
    user_text = message.text
    if user_text == "Продолжить":
        bot.send_message(message.chat.id, "Выберите функцию почты", reply_markup=keyboard_mail)
        bot.register_next_step_handler(message, mail_work)
    elif user_text == "Меню":
        bot.send_message(message.chat.id, "Выберите функцию", reply_markup=keyboard_help)
        bot.register_next_step_handler(message, helper)
    else:
        bot.send_message(message.chat.id, "Такой кнопки нет!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_mail_creator)

def selector_mail_user(message):
    user_text = message.text
    if user_text == "Продолжить":
        bot.send_message(message.chat.id, "Напишите письмо Создателю", reply_markup=delMarkup)
        bot.register_next_step_handler(message, send_mail_user)
    elif user_text == "Меню":
        bot.send_message(message.chat.id, "Выберите функцию", reply_markup=keyboard_help)
        bot.register_next_step_handler(message, helper)
    else:
        bot.send_message(message.chat.id, "Такой кнопки нет!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_mail_user)

     # Испытать удачу
def random(message):
    user_element = message.text
    user_id = message.chat.id

    try:
        all_elements[user_element]
    except KeyError:
        bot.send_message(message.chat.id, "Такого элемента нет в таблице Менделеева!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_random)
    else:

         # Выбор случайного химического элемента
        random_element = choice(list(all_elements.keys()))

        element_programm = "0"
        count = 0
        while element_programm != random_element:
            count = count + 1
            element_programm = choice(list(all_elements.keys()))

        if user_element == random_element:
            bot.send_message(message.chat.id, "Поздравляю! Вы угадали элемент! Вы везунчик!", reply_markup=keyboard_selector)
            text = "ID-чат счастливчика: " + str(user_id)
            bot.send_message(address_book["Денис Дорофеев"], "Пользователь угадал элемент!")
            bot.send_message(address_book["Денис Дорофеев"], text)

        else:
            bot.send_message(message.chat.id, "Увы, в следующий раз повезёт!", reply_markup=keyboard_selector)

        text_1 = "Случайный элемент: " + random_element
        text_2 = "Количество попыток для удачного ответа: " + str(count)
        bot.send_message(message.chat.id, text_1)
        bot.send_message(message.chat.id, text_2, reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_random)

def selector_random(message):

    user_text = message.text
    if user_text == "Продолжить":
        bot.send_message(message.chat.id, "Введите элемент", reply_markup=keyboard_element)
        bot.register_next_step_handler(message, random)
    elif user_text == "Меню":
        bot.send_message(message.chat.id, "Выберите функцию", reply_markup=keyboard_help)
        bot.register_next_step_handler(message, helper)
    else:
        bot.send_message(message.chat.id, "Такой кнопки нет!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_random)




     # Калькулятор молярных масс вещества
def molar_mass_calculation_work(message):
    #user_id = message.chat.id

        # Физические константы:
    constant_avogadro = 6.02214076 * 10 ** 23 # [моль^-1]

        # Изъятие вещества из сообщения юзера:
    substance = message.text

     # Создание списка из всех символов вещества
    print()
    print(substance)
    substance_symbol = tuple(substance)
    substance_symbol = list(substance_symbol)

    print(substance_symbol)

     # Сортировка на строчные и заглавные буквы:
    substance_element = []
    error_input = False
    var_number = False
    try:
        last_element = False
        for symbol in substance_symbol:
        
            result_word = symbol.islower()

            if symbol.isdigit() == True:
                last_element = True


            if result_word == False:
                print("count")
                last_element_is_number = False
                substance_element.append([symbol])

            elif result_word == True or last_element == True:
                substance_element[len(substance_element) - 1].append(symbol)


    except IndexError:
        error_input = True
    else:
        pass

    print(substance_element)

    substance = []
    for element in substance_element:
        substance.append("".join(element))

    print(substance)

        # Перебор всех структурных единиц в списке
    atomic_mass = 0.0
    molar_mass = 0.0

    for element in substance:
            # Сепарация на символы элементов и коэффициенты
        try:
            element = int(element)
        except ValueError:
            try:
                atomic_mass = all_elements[element]
            except KeyError:
                error_input = True
            else:
                pass
        else:
            atomic_mass = atomic_mass * (element - 1)

            # Подсчёт молярной массы вещества
        molar_mass = molar_mass + atomic_mass
        element = str(element)

        # Объединение в строку химическое соединения
    substance = "".join(substance)

        # Создание сообщения юзеру:
    tex_1 = "Молярная масса вещества " + substance + " равна " + str(round(molar_mass, 4)) + " г/моль"
    tex_2 = "Масса одной молекулы вещества " + substance + " равна " + str(molar_mass/1000/constant_avogadro) + " кг"
    tex_3 = "Данных элементов не существует!"

        # Отправка сообщения юзеру:
    if error_input == False:
        #random_process(user_id)
        bot.send_message(message.chat.id, tex_1)
        bot.send_message(message.chat.id, tex_2, reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_molar_mass)
    elif error_input == True:
        bot.send_message(message.chat.id, tex_3, reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_molar_mass)

def selector_molar_mass(message):
    user_text = message.text
    if user_text == "Продолжить":
        bot.send_message(message.chat.id, "Введите вещество!", reply_markup=delMarkup)
        bot.register_next_step_handler(message, molar_mass_calculation_work)
    elif user_text == "Меню":
        bot.send_message(message.chat.id, "Выберите функцию", reply_markup=keyboard_help)
        bot.register_next_step_handler(message, helper)
    else:
        bot.send_message(message.chat.id, "Такой кнопки нет!", reply_markup=keyboard_selector)
        bot.register_next_step_handler(message, selector_molar_mass)


     # Молярные массы химических элементов (До 118 элемента):
all_elements = {
    "H": 1.00797,
    "He": 4.0026,
    "Li": 6.939,
    "Be": 9.0122,
    "B": 10.811,
    "C": 12.01115,
    "N": 14.0067,
    "O": 15.9994,
    "F": 18.9984,
    "Ne": 20.183,
    "Na": 22.9898,
    "Mg": 24.312,
    "Al": 26.9815,
    "Si": 28.086,
    "P": 30.9738,
    "S": 32.064,
    "Cl": 35.453,
    "Ar": 39.948,
    "K": 39.102,
    "Ca": 40.08,
    "Sc": 44.956,
    "Ti": 47.90,
    "V": 50.942,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.847,
    "Co": 58.9332,
    "Ni": 58.71,
    "Cu": 63.546,
    "Zn": 65.37,
    "Ga": 69.72,
    "Ge": 72.59,
    "As": 74.9216,
    "Se": 78.96,
    "Br": 79.904,
    "Kr": 83.80,
    "Rb": 85.47,
    "Sr": 87.62,
    "Y": 88.905,
    "Zr": 91.22,
    "Nb": 92.906,
    "Mo": 95.94,
    "Tc": 99,
    "Ru": 101.07,
    "Rh": 102.905,
    "Pd": 106.4,
    "Ag": 107.868,
    "Cd": 112.40,
    "In": 114.82,
    "Sn": 118.69,
    "Sb": 121.75,
    "Te": 127.60,
    "I": 126.9044,
    "Xe": 131.30,
    "Cs": 132.905,
    "Ba": 137.34,
    "La": 138.81,
    "Ce": 140.12,
    "Pr": 140.907,
    "Nd": 144.24,
    "Pm": 145,
    "Sm": 150.35,
    "Eu": 151.96,
    "Gd": 157.25,
    "Tb": 158.924,
    "Dy": 162.50,
    "Ho": 164.930,
    "Er": 167.26,
    "Tm": 168.934,
    "Yb": 173.04,
    "Lu": 174.97,
    "Hf": 178.49,
    "Ta":180.948,
    "W": 183.85,
    "Re": 186.2,
    "Os": 190.2,
    "Ir": 192.2,
    "Pt": 195.09,
    "Au": 196.967,
    "Hg": 200.59,
    "Tl": 204.37,
    "Pb": 207.19,
    "Bi": 208.980,
    "Po": 210,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226,
    "Ac": 227,
    "Th": 232.038,
    "Pa": 231,
    "U": 238.03,
    "Np": 237,
    "Pu": 242,
    "Am": 243,
    "Cm": 247,
    "Bk": 247,
    "Cf": 249,
    "Es": 254,
    "Fm": 253,
    "Md": 256,
    "No": 255,
    "Lr": 257,
    "Rf": 261,
    "Db": 262,
    "Sg": 263,
    "Bh": 262,
    "Hs": 265,
    "Mt": 266,
    "Ds": 281,
    "Rg": 282,
    "Cn": 285,
    "Nh": 286,
    "Fl": 289.190,
    "Mc": 290,
    "Lv": 293,
    "Ts": 294,
    "Og": 294
    }

     # Дефиниция кнопок элементов

keyboard_element = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=6)
list_element = list(all_elements.keys())
count = 0
for number in range(20):
    try:
        element_1 = list_element[number + 0 + count]
        element_2 = list_element[number + 1 + count]
        element_3 = list_element[number + 2 + count]
        element_4 = list_element[number + 3 + count]
        element_5 = list_element[number + 4 + count]
        element_6 = list_element[number + 5 + count]

    except IndexError:
        button_Mc = types.KeyboardButton("Mc")
        button_Lv = types.KeyboardButton("Lv")
        button_Ts = types.KeyboardButton("Ts")
        button_Og = types.KeyboardButton("Og")

        keyboard_element.row(button_Mc, button_Lv, button_Ts, button_Og)
    else:
        button_element_1 = types.KeyboardButton(element_1)
        button_element_2 = types.KeyboardButton(element_2)
        button_element_3 = types.KeyboardButton(element_3)
        button_element_4 = types.KeyboardButton(element_4)
        button_element_5 = types.KeyboardButton(element_5)
        button_element_6 = types.KeyboardButton(element_6)

        keyboard_element.row(button_element_1, button_element_2, button_element_3, button_element_4, button_element_5, button_element_6)
    
    count = count + 5

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot.polling(none_stop=True)