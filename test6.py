from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


HELP_COMMAND = """
<b>/start</b> - <em>начало нашей работы</em>
<b>/help</b> - <em>помощь</em>
<b>/картинка</b> - <em>картинка</em>"""


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # await bot.send_message(chat_id=message.chat.id,
    #                        text='HELLO!!!')
    # await bot.send_message(chat_id=message.from_user.id,
    #                        text='HELLO!!!')
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['картинка'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://kalix.club/uploads/posts/2022-12/1671531548_kalix-club-p-oboi-na-telefon-smeshnie-koti-krasivo-1.jpg')
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=41.296018,
                            longitude=69.280788)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
