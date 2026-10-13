import os
from dotenv import load_dotenv 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()
from modules.engine import AgentEngine
from modules.loader import TableLoader
from modules.validator import ResponseValidator

def execute_program():
    path_to_file = f"{os.getenv("PATH_TO_FILE")}"
    loader = TableLoader(path_to_file)
    loader.load_data()
    prompt_structure_stroke = loader.get_table_schema()

    agent = AgentEngine()
    responer = ResponseValidator()

    while True:
        question = input("Задавайте ваш вопрос. Для выхода введите 'выход'")

        if question.lower() == 'выход':
            break
        code_text = agent.generate_code(question, prompt_structure_stroke)

        
        if responer.is_safe(code_text):
            result = responer.execute_code(loader.df, code_text)
            print(result)
        else:
            raise Exception("Чет не то")


if __name__ == '__main__':
    execute_program()