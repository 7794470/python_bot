from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Good Channel 1',
                           url='https://www.youtube.com/@Vestnik_Buri')
ib2 = InlineKeyboardButton(text='Good Channel 2',
                           url='https://www.youtube.com/@jakobimax')
ikb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Правильные каналы!',
                           reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
