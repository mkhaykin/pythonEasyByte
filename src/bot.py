import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from settings import settings

dp = Dispatcher()
logger = logging.getLogger(__name__)


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        text="Hi! Enter '/report'",
    )


@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """
    logger.info(
        f"Request help by user id: {str(message.from_user and message.from_user.id)}"
    )

    await message.answer(
        text="help info",
    )


@dp.message(Command("convert"))
async def convert_handler(message: types.Message):
    """
    This handler receives messages with `/convert` command
    """
    logger.info(
        f"Request convert by user id: {str(message.from_user and message.from_user.id)}"
    )

    await message.answer(
        text="convert",
    )


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def bot_loop() -> None:
    bot = Bot(
        token=settings.TG_BOT_TOKEN,
        parse_mode=ParseMode.HTML,
    )
    logger.info("Bot loop starting ...")
    await dp.start_polling(bot)
    logger.info("Bot loop finished.")
