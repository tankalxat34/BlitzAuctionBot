"""
Парсер файла `.env`

(c) tankalxat34 - 2022
"""
import os
import pathlib

def removeSpaces(string: str) -> str:
    """Обрезает пробелы и лишние символы в строке"""
    return string.strip()


class DotEnv:
    def __init__(self, path: str = pathlib.Path(os.getcwd(), ".env")):
        """
        Класс для работы с файлом `.env`
        
        :param path - путь к файлу `.env`
        """
        with open(path, "r", encoding="UTF-8") as file:
            lines = [value.split("#")[0].strip() for value in [value for value in [value for value in set(map(removeSpaces, file.readlines())) if value] if value[0] != "#"]]

        for line in lines:
            # создание атрибутов для экземпляра класса
            self[line.split("=")[0]] = line.split("=")[1].replace('"', '')

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __str__(self) -> str:
        return f"DotEnv({self.__dict__})"


if __name__ == "__main__":
    _env = DotEnv()
    print(_env)
    print(_env.TOKEN)