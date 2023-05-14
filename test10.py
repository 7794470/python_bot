from aiogram import Bot, Dispatcher, types, executor

from config import TOKEN_API

from keyboard import kb, ikb

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я запустился')


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
