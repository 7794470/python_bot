from aiogram import Bot, Dispatcher, types, executor


from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка фото</em>"""


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=HELP_COMMAND, parse_mode='HTML')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="Добро пожаловать в наш бот", parse_mode='HTML')


@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="Наш бот умеет отправлять фотографии", parse_mode='HTML')


@dp.message_handler(commands=['photo'])
async def image_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://avatars.mds.yandex.net/i?id=21b84b5bebb921b22572f7390bf0a91471120fbd-7546644-images-thumbs&n=13')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
