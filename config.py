from dataclasses import dataclass
from environs import Env  # type: ignore


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    bot: TgBot


def load_cfg(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    config = Config(TgBot(env('BOT_TOKEN')))
    return config
