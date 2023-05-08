from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот был успешно запущен')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer('<em>Hi. Welcome to our Bot</em>', parse_mode="HTML")


@dp.message_handler(commands=['give'])
async def command_start(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEI6T5kWWL6eWdnR9abV08azkaH0lvUpQACfSkAAjU82EgKSbMCS1IxXC8E")
    await message.delete()


@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text + '🇷🇺')


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
