import os
from dotenv import load_dotenv 
import urllib3
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

from gigachat import GigaChat

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class AgentEngine():

    def __init__(self):
        pass
    
    def generate_code(self, user_query: str, prompt_structure_stroke: str):
        load_dotenv()
        client = GigaChat(
            base_url="https://api.giga.chat/v1",
            credentials=f'{os.getenv("AUTHORIZATION_KEY")}',
            scope="GIGACHAT_API_PERS",
            verify_ssl_certs=False,
        )
        PROMPT = f'Строгое условие: возвращать только чистый код на Python/Pandas без какой - либо текстовой информации. \
                   Сохраняй итоговую информацию в переменную с именем result. Информация о входных данных: {prompt_structure_stroke}. \
                   Ты должен сделать с данными из этой таблицы: {user_query}\
                   Твой ответ должен быть строго в таком формате: ```Python\n (код)\n```'

        chat = Chat(
            model="GigaChat-2-Pro",
            messages=[Messages(role=MessagesRole.USER, content=PROMPT)],
        )

        response = client.chat(chat).choices[0].message.content
        print(response)
        if response[:3] == '```':
            response = response[9:]
            response = response[:-3]

        return str(response)