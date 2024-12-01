from  aiogram.types import KeyboardButton, ReplyKeyboardMarkup

LANG = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇷🇺 Русский")],
        [KeyboardButton(text="🇺🇿 O'zbekcha")]
    ],
    resize_keyboard=True
)