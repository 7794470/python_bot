from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_upper(message: types.Message):
    if len(message.text.split()) > 1:
        await message.answer(text=message.text.upper())


if __name__ == "__main__":
    executor.start_polling(dp)
