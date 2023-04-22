# coding:utf-8

from discord_bot import DiscordBot
from gpt import GPT
from utils import text_cleaner
from log_manager import LogManager

if __name__ == "__main__":
    with open("token", "r", encoding="utf-8") as reader:
        discord_key = reader.read()
    with open("key", "r", encoding="utf-8") as reader:
        openai_key = reader.read()

    remove_list = [
        '$L\u3000',
        '$L ',
        '$L',
        '$del\u3000',
        '$del ',
        '$del',
        '$DEL\u3000',
        '$DEL ',
        '$DEL',
        '$SHOW\u3000',
        '$SHOW ',
        '$SHOW',
        '$show\u3000',
        '$show ',
        '$show',
        '$4',
        '$35',
        '$4\u3000',
        '$35\u3000',
        '$4 ',
        '$35 ',
        '$4\n',
        '$35\n',
        '$\u3000',
        '$ ',
        '$\n',
        ]
    dir_log = r"test_log_3.json"

    gpt = GPT(openai_key)
    log_manager = LogManager(dir_log)
    discord_bot = DiscordBot(discord_key, remove_list, gpt, log_manager)

    discord_bot.run()
