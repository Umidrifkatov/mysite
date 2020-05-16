from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import telebot
from .services import *
from .constants import BUTTONS, user_step
from . import models


bot = telebot.TeleBot(settings.TOKEN, threaded=False)
try:
    # для webhook частично и получения обновлений от телеграм
    @csrf_exempt
    def worker(request):
        if request.META['CONTENT_TYPE'] == 'application/json':
            json_data = request.body.decode('utf-8')
            update = telebot.types.Update.de_json(json_data)
            bot.process_new_updates([update])
            return HttpResponse("")
        else:
            raise PermissionDenied


    # для перевода добавленного фото с админки 
    # в файл айди и сохранение таким образом
    # в базе данных   
    def tgfileid(pic):
        photo = bot.send_photo(121637541, pic)
        return photo.photo[-1].file_id


    # первое сообщение боту если пользователя нет в 
    # то пользователь получает сообщение о выборе языка
    @bot.message_handler(commands=['start'])
    def startmessage(message):
        start_message(message, bot)
        # bot.delete_message(message.chat.id, message.message_id - 1)
        
    @bot.message_handler(commands=['statistics'])
    def statmessage(message):
        bot.send_photo(message.from_user.id, 'AgACAgIAAxkDAAIasF6_k5b_4X4vV4N4nPiZ1PSwkr6eAAJFrjEbQvUAAUrI7Quhc3bTxKG0g5IuAAMBAAMCAAN5AANedAEAARkE')
        # bot.delete_message(message.chat.id, message.message_id - 1)




    # все сообщения у которых нет юсер степ
    # и не являются кнопками приходят сюда
    def unknown_message(message, bot):
        print('hi')


    # не особо нужно но пришлось
    def uncknown_callback(message, bot, z):
        pass



    # те сообщения что не попали в кнопки отправляются сюда для проверки состояния 
    # и если нет совпадений по состояниям отсылается стандартное сообщение 
    def all_text_messages_switcher(message, bot):
        switcher = {
            user_step['default']: main_interface,
            user_step['enter_lang']: enter_lang,
            user_step['chosetodel']: choose_todel,
            user_step['deliverortake']: deliverortake,
            user_step['get_day']: get_day,
            user_step['get_location']: get_location,
            user_step['get_phone']: get_phone,
            user_step['get_paymethod']: payment_method,
            user_step['changephone']: changephone,
            
            
            
        }
        func = switcher.get(models.TgUser.objects.get(userid = message.from_user.id).step, unknown_message)
        func(message, bot)



    # захватывает все сообщения и 1. проверяет на кнопки 2. проверяет на шаг пользователя (ввод)
    @bot.message_handler(content_types=['text', 'contact', 'location'])
    def buttons_answer(message):
        try:
            # print(message)
            user = models.TgUser.objects.get(userid = message.from_user.id)
            if user.lang == None:
                all_text_messages_switcher(message, bot)
            else:
                switcher = {
                    BUTTONS[user.lang]['menu']: main_menu,
                    BUTTONS[user.lang]['settings']: get_settings,
                    BUTTONS[user.lang]['about']: get_about,
                    BUTTONS[user.lang]['cart']: get_cart,
                    BUTTONS[user.lang]['back']: main_interface,
                    BUTTONS[user.lang]['clearcart']: clear_cart,
                    BUTTONS[user.lang]['createorder']: check_out,
                    BUTTONS[user.lang]['lang']: changelang,
                    BUTTONS[user.lang]['phone']: changephone,
                    BUTTONS[user.lang]['history']: get_history,
                    
                    
                    
                }
                func = switcher.get(message.text, all_text_messages_switcher)
                func(message, bot)
        except Exception:
            pass  # доделать для неизвестных сообщений
                # доделать для неизвестных пользователей
                # или общее
            
        



    # выхватывает все инлайн кнопки и проверяет части на совпадение
    # у коллбэка две части 1-куда направлять 2-название точки 
    @bot.callback_query_handler(func=lambda call: True)
    def call_message(message):
        parts = message.data.split(' ', 1)
        part1 = parts[0]
        part2 = parts[1]
        switcher = {
            'changestatus': stuff,
            'main':mainchanger,
            'category': chosen_category,
            'product': product_info,
            'back': chosen_category, 
            'addtocart': add_cart,
            '+': addsubtract,
            '-': addsubtract,
            'addbyself': product_info,
            'accept': accepted,
            'cancel': accepted,
            
        }
        func = switcher.get(part1, uncknown_callback)
        func(message, bot, part2)
except Exception:
    pass