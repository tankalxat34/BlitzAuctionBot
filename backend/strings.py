"""
Обработчик строк для чат-бота

(c) tankalxat34 - 2022
"""

def replaceAll(string: str, mask: dict) -> str:
    """
    Заменяет ключи на их значения
    
    :param string - строка, в которой нужно произвести замену
    :param mask - словарь, который используется для замены
    """
    result = string
    for k in mask.keys():
        result = result.replace(k, str(mask[k]))
    return result


if __name__ == "__main__":
    print(replaceAll("Привет, %username%, как настроение? This is %user_id%", {"%username%": "tankalxat34", "%user_id%": 125435}))
