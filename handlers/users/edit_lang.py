from aiogram import types

from keyboards.default.City import cityuz, cityru
from keyboards.default.setings import EDITRU, EDITUZ
from keyboards.default.Lang import LANG
from loader import dp,db

@dp.message_handler(text="⚙️ Настройки")
async def bot_seting(message: types.Message):
    try:
        message_id = message.from_user.id
        id_send = db.select_editlang(id=message_id)
        for idsend in id_send:
            sql_id = idsend[1]
            sql_city =idsend[2]
        await message.answer(f"Ваши текущие настройки\n\nЯзык: {sql_id}\nГород: {sql_city}",reply_markup=EDITRU)
    except:
        pass

@dp.message_handler(text="⚙️ Sozlamalar")
async def bot_seting(message: types.Message):
    try:
        message_id = message.from_user.id
        id_send = db.select_editlang(id=message_id)
        for idsend in id_send:
            sql_id = idsend[1]
            sql_city =idsend[2]
        await message.answer(f"Hozirgi sozlamalaringiz\n\nTil: {sql_id}\nShahar: {sql_city}",reply_markup=EDITUZ)
    except:
        pass

@dp.message_handler(text="🇺🇿 Tilni o'zgartirish")
async def bot_seting(message: types.Message):
    await message.answer("Iltimos, tilni tanlang.",reply_markup=LANG)

@dp.message_handler(text="📍 Shaharni o'zgartirish")
async def bot_seting(message: types.Message):
    await message.answer("Iltimos, shahringizni tanlang.",reply_markup=cityuz)

@dp.message_handler(text="🇷🇺 Поменять язык")
async def bot_seting(message: types.Message):
    await message.answer("Пожалуйста, выберите язык.",reply_markup=LANG)

@dp.message_handler(text="📍 Поменять город")
async def bot_seting(message: types.Message):
    await message.answer("Пожалуйста, выберите свой город.",reply_markup=cityru)


