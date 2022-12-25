"""
Парсинг .env
"""
import os
import pathlib

def removeSpaces(string: str) -> str:
    """Обрезает пробелы и лишние символы в строке"""
    return string.strip()


def config(path: str = pathlib.Path(os.getcwd(), ".env")) -> None:
    """Загружает все переменные из .env в глобальную область видимости"""
    with open(path, "r", encoding="UTF-8") as file:
        content = [value.split("#")[0].strip() for value in [value for value in [value for value in set(map(removeSpaces, file.readlines())) if value] if value[0] != "#"]]
    
    for line in content:
        exec(f"global {line.split('=')[0]}\n{line}")

    return True


class DotEnv:
    def __init__(self, path: str = pathlib.Path(os.getcwd(), ".env")) -> None:
        self.path = path

        with open(path, "r", encoding="UTF-8") as file:
            self.lines = [value.split("#")[0].strip() for value in [value for value in [value for value in set(map(removeSpaces, file.readlines())) if value] if value[0] != "#"]]

        self.dictionary = dict()

        for line in self.lines:
            self.dictionary[line.split("=")[0]] = line.split("=")[1]
            self[line.split("=")[0]] = line.split("=")[1].replace('"', '')

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self) -> str:
        return f"DotEnv({self.dictionary})"

if __name__ == "__main__":
    _env = DotEnv()
    print(_env)
    print(_env.TOKEN)
    print(_env.VAR_INT)

