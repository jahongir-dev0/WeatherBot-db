from  aiogram.types import KeyboardButton, ReplyKeyboardMarkup

EDITRU = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇷🇺 Поменять язык")],
        [KeyboardButton(text="📍 Поменять город")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

EDITUZ = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 Tilni o'zgartirish")],
        [KeyboardButton(text="📍 Shaharni o'zgartirish")],
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)

