import os
import pandas as pd

class TableLoader():

    def __init__(self, file_path: str):

        self.file_path = file_path
        self.df = None

    def load_data(self):

        if not os.path.exists(self.file_path):
            raise FileNotFoundError("Некорректный путь или файла не существует")

        path_extesion = os.path.splitext(self.file_path)[1].lower()

        if path_extesion == ".csv":
            self.df = pd.read_csv(self.file_path)
        elif path_extesion == ".xlsx":
            self.df = pd.read_excel(self.file_path)
        else:
            raise ValueError("Некорректное расширение файла")

    def get_table_schema(self):

        if self.df is None:
            raise ValueError("Пустой файл, проверьте данные")
        
        df_main_info = str(self.df.dtypes)
        df_header = self.df.head(3).to_string()
        prompt_structure_stroke = f'Here is the main info about user dataframe structure: {df_main_info}.\
                                    Here is example of how datframe looks like(first 3 strokes): {df_header}'
        return prompt_structure_stroke

        