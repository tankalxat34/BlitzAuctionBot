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
        self.url_api = "https://tanksblitz.ru/ru/api/events/items/auction/?page_size=99&type[]=vehicle&saleable=true"
        self.url_user = "https://tanksblitz.ru/ru/auction/"

    def get(self) -> dict:
        self.response = requests.get(self.url_api, headers=HEADERS)
        return self.response.json()
    
    def str_available(self) -> str:
        """
        Возвращает в строке информацию о продаваемой технике
        """
        res = self.get()
        results = res["results"]

        # сбор статистики по технике
        statistic_tanks = dict()
        for tank in results:
            if tank["available"]:
                try:
                    statistic_tanks["all_available_count"] += 1
                except Exception:
                    statistic_tanks["all_available_count"] = 1
                
                try:
                    statistic_tanks["average_price"] += tank["price"]["value"]
                except Exception:
                    statistic_tanks["average_price"] = tank["price"]["value"]

                if tank["entity"]["is_premium"] and tank["entity"]["is_collectible"] == False:
                    try:
                        statistic_tanks["count_premium"] += 1
                    except Exception:
                        statistic_tanks["count_premium"] = 1

                if tank["entity"]["is_collectible"]:
                    try:
                        statistic_tanks["count_collectible"] += 1
                    except Exception:
                        statistic_tanks["count_collectible"] = 1

        msg = ""
        msg += f"💰Продается танков: {statistic_tanks['all_available_count']}\n" + \
               f"    Премиум танки: {statistic_tanks['count_premium']}\n" + \
               f"    Коллекционные танки: {statistic_tanks['count_collectible']}\n" + \
               f"    Средняя цена танка: {round(statistic_tanks['average_price'] / statistic_tanks['all_available_count'], 2)}\n" + \
                "\n"

        for tank in results:
            if tank["available"]:
                # msg += (f'• <b>{tank["entity"]["user_string"]}</b> ({MASKS[tank["entity"]["type_slug"]]}-{tank["entity"]["level"]} {MASKS[tank["entity"]["nation"]]}{" коллекционный" if tank["entity"]["is_collectible"] else ""}{" прем" if tank["entity"]["is_premium"] and tank["entity"]["is_collectible"] == False else ""})\n    Танков осталось: {tank["current_count"]}/{tank["initial_count"]}\n    Цена сейчас: {tank["price"]["value"]} {MASKS[tank["price"]["currency"]["title"].lower()]}\n    Следующая цена: {tank["next_price"]["value"]} {MASKS[tank["next_price"]["currency"]["title"].lower()]} (через {humanizeTimeDiff(datetime.timestamp(datetime.now()), tank["next_price_timestamp"])})') + "\n\n"
                msg += (f'• <a href="https://old.wotblitz.eu/ru/encyclopedia/vehicles/{tank["entity"]["nation"]}/{tank["entity"]["name"]}">{tank["entity"]["user_string"]}</a> ({MASKS[tank["entity"]["type_slug"]]}-{tank["entity"]["level"]} {MASKS[tank["entity"]["nation"]]}{" коллекционный" if tank["entity"]["is_collectible"] else ""}{" прем" if tank["entity"]["is_premium"] and tank["entity"]["is_collectible"] == False else ""})\n    Танков осталось: {tank["current_count"]}/{tank["initial_count"]}\n    Цена сейчас: {tank["price"]["value"]} {MASKS[tank["price"]["currency"]["title"].lower()]}\n    Следующая цена: {tank["next_price"]["value"]} {MASKS[tank["next_price"]["currency"]["title"].lower()]} (через {humanizeTimeDiff(datetime.timestamp(datetime.now()), tank["next_price_timestamp"])})') + "\n\n"
                # msg += (f'• <a href="https://old.wotblitz.eu/ru/encyclopedia/vehicles/{tank["entity"]["nation"]}/{tank["entity"]["name"]}">{tank["entity"]["user_string"]}</a> ({MASKS[tank["entity"]["type_slug"]]}-{tank["entity"]["level"]} {MASKS[tank["entity"]["nation"]]}{" коллекционный" if tank["entity"]["is_collectible"] else ""}{" прем" if tank["entity"]["is_premium"] and tank["entity"]["is_collectible"] == False else ""})\n    <b>Танков осталось</b>: {tank["current_count"]}/{tank["initial_count"]}\n    <b>Цена сейчас</b>: {tank["price"]["value"]} {MASKS[tank["price"]["currency"]["title"].lower()]}\n    <b>Следующая цена</b>: {tank["next_price"]["value"]} {MASKS[tank["next_price"]["currency"]["title"].lower()]} (через {humanizeTimeDiff(datetime.timestamp(datetime.now()), tank["next_price_timestamp"])})') + "\n\n"

                # msg += (f'• *[{tank["entity"]["user_string"]}](https://old.wotblitz.eu/ru/encyclopedia/vehicles/{tank["entity"]["nation"]}/{tank["entity"]["name"]})* ({MASKS[tank["entity"]["type_slug"]]}-{tank["entity"]["level"]} {MASKS[tank["entity"]["nation"]]}{" коллекционный" if tank["entity"]["is_collectible"] else ""}{" прем" if tank["entity"]["is_premium"] and tank["entity"]["is_collectible"] == False else ""})\n    Танков осталось: *{tank["current_count"]}*/{tank["initial_count"]}\n    Цена сейчас: _{tank["price"]["value"]} {MASKS[tank["price"]["currency"]["title"].lower()]}_\n    Следующая цена: _{tank["next_price"]["value"]} {MASKS[tank["next_price"]["currency"]["title"].lower()]}_ (через {humanizeTimeDiff(datetime.timestamp(datetime.now()), tank["next_price_timestamp"])})') + "\n\n"
                # msg += (f'• *[{tank["entity"]["user_string"]}](https://old.wotblitz.eu/ru/encyclopedia/vehicles/{tank["entity"]["nation"]}/{tank["entity"]["name"]})* ({MASKS[tank["entity"]["type_slug"]]}-{tank["entity"]["level"]} {MASKS[tank["entity"]["nation"]]}{" коллекционный" if tank["entity"]["is_collectible"] else ""}{" прем" if tank["entity"]["is_premium"] and tank["entity"]["is_collectible"] == False else ""})\n    Танков осталось: *{tank["current_count"]}*/{tank["initial_count"]}\n    Цена сейчас: _{tank["price"]["value"]} {MASKS[tank["price"]["currency"]["title"].lower()]}_\n    Следующая цена: _{tank["next_price"]["value"]} {MASKS[tank["next_price"]["currency"]["title"].lower()]}_ (через {humanizeTimeDiff(datetime.timestamp(datetime.now()), tank["next_price_timestamp"])})') + "\n\n"

        return msg


if __name__ == "__main__":
    auction = Auction()
    print(auction.str_available())