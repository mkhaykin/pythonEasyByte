from dataclasses import dataclass
from os import environ

import dotenv


@dataclass
class Settings:
    TG_BOT_TOKEN: str


dotenv.load_dotenv(
    dotenv_path=".env",
    override=False,
)

settings = Settings(
    TG_BOT_TOKEN=environ["TG_BOT_TOKEN"],
)
