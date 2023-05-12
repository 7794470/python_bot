from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from random import randrange


from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help')).insert(KeyboardButton('/orange')).add(KeyboardButton('/random'))

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка фото</em>"""


async def on_startup(_):
    print('Я запустился')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Добро пожаловать!',
                           reply_markup=kb)


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, parse_mode='HTML',
                           text=HELP_COMMAND)


@dp.message_handler(commands=['description'])
async def command_desc(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Our bot for LoL')
# @dp.message_handler()
# async def send_cat(message: types.Message):
#     if message.text == '❤️':
#         await bot.send_sticker(chat_id=message.from_user.id,
#                                sticker='CAACAgIAAxkBAAEI665kWjrUUckmubMRIuOK81ds_By2OQACSCIAAtai2Egvtr9hU9kdcC8E')


@dp.message_handler(commands=['orange'])
async def send_orange(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Ambersweet_oranges.jpg/800px-Ambersweet_oranges.jpg')


@dp.message_handler(['random'])
async def send_random (message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=randrange(1, 100),
                            longitude=randrange(1, 100))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
