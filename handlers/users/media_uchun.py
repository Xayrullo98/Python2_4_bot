from aiogram import types
from aiogram.types import ContentTypes, InputFile

from loader import dp,bot


# Echo bot
@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text=f" Fayl qabul qilindi")

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text=f"{message}")

@dp.message_handler(text="Ichimliklar")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/UstozShogird/25032'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu pepsi")
    rasm_manzili = 'https://t.me/UstozShogird/17932'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption="Bu pepsi")
    rasm_manzili = 'https://t.me/UstozShogird/25032'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption="Bu pepsi")
































