"""
Функционал чат-бота реализован здесь

(c) tankalxat34 - 2022
"""

import requests
import json
from datetime import datetime

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

with open("./masks.json", "r", encoding="UTF-8") as file:
    MASKS = json.loads(file.read())


def humanizeTimeDiff(time1: int, time2: int) -> str:
    diff = round(abs(time1 - time2))
    if diff >= 24 * 60 * 60:
        return f"{round(diff / (24 * 60 * 60))} дней"
    if diff >= 60 * 60:
        return f"{round(diff / (60 * 60))} часов"
    if diff >= 60:
        return f"{round(diff / (60))} минут"
    else:
        return f"{diff} секунд"
    


class Auction:
    def __init__(self) -> None:
        self.url_api = "https://tanksblitz.ru/ru/api/events/items/auction/?page_size=50&type[]=vehicle&saleable=true"
        self.url_user = "https://tanksblitz.ru/ru/auction/"

    def get(self) -> dict:
        self.response = requests.get(self.url_api, headers=HEADERS)
        return self.response.json()
    
    def str_available(self) -> str:
        msg = ""
        results = self.get()["results"]

        for tank in results:
            if tank["available"]:
                msg += (f'• *{tank["entity"]["user_string"]}* ({MASKS[tank["entity"]["type_slug"]]}-{tank["entity"]["level"]})\n    Танков осталось: *{tank["current_count"]}*/{tank["initial_count"]}\n    Цена сейчас: _{tank["price"]["value"]} {MASKS[tank["price"]["currency"]["title"].lower()]}_\n    Следующая цена: _{tank["next_price"]["value"]} {MASKS[tank["next_price"]["currency"]["title"].lower()]}_\n    Цена упадет {datetime.fromtimestamp(tank["next_price_timestamp"])} (через {humanizeTimeDiff(datetime.timestamp(datetime.now()), tank["next_price_timestamp"])})\n    Будет выведен из продажи {tank["available_before"]}') + "\n\n"

        return msg


if __name__ == "__main__":
    auction = Auction()
    print(auction.str_available())