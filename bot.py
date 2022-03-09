from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
token = input("Enter your token: ")
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(Command('start'))
async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id, "<b>Hello, I'm Obhavo Bot!</b>")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)