from aiogram import types
from aiogram.types import ContentTypes

from loader import dp,bot
from filters.guruh_uchun import Guruh

# Echo bot
@dp.message_handler(Guruh(),commands='start')
async def bot_echo(message: types.Message):
    await message.answer(text='guruhga hush kelibsiz')




@dp.message_handler(Guruh(),content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
     ism  = message.new_chat_members[0].full_name
     await message.reply(text=f'Guruhga hush kelibsiz {ism}')

@dp.message_handler(Guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
     ism  = message.left_chat_member.full_name
     await message.reply(text=f'Guruhni tark etdi {ism}')

@dp.message_handler(Guruh(),text='salom',chat_id='5883029982')
async def bot_echo(message: types.Message):
     ism  = message.from_user.full_name
     user_id = message.from_user.id
     guruh_id = message.chat.id
     message_id = message.message_id

     await bot.delete_message(chat_id=guruh_id,message_id=message_id)
     await bot.send_message(chat_id=guruh_id,text="bunday soz taqiqlangan")

