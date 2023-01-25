from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from vocabularies.ru import RU

yesno_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True
)

yes_btn: KeyboardButton = KeyboardButton(RU['yes_button'])
no_btn: KeyboardButton = KeyboardButton(RU['no_button'])

yesno_kb.add(yes_btn, no_btn)

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)

rock_btn: KeyboardButton = KeyboardButton(RU['rock'])
scissors_btn: KeyboardButton = KeyboardButton(RU['scissors'])
paper_btn: KeyboardButton = KeyboardButton(RU['paper'])

game_kb.add(rock_btn).add(scissors_btn).add(paper_btn)
