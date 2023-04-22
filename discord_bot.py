# coding:utf-8

import discord
import json
from gpt import GPT
from utils import text_cleaner

class DiscordBot:
    def __init__(self, token, l_remove, gpt, log_manager):
        self.token = token
        self.l_remove = l_remove
        self.gpt = gpt
        self.log_manager = log_manager
        
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.client = discord.Client(intents=self.intents)
        
        self.b_talk = False

        @self.client.event
        async def on_ready():
            print(f'We have logged in as {self.client.user}')

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return
            # print(message.content)
            command = message.content.lower()
            print("aaa", command)

            if command.startswith('$4'):
                s_mode = "gpt-4"
                b_ignore_log = False
                self.b_talk = True
                # s_text = self.gpt.run_gpt(text_cleaner(message.content, self.l_remove), model="gpt-4")
                # await message.channel.send(s_text["content"])

            elif command.startswith('$l'):
                s_mode = "gpt-3.5-turbo"
                b_ignore_log = True
                self.b_talk = True
                # s_text = self.gpt.run_gpt(text_cleaner(message.content, self.l_remove), i_max_tokens=500, ignore_log=True)
                # await message.channel.send(s_text["content"])

            elif command.startswith('$show'):
                self.b_talk = False
                log_data = self.log_manager.log_data["log"]
                await message.channel.send("\n".join(["{}.{}:{}".format(str(i_message//2), e_message["role"], e_message["content"][:11]) for i_message, e_message in enumerate(log_data)]))

            elif command.startswith('$del'):
                self.b_talk = False
                index_del = text_cleaner(message.content, self.l_remove)
                success = self.log_manager.delete_log_entry(index_del)
                if success:
                    await message.channel.send(f"Deleted log entry {index_del}")
                else:
                    await message.channel.send("Invalid index. Please specify a valid index.")

            elif command.startswith('$35') or command.startswith('$'):
                s_mode = "gpt-3.5-turbo"
                b_ignore_log = False
                self.b_talk = True
                # s_text = self.gpt.run_gpt(text_cleaner(message.content, self.l_remove), i_max_tokens=500)
                # await message.channel.send(s_text["content"])
                
            if self.b_talk:
                
                
                self.log_manager.add_logs(text_cleaner(message.content, self.l_remove))
                if b_ignore_log:
                    s_text = self.gpt.run_gpt([{"role": "user", "content": text_cleaner(message.content, self.l_remove)}], model=s_mode)
                else:
                    s_text = self.gpt.run_gpt(self.log_manager.log_data["log"], model=s_mode)
                self.log_manager.add_logs(s_text["content"], s_mode="assistant")
                await message.channel.send(s_text["content"])
                self.b_talk = False

            self.log_manager.clean_logs()

    def run(self):
        self.client.run(self.token)

