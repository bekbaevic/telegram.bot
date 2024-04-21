from aiogram import F, Router, html,types,Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types.web_app_info import WebAppInfo

import webapp
import text
import kb
router = Router()

@router.message(Command('start'))
async def start_hadler(msg: Message):
    await msg.answer(text.start_text.format(name = msg.from_user.full_name), reply_markup=kb.shop_bt)

@router.message(F.text == "Shop")
async def webapp_handler(msg: Message):
    await msg.answer('Magazinga Xush kelib siz!',reply_markup=kb.shop_bt)

