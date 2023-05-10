import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, \
    InlineKeyboardMarkup, LabeledPrice
from filters.shaxsiy_uchun import Shaxsiy
from loader import dp, obyekt, bot
from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.oziq_ovqat_uchun import oziq_ovqat_buttons

from keyboards.inline.tillar_uchun import tillar_buttons
@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    msg_id = message.message_id
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    username = message.from_user.username
    user_id = message.from_user.id
    date = datetime.datetime.now()
    try:
        obyekt.user_qoshish(ism=ism,tg_id=user_id,fam=familya,username=username,date=date)

    except Exception:
        pass
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)

    await bot.delete_message(chat_id=user_id,message_id=msg_id)



@dp.message_handler(commands='reklama', chat_id='5883029982')
async def bot_start(message: types.Message):
    userlar = obyekt.select_barcha_foydalanuvchilar()
    print(userlar)

    for  user in userlar:
        await bot.send_message(chat_id=user[4],text="Bu reklama !!!")


@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum {xabar.from_user.full_name} botga xush kelibsiz  !",
                               reply_markup=menu_buttons)

@dp.message_handler( text='Ortga')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Maxsulotni tanlang", reply_markup=menu_buttons)


menular = obyekt.select_barcha_menular()

@dp.message_handler( text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    print(text)
    tur = obyekt.select_type(nomi=text)
    maxsulotlar = obyekt.select_maxsulotlar(tur_id=tur[0])
    j = 0
    index = 0
    keys = []
    for menu in maxsulotlar:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f'{menu[1]}', )])
        else:
            keys[index].append(KeyboardButton(text=f'{menu[1]}', ))
        j += 1

    keys.append([KeyboardButton(text='Ortga')])
    maxsulot_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Maxsulotni tanlang",reply_markup=maxsulot_buttons)



menular = obyekt.select_barcha_maxsulotlar()
print(menular,)
@dp.message_handler( text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    print(text)
    """(1, 'Osh', 'https://t.me/UstozShogird/25032', 20000, None, 'Taomlar')"""
    maxsulot = obyekt.select_maxsulot(nomi=text)
    max_id= maxsulot[0]
    max_nomi = maxsulot[1]
    max_narxi = maxsulot[3]
    max_rasmi = maxsulot[2]
    max_text = maxsulot[4]
    user_id = message.from_user.id
    malumot = f"Nomi : {max_nomi}\n" \
              f"Narxi : {max_narxi}\n" \
              f"Malumot :  {max_text}"

    await bot.send_photo(chat_id=user_id,photo=max_rasmi,caption=malumot,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Sotib olish",callback_data=f"buy {max_id}")
            ]
        ]))




@dp.callback_query_handler()
async def bot_start(xabar: CallbackQuery):
    malumot = xabar.data.split()
    max_id = malumot[1]
    msg_id = xabar.message.message_id
    """['buy', '1']"""
    if malumot[0]=='buy':

        max_id = malumot[1]
        maxsulot = obyekt.select_maxsulot(id=max_id)
        "(1, 'Osh', 'https://t.me/UstozShogird/26311', 14000, '', 1)"
        max_nomi = maxsulot[1]
        max_narxi = maxsulot[3]
        max_rasm = maxsulot[2]
        max_soni = 1
        ism  =xabar.from_user.full_name
        tg_id = xabar.from_user.id
        korzinka_maxsulot = obyekt.select_maxsulot_from_korzinka(tg_id=tg_id,nomi=max_nomi)
        print(korzinka_maxsulot)
        if korzinka_maxsulot:
            soni = korzinka_maxsulot[0]+1
            print(soni,'ddddddddd')
            obyekt.update_korzinka(tg_id=tg_id,nomi=max_nomi,son=soni)
        else:
            obyekt.add_to_korzinka(ism=ism,tg_id=tg_id,nomi=max_nomi,narxi=max_narxi,rasm=max_rasm,son=max_soni)
        print(maxsulot)
        await xabar.message.answer(f"Sotib olindi !",
                               )

    elif malumot[0]=="minus":
        print(malumot)
        msg_id = xabar.message.message_id
        max_id = int(malumot[1])
        maxsulot = obyekt.select_maxsulotlar_from_korzinka(id=max_id)[0]
        print(maxsulot)
        "(1, 'Osh', 'https://t.me/UstozShogird/26311', 14000, '', 1)"
        max_nomi = maxsulot[1]
        tg_id = xabar.from_user.id
        korzinka_maxsulot = obyekt.select_maxsulot_from_korzinka(tg_id=tg_id, nomi=max_nomi)
        if korzinka_maxsulot:
            soni = korzinka_maxsulot[0] - 1
            obyekt.update_korzinka(tg_id=tg_id, nomi=max_nomi, son=soni)
            await bot.edit_message_reply_markup(chat_id=tg_id,message_id=msg_id,reply_markup=InlineKeyboardMarkup(
               inline_keyboard=[
                   [
                       InlineKeyboardButton(text="-",callback_data=f"minus {max_id}"),
                       InlineKeyboardButton(text=f"{soni}" ,callback_data=f"num {max_id}"),
                       InlineKeyboardButton(text=f"+",callback_data=f"plus {max_id}")
                   ],
                   [
                       InlineKeyboardButton(text="Delete",callback_data=f"del {max_id}"),
                       InlineKeyboardButton(text="Xarid qilish",callback_data=f"shop {max_id}")
                   ]
               ]))

    elif malumot[0]=="plus":
        print(malumot)
        msg_id = xabar.message.message_id
        max_id = int(malumot[1])
        maxsulot = obyekt.select_maxsulotlar_from_korzinka(id=max_id)[0]
        print(maxsulot)
        "(1, 'Osh', 'https://t.me/UstozShogird/26311', 14000, '', 1)"
        max_nomi = maxsulot[1]
        tg_id = xabar.from_user.id
        korzinka_maxsulot = obyekt.select_maxsulot_from_korzinka(tg_id=tg_id, nomi=max_nomi)
        if korzinka_maxsulot:
            soni = korzinka_maxsulot[0] + 1
            obyekt.update_korzinka(tg_id=tg_id, nomi=max_nomi, son=soni)
            await bot.edit_message_reply_markup(chat_id=tg_id,message_id=msg_id,reply_markup=InlineKeyboardMarkup(
               inline_keyboard=[
                   [
                       InlineKeyboardButton(text="-",callback_data=f"minus {max_id}"),
                       InlineKeyboardButton(text=f"{soni}" ,callback_data=f"num {max_id}"),
                       InlineKeyboardButton(text=f"+",callback_data=f"plus {max_id}")
                   ],
                   [
                       InlineKeyboardButton(text="Delete",callback_data=f"del {max_id}"),
                       InlineKeyboardButton(text="Xarid qilish", callback_data=f"shop {max_id}")
                   ]
               ]))

    elif malumot[0]=='del':
        obyekt.delete_maxsulot_from_korzinka(id=max_id)
        await bot.delete_message(chat_id=xabar.from_user.id,message_id=msg_id)

    elif malumot[0] =='shop':
        maxsulot = obyekt.select_maxsulotlar_from_korzinka(id=max_id)[0]
        """ (3, 'Osh', 'https://t.me/UstozShogird/26311', 14000, 4, 5883029982, '.....') """
        max_id = maxsulot[0]
        max_nomi = maxsulot[1]
        max_narxi = maxsulot[3]
        max_soni = maxsulot[4]
        summa = int(max_narxi)*int(max_soni)*100
        user_id = xabar.from_user.id
        await bot.send_invoice(chat_id=user_id,title="Sotib olingan maxsulot",
                               provider_token='371317599:TEST:1679139695376',currency='UZS',
                               description="Sotib olindi",
                               payload='111',
                               prices=[LabeledPrice(max_nomi,summa,),])


@dp.message_handler(Shaxsiy(),text="Korzinka")
async def bot_start(message: types.Message):
   user_id = message.from_user.id
   tanlangan_maxsulotlar = obyekt.select_maxsulotlar_from_korzinka(tg_id=user_id)

   for maxsulot in tanlangan_maxsulotlar:
       """(3, 'Osh', 'https://t.me/UstozShogird/26311', 14000, 5, 5883029982, '.....')"""
       max_id = maxsulot[0]
       max_nomi = maxsulot[1]
       max_narxi = maxsulot[3]
       max_soni = maxsulot[4]
       max_rasm = maxsulot[2]
       await bot.send_photo(chat_id=user_id,photo=max_rasm,caption=f"Nomi : {max_nomi}\n"
                                                                   f"Narxi : {max_narxi}\n"
                                                                   f"Soni : {max_soni}\n"
        ,reply_markup=InlineKeyboardMarkup(
               inline_keyboard=[
                   [
                       InlineKeyboardButton(text="-",callback_data=f"minus {max_id}"),
                       InlineKeyboardButton(text=f"{max_soni}" ,callback_data=f"num {max_id}"),
                       InlineKeyboardButton(text=f"+",callback_data=f"plus {max_id}")
                   ],
                   [
                       InlineKeyboardButton(text="Delete",callback_data=f"del {max_id}"),
                       InlineKeyboardButton(text="Xarid qilish", callback_data=f"shop {max_id}")
                   ]
               ]))



































