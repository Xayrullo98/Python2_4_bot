from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

oziq_ovqat_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Non maxsulotlari"),
            KeyboardButton(text="Ichimliklar"),
            KeyboardButton(text="Shirinliklar")
        ],
        [
            KeyboardButton(text="Sut maxsulotlari"),
            KeyboardButton(text="Go'sht maxsulotlari")
        ]
    ],
    resize_keyboard=True
)