from aiogram.types import InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

shop_bt = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(
            text="Shop", web_app=WebAppInfo(url='https://bulavka.uz/uz/telegram.html')
        )
    ]
]


                              )