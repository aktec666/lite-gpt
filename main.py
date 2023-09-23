import discord
import random
import openai

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

openai.api_key = "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"

def gpt(s):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": s}
    ]
    )
    return completion.choices[0].message.content

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await message.reply(gpt(message.content), mention_author=True)

client.run("")