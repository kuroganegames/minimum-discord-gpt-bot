# coding:utf-8

import openai

class GPT:
    def __init__(self, openai_key):
        openai.api_key = openai_key


    def run_gpt(self, messages, i_max_tokens=500, model="gpt-3.5-turbo"):
        completion_params = {
            "model": model,
            "messages": messages,
            "max_tokens": i_max_tokens
        }

        completion = openai.ChatCompletion.create(**completion_params)
        return completion.choices[0].message.to_dict()