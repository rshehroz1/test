from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from buttons.callback_data import lang, main

btn_lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Uz ðºð¿', callback_data=lang.new(name='uz')),
            InlineKeyboardButton(text='Ru ð·ðº', callback_data=lang.new(name='ru'))
        ]
    ]
)

btn_info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ayollarni himoya orderi haqida maâlumot. ð§',
                                 web_app=WebAppInfo(url="https://iiv.uz/news/himoya-orderi-haqida-bilasizmi")),
        ],
        [
            InlineKeyboardButton(text='Ayollar huquqlari. ð®',
                                 web_app=WebAppInfo(url="https://nhrc.uz/oz/menu/prava-zhenschin"))
        ],
        [
            InlineKeyboardButton(text='Asosiy menuga qaytish ð', callback_data=main.new(name='back'))
        ]

    ]
)

btn_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ayollar haq va huquqlari haqida ma'lumot ð§",
                                 callback_data=main.new(name='order')),
        ],
        [
            InlineKeyboardButton(text='Bola puli olish tartibi. ð',
                                 web_app=WebAppInfo(url="https://www.youtube.com/watch?v=lILU9yri0WE"))
        ],
        [
            InlineKeyboardButton(text='Bola puli uchun ariza yuborish. ð', callback_data=main.new(name='ariza'))
        ]
    ]
)
