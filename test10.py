from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я запустился')

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='YouTube',
                           url='https://www.youtube.com/@Vestnik_Buri')
ib2 = InlineKeyboardButton(text='Google',
                           url='google.com')
ikb.add(ib1).add(ib2)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
b = KeyboardButton(text="/links")
kb.add(b)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Welcome to main menu',
                         reply_markup=kb)


@dp.message_handler(commands=['links'])
async def links_command(message: types.Message):
    await message.answer(text='Выберите опцию ...',
                         reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
