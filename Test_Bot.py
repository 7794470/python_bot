from aiogram import Bot, Dispatcher, executor, types

# бот - сервер, который взаимодействует в API телеграм
TOKEN_API = "5933700681:AAFY7GyCeoVKanLZAPojPUrgvUPMXqlt_xw"  # токен testnip_bot

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)  # написать сообщение text


if __name__ == '__main__':
    executor.start_polling(dp)
