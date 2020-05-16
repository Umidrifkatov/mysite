from .constants import *
from . import models
from telebot import types
import telebot
# from datetime import datetime
from django.utils import timezone

try:
    def main_menu(message, bot, *args):

        user = models.TgUser.objects.get(userid = message.from_user.id)
        cartall = models.Category.objects.filter(parent = None, active=True)
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buttons = [types.InlineKeyboardButton(text=f'{text.name.upper()}', callback_data='category '+ text.name) for text in cartall]
        keyboard.add(*buttons)
        bot.send_photo(message.from_user.id, photo=pics['main'], caption=TEXTS[user.lang]['menu'], reply_markup=keyboard)
        bot.delete_message(message.from_user.id, message.message_id - 2)



    def mainchanger(message, bot, part):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        cartall = models.Category.objects.filter(parent = None, active=True)
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buttons = [types.InlineKeyboardButton(text=f'{text.name.upper()}', callback_data='category '+ text.name) for text in cartall]
        keyboard.add(*buttons)
        media = types.InputMediaPhoto(media=pics['main'], caption=TEXTS[user.lang]['menu'])
        bot.edit_message_media(chat_id=message.from_user.id, media=media, message_id=message.message.message_id, reply_markup=keyboard)
        
        


    def chosen_category(message, bot, part):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        category = models.Category.objects.get(name=part)
        allitems = models.Product.objects.filter(category=category, active=True).exclude(photo = None)
        allcat = models.Category.objects.filter(parent=category, active=True)
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buttonsc = [types.InlineKeyboardButton(text=f'{z.name.upper()}', callback_data='category '+ z.name)for z in allcat]
        buttonsi = [types.InlineKeyboardButton(text=z.name, callback_data='product '+ z.name)for z in allitems]
        
        keyboard.add(*buttonsc)
        keyboard.add(*buttonsi)
        try:    
            back = types.InlineKeyboardButton(text=BUTTONS[user.lang]['back'], callback_data='back '+ category.parent.name)
            keyboard.add(back)
        except Exception:
            back = types.InlineKeyboardButton(text=BUTTONS[user.lang]['back'], callback_data='main main')
            keyboard.add(back)
        media = types.InputMediaPhoto(media=pics['category'], caption=part)
        bot.edit_message_media(chat_id=message.from_user.id, media=media, message_id=message.message.message_id, reply_markup=keyboard)   
            

    def product_info(message, bot, part):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        currency = TEXTS[user.lang]['currency']
        qty = TEXTS[user.lang]['qty']
        if len(part.split()) > 1 and part.split()[0] == part.split()[1]:
            part = part.split()[0]
            cart = models.Cart.objects.get(id=int(part))
        else:
            item = models.Product.objects.get(name=part)
            cart = models.Cart.objects.create(product=item, user=user)
        text = f'<strong>{cart.product.name}\n{cart.product.price} {currency}</strong>\n\n{cart.product.caption}\n\n<code>{cart.product.price} {currency} x {cart.qty} {qty} = {cart.product.price * cart.qty} {currency}</code>'
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        buttonadd = types.InlineKeyboardButton(text=uneditable['-'], callback_data='- '+ str(cart.id))
        buttonsub = types.InlineKeyboardButton(text=uneditable['+'], callback_data='+ '+ str(cart.id))
        addbyhand = types.InlineKeyboardButton(text=str(cart.qty), callback_data='addbyself '+ str(cart.id))
        backb = types.InlineKeyboardButton(text=BUTTONS[user.lang]['back'], callback_data='back '+ cart.product.category.name)
        addtocart = types.InlineKeyboardButton(text=BUTTONS[user.lang]['addtocart'], callback_data='addtocart '+ str(cart.id))
        keyboard.add(buttonadd, addbyhand, buttonsub)
        keyboard.add(addtocart)
        keyboard.add(backb)
        media = types.InputMediaPhoto(media=cart.product.photo, caption=text, parse_mode='HTML')
        bot.edit_message_media(chat_id=message.from_user.id, media=media, message_id=message.message.message_id, reply_markup=keyboard)
        

    def add_cart(message, bot, part):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        cart = models.Cart.objects.get(id=int(part))
        try:
            allcart = models.Cart.objects.get(status=True, user__userid=message.from_user.id, product__name=cart.product.name)
            if allcart.product.name == cart.product.name:
                allcart.qty = allcart.qty + cart.qty
                allcart.status = True
                allcart.save()
            else:
                cart.status = True
                cart.save()
        except Exception:
            cart.status = True
            cart.save()
        ret = cart.product.category.name
        bot.answer_callback_query(callback_query_id=message.id, text=TEXTS[user.lang]['addedtocart'])
        chosen_category(message, bot, ret)
        
        
    

    def addsubtract(message, bot, part):
        cart = models.Cart.objects.get(id=int(part))
        if message.data.split()[0] == '+':
            cart.qty = cart.qty + 1
        elif message.data.split()[0] == '-' and cart.qty >= 2:
            cart.qty = cart.qty - 1
        cart.save()
        part = f'{cart.id} {cart.id}'
        product_info(message, bot, part)
        
    

    def get_settings(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        user.step = user_step['default']
        user.save()
        text = BUTTONS[user.lang]['settings']
        reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton(text= BUTTONS[user.lang]['back'])
        button4 = types.KeyboardButton(text= BUTTONS[user.lang]['lang'])
        button2 = types.KeyboardButton(text= BUTTONS[user.lang]['phone'])
        button5 = types.KeyboardButton(text= BUTTONS[user.lang]['history'])
        reply_keyboard.add(button2, button4)
        reply_keyboard.add(button5)
        reply_keyboard.add(button1)
        bot.send_message(message.from_user.id, text, reply_markup=reply_keyboard)


    def changelang(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        text = uneditable['text']
        user.step = user_step['enter_lang']
        user.save()
        reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttons = [types.KeyboardButton(text=i) for i in uneditable['buttons']]
        reply_keyboard.add(*buttons)
        bot.send_message(message.from_user.id, text, reply_markup=reply_keyboard)
        
        
    def changephone(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        if user.step != user_step['changephone']:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            button = types.KeyboardButton(text=BUTTONS[user.lang]['sendphone'], request_contact=True)
            keyboard.add(button)
            back = types.KeyboardButton(text=BUTTONS[user.lang]['back'])
            keyboard.add(back)
            bot.send_message(message.from_user.id, TEXTS[user.lang]['phonerequest'], reply_markup=keyboard)
            user.step = user_step['changephone']
            user.save()
        elif user.step == user_step['changephone']:
            if message.content_type == 'contact':
                a = message.contact.phone_number
                if a.startswith('+'):
                    a = a[1:]
                user.phone = a
                user.save()         
                get_settings(message, bot)
            elif len(message.text) == 12 and message.text.isdigit():
                user.phone = message.text 
                user.save()         
                get_settings(message, bot)


    def get_history(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        allorder = models.Order.objects.filter(user=user, status='✅ Выполнено')
        for i in allorder:
            bot.send_message(message.from_user.id, i.withmarkup, parse_mode='HTML', disable_web_page_preview=True)


    def get_about(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url1 = types.InlineKeyboardButton(text="Telgram", url="https://t.me/alati_uzb")
        url2 = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/alati_uzb/")
        url3 = types.InlineKeyboardButton(text="Facebook", url="https://www.facebook.com/Alati_uzb-2308671186056418/?ref=page_internal")
        keyboard.add(url1, url2, url3)
        pic = pics['about']
        text = TEXTS[user.lang]['about']
        bot.send_photo(message.chat.id, pic, caption=text, reply_markup=keyboard)
        

    def get_cart(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        qty = TEXTS[user.lang]['qty']
        currency = TEXTS[user.lang]['currency']
        total = TEXTS[user.lang]['total']
        
        cartall = models.Cart.objects.filter(status=True, user__userid=message.from_user.id)
        text = ''
        if cartall:
            total_sum = 0     
            for cart in cartall:          
                cart_total = cart.qty * cart.product.price          
                total_sum = cart_total + total_sum
                text += f'<strong>{cart.product.name}</strong>\n<code>{cart.product.price} x {cart.qty} {qty} = {cart_total} {currency}\n</code>'         
            text += f'\n\n{total} {total_sum} {currency}'
        else:
            text += TEXTS[user.lang]['emptycart']   
        user.step = user_step['chosetodel']
        user.save() 
        buttons = [types.KeyboardButton(text = uneditable['d'] + text.product.name) for text in cartall]
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(*buttons)
        button = types.KeyboardButton(text=BUTTONS[user.lang]['createorder'])
        button1 = types.KeyboardButton(text=BUTTONS[user.lang]['clearcart'])
        button2 = types.KeyboardButton(text=BUTTONS[user.lang]['back'])
        keyboard.add(button, button1, button2)
        bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')


    def clear_cart(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        models.Cart.objects.filter(user=user).delete()
        get_cart(message, bot)  



    def choose_todel(message, bot):
        try:
            parts = message.text.split()
            models.Cart.objects.filter(user__userid=message.from_user.id, product__name=parts[1]).delete()
            get_cart(message, bot)
        except Exception:
            pass
        



    def main_interface(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        user.step = user_step['default']
        user.save()
        reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton(text=BUTTONS[user.lang]['menu'])
        button2 = types.KeyboardButton(text=BUTTONS[user.lang]['cart'])
        button3 = types.KeyboardButton(text=BUTTONS[user.lang]['settings'])
        button4 = types.KeyboardButton(text=BUTTONS[user.lang]['about'])
        reply_keyboard.add(button1)
        reply_keyboard.add(button2)
        reply_keyboard.add(button3, button4)
        text = TEXTS[user.lang]['firstmessage']
        bot.send_message(message.from_user.id, text, reply_markup=reply_keyboard)
        
        
    def enter_lang(message, bot):
        mst = message.text
        user = models.TgUser.objects.get(userid = message.from_user.id)
        if mst in uneditable['buttons']:
            if mst == uneditable['buttons'][0]:
                user.lang = 'ru' 
            # additional ifs uz en uz
            user.step = user_step['default']
            user.name = '@'+ message.from_user.username
            user.save()
            main_interface(message, bot)
        else:
            bot.send_message(message.from_user.id, uneditable['text'])
            

    def start_message(message, bot):
        if models.TgUser.objects.filter(userid = message.from_user.id).exists() and models.TgUser.objects.get(userid = message.from_user.id).lang != None:
            user = models.TgUser.objects.get(userid = message.from_user.id)
            user.step = user_step['default']
            user.save()
            main_interface(message, bot)
            
        else:
            if models.TgUser.objects.filter(userid = message.from_user.id).exists(): 
                user = models.TgUser.objects.get(userid = message.from_user.id)
                user.step = user_step['enter_lang']
                user.save()
            else:
                user = models.TgUser.objects.create(userid = message.from_user.id, step = user_step['enter_lang'])
            text = uneditable['text']
            reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            buttons = [types.KeyboardButton(text=i) for i in uneditable['buttons']]
            reply_keyboard.add(*buttons)
            bot.send_message(message.from_user.id, text, reply_markup=reply_keyboard)
            


    def check_out(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        if workingtime():      
            cart = models.Cart.objects.filter(user=user, status=True)
            count = 0
            for i in cart:
                count += 1
            if count >= 1:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                button = [types.KeyboardButton(text=BUTTONS[user.lang]['deliver'])]
                if SETTINGS['takeon']:
                    button.append(types.KeyboardButton(text=BUTTONS[user.lang]['takeon']))
                keyboard.add(*button)
                back = types.KeyboardButton(text=BUTTONS[user.lang]['back'])
                keyboard.add(back)
                user.step = user_step['deliverortake']
                user.save()
                bot.send_message(message.from_user.id, TEXTS[user.lang]['delivercost'], reply_markup=keyboard)
            else:
                bot.send_message(message.from_user.id, TEXTS[user.lang]['cantcheckout'])
        else:
            bot.send_message(message.from_user.id, TEXTS[user.lang]['notworking'])
            

    def create_order(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        user.step = user_step['default']
        user.save()
        carts = models.Cart.objects.filter(status=True, user=user)
        qty = TEXTS[user.lang]['qty']
        currency = TEXTS[user.lang]['currency']
        total = TEXTS[user.lang]['total']
        chosenpay = TEXTS[user.lang]['chosenpayment']
        delivercosttext = TEXTS[user.lang]['delivercost']
        delivercost = SETTINGS['delivercost']
        total1 = TEXTS[user.lang]['total+']
        orderid = TEXTS[user.lang]['orderid']
        location = TEXTS[user.lang]['location']
        here = TEXTS[user.lang]['mylocation']
        timetoget = TEXTS[user.lang]['timetoget']
        realtime = TEXTS[user.lang]['today']
        gettype = TEXTS[user.lang]['gettype']
        delive = BUTTONS[user.lang]['deliver']
        getbyhand = BUTTONS[user.lang]['takeon']
        phoneis = BUTTONS[user.lang]['phone']
        if user.location != None:
            lon = user.location.split()[0]
            lat = user.location.split()[1]
        
        text = ''
        if not user.delivery:
            delivercost = 0
            bot.send_location(message.from_user.id, uneditable['location'][0], uneditable['location'][1])
        if user.deferred:
            realtime = TEXTS[user.lang]['tomorrow']
        
        textfororder = ''
        
        itemstext = ''
        total_sum = 0
        for cart in carts:
            item_sum = cart.qty * cart.product.price
            total_sum += item_sum
            itemstext += f'\n<strong>{cart.product.name}</strong>\n<code>{cart.qty} {qty} x {cart.product.price} {currency} = {item_sum} {currency}</code>'
            textfororder += f'{cart.product.name} x {cart.qty}'
        allsum = total_sum + delivercost
        
        
        order = models.Order.objects.create(user=user, itemandcost=textfororder, total=allsum, deferred=user.deferred ,deliver=user.delivery,geo=user.location, status='💙Не подтвержден')
        text += f'<strong>{chosenpay}</strong> {user.payment}\n'
        text += f'{itemstext}\n\n<strong>{total}</strong> {total_sum} {currency}\n'
        text += f'<strong>{delivercosttext}</strong> {delivercost} {currency}\n'
        text += f'<strong>{total1}</strong> {allsum} {currency}' 
        
        if user.delivery:
            text =  f'<strong>{location}</strong> <a href="https://yandex.ru/maps/?pt={lat},{lon}&z=18&l=map">[{here}]</a>\n{text}'
            text = f'<strong>{gettype}</strong> {delive}\n{text}'
            text = f'<strong>{timetoget}</strong> {realtime}\n{text}'
        if not user.delivery:
            text = f'<strong>{gettype}</strong> {getbyhand}\n{text}'
        text = f'<strong>{phoneis}</strong>: +{user.phone}\n{text}'
        text = f'<strong>{orderid}</strong> №00{order.id}\n{text}'
        order.withmarkup = text
        order.save()
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        yes = types.InlineKeyboardButton(text=BUTTONS[user.lang]['agree'], callback_data='accept ' + str(order.id))
        no = types.InlineKeyboardButton(text=BUTTONS[user.lang]['cancel'], callback_data='cancel ' + str(order.id))
        keyboard.add(no, yes)
        bot.send_message(message.from_user.id, text, reply_markup=keyboard ,parse_mode='HTML', disable_web_page_preview=True)


        
        
    def accepted(message, bot, part):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        part2 = message.data.split()
        order = models.Order.objects.get(id=int(part))
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        ordeuser = f'\n\nusername: {order.user.name}\nuserid: #i{order.user.userid}'
        if part2[0] == 'accept':
            carts = models.Cart.objects.filter(user=user).delete()
            no = types.InlineKeyboardButton(text=BUTTONS[user.lang]['cancel'], callback_data='cancell ' + str(order.id))
            keyboard.add(no)
            order.status = '💛 Ожидает'
            status = TEXTS[user.lang]['accepted']
            text = f'{status}\n' + order.withmarkup
            bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=text, parse_mode='HTML', reply_markup=keyboard, disable_web_page_preview=True)
            order.messageid = message.message.message_id
            #to group
            board = types.InlineKeyboardMarkup(row_width=1)
            no = types.InlineKeyboardButton(text='Изменить статус', callback_data='changestatus changestatus '+ part)
            board.add(no)
            
            adminmessage = bot.send_message(SETTINGS['group_id'], order.withmarkup + ordeuser, reply_markup=board, parse_mode='HTML', disable_web_page_preview=True)
            user.messageid = adminmessage.message_id
            user.save()
        
        
        elif part2[0] == 'cancell':
            status = TEXTS[user.lang]['declined']
            text = f'{status}\n' + order.withmarkup
            bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=text, parse_mode='HTML', reply_markup=keyboard)
            order.status = '❤️ Отменен'
            grouptext = '#ОТМЕНЕН ПОЛЬЗОВАТЕЛЕМ\n' + order.withmarkup + ordeuser
            bot.edit_message_text(chat_id=SETTINGS['group_id'], message_id=user.messageid, text=grouptext, parse_mode='HTML', disable_web_page_preview=True)
        elif part2[0] == 'cancel':
            status = TEXTS[user.lang]['declined']
            text = f'{status}\n' + order.withmarkup
            bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=text, parse_mode='HTML', reply_markup=keyboard, disable_web_page_preview=True)
            order.status = '❤️ Отменен'
        order.save()    
        
    


    def payment_method(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        if user.step != user_step['get_paymethod']:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            buttons = []
            if SETTINGS['cash']:
                buttons.append(types.KeyboardButton(text=BUTTONS[user.lang]['cash']))
            if SETTINGS['click']:
                buttons.append(types.KeyboardButton(text=BUTTONS[user.lang]['click']))
            if SETTINGS['terminal']:
                buttons.append(types.KeyboardButton(text=BUTTONS[user.lang]['terminal']))
            if SETTINGS['payme']:
                buttons.append(types.KeyboardButton(text=BUTTONS[user.lang]['payme']))
            keyboard.add(*buttons)
            back = types.KeyboardButton(text=BUTTONS[user.lang]['back'])
            keyboard.add(back)
            bot.send_message(message.from_user.id, TEXTS[user.lang]['chosepayment'], reply_markup=keyboard)
            user.step = user_step['get_paymethod']
            user.save()
        elif user.step == user_step['get_paymethod']:
            buts = [BUTTONS[user.lang]['payme'], BUTTONS[user.lang]['click'], BUTTONS[user.lang]['terminal'], BUTTONS[user.lang]['cash']]
            if message.text in buts:  
                if message.text == BUTTONS[user.lang]['payme'] and SETTINGS['payme']:
                    user.payment = 'PayMe'
                elif message.text == BUTTONS[user.lang]['terminal'] and SETTINGS['terminal']:
                    user.payment = 'Terminal'
                elif message.text == BUTTONS[user.lang]['click'] and SETTINGS['click']:
                    user.payment = 'Click'
                elif message.text == BUTTONS[user.lang]['cash'] and SETTINGS['cash']:
                    user.payment = TEXTS[user.lang]['cash']
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                back = types.KeyboardButton(text=BUTTONS[user.lang]['back'])
                keyboard.add(back)
                bot.send_message(message.from_user.id, TEXTS[user.lang]['choseone'], reply_markup=keyboard)
                user.save()
                create_order(message, bot)
        
                
    

    def get_phone(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        if user.step != user_step['get_phone']:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            button = types.KeyboardButton(text=BUTTONS[user.lang]['sendphone'], request_contact=True)
            keyboard.add(button)
            back = types.KeyboardButton(text=BUTTONS[user.lang]['back'])
            keyboard.add(back)
            bot.send_message(message.from_user.id, TEXTS[user.lang]['phonerequest'], reply_markup=keyboard)
            user.step = user_step['get_phone']
            user.save()
        elif user.step == user_step['get_phone']:
            if message.content_type == 'contact':
                a = message.contact.phone_number
                if a.startswith('+'):
                    a = a[1:]
                user.phone = a
                user.save()         
                payment_method(message, bot)
            elif len(message.text) == 12 and message.text.isdigit():
                user.phone = message.text 
                user.save()         
                payment_method(message, bot)
            



    def get_location(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        if user.step != user_step['get_location']:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            button = types.KeyboardButton(text=BUTTONS[user.lang]['sendlocation'], request_location=True)
            keyboard.add(button)
            back = types.KeyboardButton(text=BUTTONS[user.lang]['back'])
            keyboard.add(back)
            bot.send_message(message.from_user.id, TEXTS[user.lang]['locationrequest'], reply_markup=keyboard)
            user.step = user_step['get_location']
            user.save()
        
        elif user.step == user_step['get_location']: 
            if message.content_type == 'location':
                location = f'{message.location.latitude} {message.location.longitude}'
                user.location = location
                user.save()
                get_phone(message, bot)
            


    def get_day(message, bot):
        user = models.TgUser.objects.get(userid = message.from_user.id)
        if message.text == BUTTONS[user.lang]['today'] or message.text == BUTTONS[user.lang]['tomorrow']:
            if message.text == BUTTONS[user.lang]['today']:
                user.deferred = False
            elif message.text == BUTTONS[user.lang]['tomorrow']:
                user.deferred = True
            user.save()
            get_location(message, bot)
        
        

    def deliverortake(message, bot):   
        user = models.TgUser.objects.get(userid = message.from_user.id)
        if message.text == BUTTONS[user.lang]['deliver']: 
                
            user.delivery = True
            if SETTINGS['deferred']:           
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                button = types.KeyboardButton(text=BUTTONS[user.lang]['today'])
                button2 = types.KeyboardButton(text=BUTTONS[user.lang]['tomorrow'])
                keyboard.add(button, button2)            
                back = types.KeyboardButton(text=BUTTONS[user.lang]['back'])
                keyboard.add(back)            
                bot.send_message(message.from_user.id, TEXTS[user.lang]['choseone'], reply_markup=keyboard)
                user.step = user_step['get_day']
                user.save()            
            
            else:
                get_location(message, bot)
            
            
        elif message.text == BUTTONS[user.lang]['takeon'] and SETTINGS['takeon']:
            user.delivery = False
            user.save()
            # bot.send_location(message.from_user.id, uneditable['location'][0], uneditable['location'][1])
            # create_order(message, bot)
            get_phone(message, bot)


    def makestatistics():
        lastday = 0
        lastweek = 0
        lastmonth = 0
        now = timezone.now()
        today = now.day
        thisweek = now.isocalendar()[1]
        thismonth = now.month()
        if lastday != today:
            pass
        if lastmonth != thismonth:
            pass
        if lastweek != thisweek:
            pass
        




    def stuff(message, bot, part):
        timenow = str(timezone.now().replace(microsecond=0))
        board = types.InlineKeyboardMarkup(row_width=1)
        part2 = part.split()[0]
        part = part.split()[1]
        order = models.Order.objects.get(id=int(part))
        user = order.user
        keys = [
        (types.InlineKeyboardButton(text='Доставляется', callback_data='changestatus delivering '+ part)),
        (types.InlineKeyboardButton(text='Принято', callback_data='changestatus accepted '+ part)),
        (types.InlineKeyboardButton(text='Отменено', callback_data='changestatus declined '+ part)),
        (types.InlineKeyboardButton(text='Изменить статус', callback_data='changestatus changestatus '+ part)),
        (types.InlineKeyboardButton(text='Завершено', callback_data='changestatus done '+ part)),
        ]
        keyboard =[]
        text = ''
        
        if part2 == 'changestatus' and order.status == '💛 Ожидает':
            keyboard.append(keys[1])
            keyboard.append(keys[2])
        elif part2 == 'changestatus' and order.status == '💚 Принято':
            if order.deliver:   
                keyboard.append(keys[0])
            else:
                keyboard.append(keys[4])
            keyboard.append(keys[2])
            
            
        elif part2 == 'changestatus' and order.status == '🚗 Доставляется':
            keyboard.append(keys[4])
            keyboard.append(keys[2])
        
        
        elif part2 == 'accepted':
            order.status = '💚 Принято'
            keyboard.append(keys[3])
            text = '#ПРИНЯТО ' + timenow
            usertext = TEXTS[user.lang]['orderid'] + ' №00' + str(order.id) + '\n' + TEXTS[user.lang]['orderaccepted']
            bot.send_message(order.user.userid, usertext)
            bot.edit_message_text(chat_id=user.userid, message_id=order.messageid, text=order.withmarkup, parse_mode='HTML', disable_web_page_preview=True)
        
        elif part2 == 'delivering':
            order.status = '🚗 Доставляется' 
            keyboard.append(keys[3])
            text = '#ДОСТАВЛЯЕТСЯ ' + timenow
            # bot.send_message to user
        elif part2 == 'done':
            order.status = '✅ Выполнено'
            text = '#ВЫПОЛНЕНО ' + timenow
            makestatistics()
        
        elif part2 == 'declined':
            order.status = '❤️ Отменен'
            text = '#ОТМЕНЕНО ' + timenow
            # bot.send_message to user
        board.add(*keyboard)
        text += '\n' + order.withmarkup
        order.withmarkup = text
        
        addition = f'\n\nusername: {order.user.name}\nuserid: #i{order.user.userid}'  
        text += addition
        order.save()
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id, text=text, parse_mode='HTML', reply_markup=board, disable_web_page_preview=True)
        
except Exception:
    pass   