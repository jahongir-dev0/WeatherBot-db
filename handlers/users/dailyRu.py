import sqlite3

from aiogram import types
from keyboards.default.City import cityuz, cityru
from keyboards.default.weather import WeatherRU,WeatherRU
from . siteWeather import *
from loader import dp,db

@dp.message_handler(text="📅 Прогноз на сегодня")
async def bot_echo(messge: types.Message):
    try:
        db.add_lang(id=messge.from_user.id,
                    )
    except sqlite3.IntegrityError as err:
        pass
    id =messge.chat.id
    lang = db.select_lang(id=id)
    if lang[2] == 'NO':
        await messge.answer("<b>Сначала укажите регион...</b>",reply_markup=cityru)
    if lang[2] == 'Ташкент':
        await messge.answer(text=f"{kunru('tashkent')} \n<b>{Viloyatru('tashkent')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('tashkent')}...{minru('tashkent')} , {obhavoru('tashkent')}\n\n"
                                 f"<b>Утро</b> : {tongru('tashkent')} \n"
                                 f"<b>День</b> : {kunhru('tashkent')}\n"
                                 f"<b>Вечер</b> : {oqshomru('tashkent')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('tashkent')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('tashkent')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == 'Фергана':
        await messge.answer(text=f"{kunru('ferghana')} \n<b>{Viloyatru('ferghana')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('ferghana')}...{minru('ferghana')} , {obhavoru('ferghana')}\n\n"
                                 f"<b>Утро</b> : {tongru('ferghana')} \n"
                                 f"<b>День</b> : {kunhru('ferghana')}\n"
                                 f"<b>Вечер</b> : {oqshomru('ferghana')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('ferghana')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('ferghana')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == 'Самарканд':
        await messge.answer(text=f"{kunru('samarkand')} \n<b>{Viloyatru('samarkand')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('samarkand')}...{minru('samarkand')} , {obhavoru('samarkand')}\n\n"
                                 f"<b>Утро</b> : {tongru('samarkand')} \n"
                                 f"<b>День</b> : {kunhru('samarkand')}\n"
                                 f"<b>Вечер</b> : {oqshomru('samarkand')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('samarkand')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('samarkand')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Андижан":
        await messge.answer(text=f"{kunru('andijan')} \n<b>{Viloyatru('andijan')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('andijan')}...{minru('andijan')} , {obhavoru('andijan')}\n\n"
                                 f"<b>Утро</b> : {tongru('andijan')} \n"
                                 f"<b>День</b> : {kunhru('andijan')}\n"
                                 f"<b>Вечер</b> : {oqshomru('andijan')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('andijan')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('andijan')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Бухара":
        await messge.answer(text=f"{kunru('bukhara')} \n<b>{Viloyatru('bukhara')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('bukhara')}...{minru('bukhara')} , {obhavoru('bukhara')}\n\n"
                                 f"<b>Утро</b> : {tongru('bukhara')} \n"
                                 f"<b>День</b> : {kunhru('bukhara')}\n"
                                 f"<b>Вечер</b> : {oqshomru('bukhara')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('bukhara')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('bukhara')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Гулистан":
        await messge.answer(text=f"{kunru('gulistan')} \n<b>{Viloyatru('gulistan')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('gulistan')}...{minru('gulistan')} , {obhavoru('gulistan')}\n\n"
                                 f"<b>Утро</b> : {tongru('gulistan')} \n"
                                 f"<b>День</b> : {kunhru('gulistan')}\n"
                                 f"<b>Вечер</b> : {oqshomru('gulistan')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('gulistan')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('gulistan')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Джизак":
        await messge.answer(text=f"{kunru('jizzakh')} \n<b>{Viloyatru('jizzakh')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('jizzakh')}...{minru('jizzakh')} , {obhavoru('jizzakh')}\n\n"
                                 f"<b>Утро</b> : {tongru('jizzakh')} \n"
                                 f"<b>День</b> : {kunhru('jizzakh')}\n"
                                 f"<b>Вечер</b> : {oqshomru('jizzakh')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('jizzakh')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('jizzakh')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Зарафшон":
        await messge.answer(text=f"{kunru('zarafshan')} \n<b>{Viloyatru('zarafshan')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('zarafshan')}...{minru('zarafshan')} , {obhavoru('zarafshan')}\n\n"
                                 f"<b>Утро</b> : {tongru('zarafshan')} \n"
                                 f"<b>День</b> : {kunhru('zarafshan')}\n"
                                 f"<b>Вечер</b> : {oqshomru('zarafshan')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('zarafshan')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('zarafshan')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Қарши":
        await messge.answer(text=f"{kunru('karshi')} \n<b>{Viloyatru('karshi')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('karshi')}...{minru('karshi')} , {obhavoru('karshi')}\n\n"
                                 f"<b>Утро</b> : {tongru('karshi')} \n"
                                 f"<b>День</b> : {kunhru('karshi')}\n"
                                 f"<b>Вечер</b> : {oqshomru('karshi')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('karshi')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('karshi')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Навои":
        await messge.answer(text=f"{kunru('navoi')} \n<b>{Viloyatru('navoi')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('navoi')}...{minru('navoi')} , {obhavoru('navoi')}\n\n"
                                 f"<b>Утро</b> : {tongru('navoi')} \n"
                                 f"<b>День</b> : {kunhru('navoi')}\n"
                                 f"<b>Вечер</b> : {oqshomru('navoi')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('navoi')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('navoi')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Наманган":
        await messge.answer(text=f"{kunru('namangan')} \n<b>{Viloyatru('namangan')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('namangan')}...{minru('namangan')} , {obhavoru('namangan')}\n\n"
                                 f"<b>Утро</b> : {tongru('namangan')} \n"
                                 f"<b>День</b> : {kunhru('namangan')}\n"
                                 f"<b>Вечер</b> : {oqshomru('namangan')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('namangan')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('namangan')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Нукус":
        await messge.answer(text=f"{kunru('nukus')} \n<b>{Viloyatru('nukus')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('nukus')}...{minru('nukus')} , {obhavoru('nukus')}\n\n"
                                 f"<b>Утро</b> : {tongru('nukus')} \n"
                                 f"<b>День</b> : {kunhru('nukus')}\n"
                                 f"<b>Вечер</b> : {oqshomru('nukus')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('nukus')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('nukus')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Хива":
        await messge.answer(text=f"{kunru('khiva')} \n<b>{Viloyatru('khiva')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('khiva')}...{minru('khiva')} , {obhavoru('khiva')}\n\n"
                                 f"<b>Утро</b> : {tongru('khiva')} \n"
                                 f"<b>День</b> : {kunhru('khiva')}\n"
                                 f"<b>Вечер</b> : {oqshomru('khiva')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('khiva')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('khiva')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Ургенч":
        await messge.answer(text=f"{kunru('urgench')} \n<b>{Viloyatru('urgench')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('urgench')}...{minru('urgench')} , {obhavoru('urgench')}\n\n"
                                 f"<b>Утро</b> : {tongru('urgench')} \n"
                                 f"<b>День</b> : {kunhru('urgench')}\n"
                                 f"<b>Вечер</b> : {oqshomru('urgench')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('urgench')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('urgench')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)
    if lang[2] == "Термиз":
        await messge.answer(text=f"{kunru('termez')} \n<b>{Viloyatru('termez')}</b> ожидаемая погода в регионе.\n\n"
                                 f"🌡 {haroratru('termez')}...{minru('termez')} , {obhavoru('termez')}\n\n"
                                 f"<b>Утро</b> : {tongru('termez')} \n"
                                 f"<b>День</b> : {kunhru('termez')}\n"
                                 f"<b>Вечер</b> : {oqshomru('termez')}\n"
                                 f"_________________________________________\n"
                                 f" {Oyru('termez')}\n"
                                 f"_________________________________________\n"
                                 f"{Namlikru('termez')}\n"
                                 f"Непрерывная информация о погоде  <a href='https://t.me/WeatherRUB_Robot'>Погода</a>\n"
                                 f"<b>Если вы считаете это полезным, поделитесь им со своими близкими</b>",reply_markup=WeatherRU,disable_web_page_preview=True)

@dp.message_handler(text="Ташкент")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Ташкент":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Фергана")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] == "Фергана":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Самарканд")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Самарканд":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Андижан")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Андижан":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Бухара")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Бухара":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Гулистан")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Гулистан":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass
@dp.message_handler(text="Джизак")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Джизак":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass
@dp.message_handler(text="Зарафшон")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Зарафшон":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Қарши")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Қарши":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Навои")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Навои":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Наманган")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Наманган":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Нукус")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Нукус":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Термиз")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Термиз":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="Ургенч")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Ургенч":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass
@dp.message_handler(text="Хива")
async def bot_uz(message: types.Message):
    message_text= message.text
    message_user = message.from_user
    try:
        db.update_user_city(id=message_user.id,
                            city=message_text)

        id = message.chat.id
        lang = db.select_lang(id=id)
        if lang[2] ==  "Хива":
            await message.answer("<b>Регион определен...</b>",reply_markup=WeatherRU)
    except:
        pass

@dp.message_handler(text="🗓 Прогноз на 3 дня")
async def bot_echo(message: types.Message):
    await message.answer("В каком регионе вы хотите получать информацию о погоде?",reply_markup=WeatherRU)



@dp.message_handler(text="🔙 Назад")
async def bot_echo(message: types.Message):
    await message.answer("<b>🔙 Назад</b>",reply_markup=WeatherRU)