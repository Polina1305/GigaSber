from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os
from langchain_gigachat import GigaChat  # Отдельный пакет для GigaChat
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache
from dotenv import load_dotenv
# Включаю кеш в памяти
set_llm_cache(InMemoryCache())
load_dotenv()
# Инициализация GigaChat
chat = GigaChat(
    credentials=os.getenv("GIGATOKEN"),
    verify_ssl_certs=False
)

messages = [
    SystemMessage(content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблему")
]

while True:
    user_input = input("User: ")

    if user_input.lower() == 'пока':
        print("Bot: До свидания! Было приятно пообщаться.")
        break

    messages.append(HumanMessage(content=user_input))

    try:
        res = chat.invoke(messages)
        messages.append(AIMessage(content=res.content))
        print(f"Bot: {res.content}")

    except Exception as e:
        print(f"Bot: Произошла ошибка: {str(e)}")
        break