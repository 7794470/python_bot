from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True)
b1 = KeyboardButton('/Дамир')
b2 = KeyboardButton('/Булат')
b3 = KeyboardButton('/Манул')
kb.add(b1).insert(b2).add(b3)

HELP_COMMAND = """
<b>/Дамир</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/Булат</b> - <em>описание бота</em>
<b>/Манул</b> - <em>отправка фото</em>"""


@dp.message_handler(commands=['Дамир'])
async def help_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://opis-cdn.tinkoffjournal.ru/mercury/15fe1148.ny5qcgc')
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="Добро пожаловать в Кото-бот", parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['Булат'])
async def image_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://krasivosti.pro/uploads/posts/2022-01/1641457358_31-krasivosti-pro-p-samii-zloi-kot-krasivo-foto-35.jpg')
    await message.delete()


@dp.message_handler(commands=['Манул'])
async def image_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://memepedia.ru/wp-content/uploads/2017/04/%D0%BC%D0%B0%D0%BD%D1%83%D0%BB.jpg')
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
