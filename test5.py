from aiogram import Bot, Dispatcher, types, executor


from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>показывает список команд</em>
<b>/give</b> - <em>отправляет кота</em>
<b>/start</b> - <em>запускает бота</em>"""


async def on_startup(_):
    print('я запустился')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML')
    await message.delete()


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
# @dp.message_handler()
# async def count(message: types.Message):
#     await message.answer(text=str(message.text.count('😺')))
# @dp.message_handler(commands='katz')
# async def send_sticker(message: types.Message):
#     await message.answer('Смотри на тебя похож- кошак недовольный 😺️')
#     await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEI665kWjrUUckmubMRIuOK81ds_By2OQACSCIAAtai2Egvtr9hU9kdcC8E')
#     await message.delete()
#
#
# @dp.message_handler()
# async def send_sticker(message: types.Message):
#     if message.text == "❤️":
#         await message.answer('🖤')
#         await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
