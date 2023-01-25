import random

from vocabularies.ru import RU


def get_bot_choice() -> str:
    return random.choice(['rock', 'scissors', 'paper'])


def _normalize_user_answer(answer: str) -> str:
    for key in RU:
        if RU[key] == answer:
            return key


def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice: str = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'
