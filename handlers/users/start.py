import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.City import cityuz, cityru
from loader import dp,db
from keyboards.default.Lang import LANG
from keyboards.default.weather import *

lang = f"<b>🌍 Choose a Language :</b>"
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        db.add_lang(id=message.from_user.id,
                    )
    except sqlite3.IntegrityError as err:
        pass
    id =message.chat.id
    lang = db.select_lang(id=id)
    if lang[1] == 'uz':
        await message.answer("<b>Пожалуйста, выберите язык.\n\nTilni tanlang.</b>",reply_markup=LANG)
    if lang[1] == '🇷🇺 Русский':
        await message.answer(f"<b>Какой прогноз вы хотели бы получить?</b>",reply_markup=WeatherRU)
    if lang[1] == "🇺🇿 O'zbekcha":
        await message.answer("<b>Qanday ob-havo ma'lumotini olishni istaysiz?</b>",reply_markup=WeatherUZ)

@dp.message_handler(text="🇺🇿 O'zbekcha")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_lang(id=message_user.id,
                            lang=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[1] ==  "🇺🇿 O'zbekcha":
            await message.answer("Iltimos, shahringizni tanlang.",reply_markup=cityuz)
    except:
        pass

@dp.message_handler(text='🇷🇺 Русский')
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_lang(id=message_user.id,
                            lang=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[1] == '🇷🇺 Русский':
            await message.answer("Пожалуйста, выберите свой город.",reply_markup=cityru)
    except:
        pass

@dp.message_handler(text="/stat")
async def bot_start(message: types.Message):
    users= db.select_all_foidalanuvchilar()
    for user in users:
        user_id= user[0]
    await  message.answer(text=f"<b> Statistikasi 📶\n\n👤 Foydalanuvchilar: {user_id}\n\n🟢 Bot holati: Online</b>",disable_web_page_preview=True)


