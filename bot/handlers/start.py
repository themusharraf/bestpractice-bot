from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.reply(f"{message.from_user.full_name} welcome back!")