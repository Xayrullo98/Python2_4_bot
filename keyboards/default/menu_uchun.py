from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from loader import obyekt
# menu_buttons = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Oziq ovqat"),
#             KeyboardButton(text="Kiyim kechaklar")
#         ],
#         [
#             KeyboardButton(text="elektronika"),
#             KeyboardButton(text="Sport")
#         ],
#         [
#             KeyboardButton(text="Adminga murojaat")
#         ],
#         [
#             KeyboardButton(text="Lokatsiya",request_location=True),
#             KeyboardButton(text="Kontakt",request_contact=True)
#         ]
#
#     ],
#     resize_keyboard=True
# )

menular = obyekt.select_barcha_menular()

j = 0
index= 0
keys = []
for menu in menular:
    if j % 2 == 0 and j != 0:
        index += 1
    if j % 2 == 0:
        keys.append([KeyboardButton(text=f'{menu[1]}', )])
    else:
        keys[index].append(KeyboardButton(text=f'{menu[1]}', ))
    j += 1

keys.append([KeyboardButton(text='Adminga murojaat')])
keys[index].append(KeyboardButton(text='Korzinka'))
menu_buttons = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)

tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)