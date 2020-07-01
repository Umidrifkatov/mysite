


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
    'admin_id': 121637541,
    
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
    'buttons': ['Русский', 'O\'zbekcha'],
    'text': 'Выберите язык чтобы продолжить\n Davom etirish uchun tilni tanlang'
}


TEXTS = {
    'ru':{
        'ordersent':'Ваш заказ отправлен. Пожалуйста будьте готовы к звонку курьера',
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
        'ordersent':'Buyurtmangiz tayyor. Qo\'ng\'iroq qabul qilishga tayyor boling.',
        'orderaccepted': 'Buyurtma qabul qilindi.',
        'gettype':'Olish usuli:',
        'tomorrow':'Ertaga',
        'today':'Bugun',
        'timetoget': 'Olib kelish vaqti',
        'mylocation': 'Karta',
        'location': 'Olib kelish manzili',
        'declined':'Bekor qilindi',
        'accepted': 'Qabul qilindi',
        'orderid':'Buyurma raqami:',
        'total+':'Jami:',
        'cash': 'Naqd pul',
        'chosenpayment':'To\'lo\'v usuli:',
        'chosepayment': 'To\'lo\'v usulini tanlang',
        'phonerequest':'Telefon raqamingizni yuboring namuna: 998912345678',
        'choseone': 'Tanlang:',
        'locationrequest':'Locatsiyangizni yuboring',
        'notworking':'Kechirasiz hozir ish vaqti emas, butyurtmani kechroq amal qiling',
        'delivercost':'Olibkelish:',
        'cantchekout':'Savatingiz bo\'sh',
        'cartcleared': '♻️ Savat tozalandi',
        'addedtocart':'✅ Savatga q\'o\'shildi',
        'menu': 'Menu',
        'emptycart': 'Savatingiz bo\'sh',
        'total':'Jami:',
        'currency': '[so\'m]',
        'qty': 'dona',
        'firstmessage': 'Nima buyurasiz?',
        'about':'''about text about text''',
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
    },
        'uz':{
        'history': 'Buyurtmalar tarixi',
        'cancel':'❌ Bekor qilish',
        'agree':'✅ Tastdiqlash',
        'payme':'PayMe',
        'click':'Click',
        'terminal':'Terminal',
        'cash':'Naqd pul',
        'sendphone':'📱 Nomerimni yuborish',
        'sendlocation':'📍 Lokatsiyamni yuborish',
        'tomorrow': 'Ertaga',
        'today': 'Bugun',
        'takeon':'Olib ketish',
        'deliver':'Etkazib berish',
        'addtocart': 'Savatga qo\'shish',
        'clearcart': 'Tozalash',
        'createorder': 'Tasdiqlash',
        'back': 'Ortga',
        'menu': 'Menyu',
        'settings': 'Sozlamalar',
        'cart': 'Savat',
        'about': 'Biz haqimizda',
        'phone': 'Telefon',
        'name': 'Ism',
        'lang': 'Til',
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

}


pics = {
    'main': 'AgACAgIAAxkDAAIcIF6_4dtN5p64oVH7eZmyz1GfbkOlAAIgrzEbQvUAAUq_LirB1I6qyPxdyw4ABAEAAwIAA3kAAzy2BQABGQQ',
    'category': 'AgACAgIAAxkDAAIcH16_4b_QP9znmFiH8NjmSKvjwdCVAAIdrzEbQvUAAUqWBJ1x-t40-s6yg5IuAAMBAAMCAAN5AAOTeAEAARkE',
    'about':'AgACAgIAAxkDAAIcIV6_4ggVDwH3lN1_sYFqax-xoX_bAAIhrzEbQvUAAUq4IFSvThEWsnLHwg8ABAEAAwIAA3kAAz8TBwABGQQ',
    'additional':'AgACAgIAAxkDAAIcIF6_4dtN5p64oVH7eZmyz1GfbkOlAAIgrzEbQvUAAUq_LirB1I6qyPxdyw4ABAEAAwIAA3kAAzy2BQABGQQ',
}



