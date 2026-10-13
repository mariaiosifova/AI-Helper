import pandas as pd

class ResponseValidator():

    def __init__(self):
        pass

    def is_safe(self, code_text: str):

        dangerous_strokes_array = ["import os", "import sys", "import shutil", "import requests", "open("]

        have_dangerous_stroke = [i in code_text for i in dangerous_strokes_array]

        if True in have_dangerous_stroke:
            return False

        return True

    def execute_code(self, dataframe: pd.DataFrame, code_text: str):

        local_context = {"df": dataframe}
        try:
            exec(code_text, {}, local_context)
        except Exception as e:
            return f'Ошибка выполнения {e}'

        result = local_context.get("result")

        return result