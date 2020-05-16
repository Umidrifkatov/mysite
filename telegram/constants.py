


SETTINGS = {
    'takeon': True,
    'workingtime': True,
    'deferred': True,
    'payme':True,
    'click':True,
    'terminal':True,
    'cash':True,
    'delivercost': 1000,
    'group_id': -490006863, 
    
}




def workingtime():
    from datetime import datetime
    now = datetime.now()
    if 1 < now.hour and now.hour < 23 and now.weekday() != 6:
        return True
    else:
        return False




uneditable = {
    'location': [12 ,18],
    '-':'➖',
    '+':'➕',
    'd':'❌ ',
    'buttons': ['Русский', 'O\'zbekcha', 'Узбекча', 'English'],
    'text': 'выберите язык...\n\n tilni tanlang...\n\nтилни танланг...'
}


TEXTS = {
    'ru':{
        
        'orderaccepted': 'Заказ принят.',
        'gettype':'Способ получения:',
        'tomorrow':'Завтра',
        'today':'Сегодня',
        'timetoget': 'Время доставки:',
        'mylocation': 'Карта',
        'location': 'Место доставки:',
        'declined':'Отменен',
        'accepted': 'Принят',
        'orderid':'Номер заказа:',
        'total+':'Итого:',
        'cash': 'Наличные',
        'chosenpayment':'Способ оплаты:',
        'chosepayment': 'Выберите способ оплаты',
        'phonerequest':'Отправьте или введите ваш номер телефона в формате: 998001234567 \nПримечание: Если вы планируете оплатить заказ онлайн с помощью Click, либо Payme, пожалуйста, укажите номер телефона, на который зарегистрирован аккаунт в соответствующем сервисе',
        'choseone': 'Выберите:',
        'locationrequest':'Отправте свою локацию пожалуйста',
        'notworking':'Извините, сейчас у нас нерабочее время, вы можете оформить заказ позже',
        'delivercost':'Доставка:',
        'cantchekout':'Ваша корзина пуста',
        'cartcleared': '♻️ Корзина очищена',
        'addedtocart':'✅ Добавлено в корзину',
        'menu': 'Меню',
        'emptycart': 'Корзина пуста',
        'total':'Сумма:',
        'currency': '[cyм]',
        'qty': 'шт.',
        'firstmessage': 'Закажем что нибудь?',
        'about':'''❄️Замороженные манты/самса/котлеты...\n💯Все натуральное\n🥩Только мясо 🐄 и 🐓\n🚛Доставка 12.000 сум по Ташкенту\n🕙ПН-СБ 10:00-19:00\n☎️ +998(95)1942746''',
    },
    'uz':{
        'firstmessage': 'Salom nima buyurtma qilasiz?',
    }
}








BUTTONS = {
    'ru':{
        'history': 'История заказов',
        'cancel':'❌ Отменить',
        'agree':'✅ Подтвердить',
        'payme':'PayMe',
        'click':'Click',
        'terminal':'Терминал',
        'cash':'Наличные',
        'sendphone':'📱 Отправить номер',
        'sendlocation':'📍 Отправить мою локацию',
        'tomorrow': 'Завтра',
        'today': 'Сегодня',
        'takeon':'Самовывоз',
        'deliver':'Доставка',
        'addtocart': 'Добавить в корзину',
        'clearcart': 'Очистить корзину',
        'createorder': 'Оформить',
        'back': 'Назад',
        'menu': 'Меню',
        'settings': 'Настройки',
        'cart': 'Корзина',
        'about': 'О нас',
        'phone': 'Телефон',
        'name': 'Имя',
        'lang': 'Язык',
    }
}


user_step = {
    'default': 0,
    'enter_lang': 1,
    'chosetodel': 2,
    'deliverortake': 3,
    'deferredtype': 4,
    'get_day': 5,
    'get_location': 6,
    'get_phone': 7,
    'get_paymethod': 8,
    'changephone': 9,
    # 'ENTER_PHONE': 10,
    # 'ENTER_LOCATION': 11,
    # 'ENTER_NAME': 12,
}


pics = {
    'main': 'AgACAgIAAxkDAAICLl6yA34Yx0ueU-tBlmvWNXTRxhycAAJWrTEb0CyQSZWvtMnlr5lW3CXBDgAEAQADAgADdwADRuYFAAEZBA',
    'category': 'AgACAgIAAxkDAAICLl6yA34Yx0ueU-tBlmvWNXTRxhycAAJWrTEb0CyQSZWvtMnlr5lW3CXBDgAEAQADAgADdwADRuYFAAEZBA',
    'about':'AgACAgIAAxkDAAICLl6yA34Yx0ueU-tBlmvWNXTRxhycAAJWrTEb0CyQSZWvtMnlr5lW3CXBDgAEAQADAgADdwADRuYFAAEZBA',
    'additional':'AgACAgIAAxkDAAICLl6yA34Yx0ueU-tBlmvWNXTRxhycAAJWrTEb0CyQSZWvtMnlr5lW3CXBDgAEAQADAgADdwADRuYFAAEZBA',
}



