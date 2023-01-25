from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from vocabularies.ru import RU
from keyboards.keyboards import yesno_kb, game_kb
from services.services import get_bot_choice, get_winner


async def process_start_command(message: Message):
    await message.answer(RU['/start'], reply_markup=yesno_kb)


async def process_help_command(message: Message):
    await message.answer(RU['/help'], reply_markup=yesno_kb)


async def process_yes_answer(message: Message):
    await message.answer(RU['yes'], reply_markup=game_kb)


async def process_no_answer(message: Message):
    await message.answer(RU['no'])


async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(f'{RU["bot_choice"]} - {RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(RU[winner], reply_markup=yesno_kb)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_yes_answer, text=RU['yes_button'])
    dp.register_message_handler(process_no_answer, text=RU['no_button'])
    dp.register_message_handler(process_game_button, Text(equals=[
        RU['rock'],
        RU['paper'],
        RU['scissors']
    ]))
    dp.register_message_handler(process_start_command, commands='start')
