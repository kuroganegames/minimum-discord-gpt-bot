# minimum-discord-gpt-bot

This is very simple chatbot.

This chatbot is integrated with Discord and allows users to interact by **specific commands(below)**.


Minimal code for a **small community** to use a ChatGPT-style chatbot that uses GPT models to generate responses. 


Multiple inputs at the same time and advanced Log functions(e.g. langchain) are **NOT** supported.
This can cause problems if used by a large community.

The chatbot supports **GPT-4** and **GPT-3.5-turbo** models.
Of course, you have to get **your own API key.**

Logs are limited to **4 chat** or **3200 characters**(not token).
 The logs are stored without any processing at all. 
Old logs will be deleted.

Instead, you can easily run the bot on **your PC** with python installed. You don't need to rent a server.

This code **never do heavy processing**, only accesses openAI and Discord API.

## Requirements

- Python 3.8 or higher
- `discord.py`
- `openai`
- OpenAI API key for GPT-3.5-turbo and GPT-4

## Installation

1. Install the required packages:

```
pip install -U discord.py
pip install openai
```

[discord.py · PyPI](https://pypi.org/project/discord.py/)

[Libraries - OpenAI API](https://platform.openai.com/docs/libraries)

1. Set up your API keys:

Create a file named `token` in the project directory and paste your Discord bot token.

Create another file named `key` in the project directory and paste your OpenAI API key.

## Usage

To start the chatbot, run the `chatbot_v_main.bat` file or execute the following command:

```
python main.py
```

## Commands

- `$ [text]`: Generate a response using the GPT-3.5-turbo model.
- `$35 [message]`: Generate a response using the GPT-3.5-turbo model.
- `$4 [message]`: Generate a response using the GPT-4 model.
- `$L [message]`: Generate a response using the GPT-3.5-turbo model and **ignore logs.**
- `$show`: Show the log of recent messages.
- `$del [index]`: Delete a log entry by index.

## Components

- `chatbot_v_main.bat`: Batch script to start the chatbot.
- `main.py`: Main script to initialize and run the chatbot.
- `log_manager.py`: A utility class to manage logs.
- `utils.py`: A utility script for text cleaning.
- `discord_bot.py`: The main chatbot class that handles the Discord bot and its events.

## Note

This project uses GPT-4 and GPT-3.5-turbo models, which are not free to use. 
Make sure to have access to these models through OpenAI's API.

## License

This project is licensed under the MIT License.
