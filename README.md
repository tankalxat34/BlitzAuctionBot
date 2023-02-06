# BlitzAuctionBot
Чат-бот Telegram для отслеживания информации о танках на новогоднем аукционе Tanks Blitz

Пример ответа бота на команду `/stat` или "Показать аукцион":

<img src="https://sun9-86.userapi.com/impg/1p6G10TJuRE8wcAEsTnGiJk78TDd2DG6L-jCMg/VtWIaul2uIs.jpg?size=1080x1830&quality=96&sign=2989f78e4a02706b6f1e86b5e767684f&type=album" width=400px>

<details>
<summary>Текст</summary>

```
💰Продается танков: 14
    Премиум танки: 12
    Коллекционные танки: 2
    Средняя цена танка: 9357.14

• СТГ (https://old.wotblitz.eu/ru/encyclopedia/vehicles/ussr/R146_STG) (СТ-8 🌍 прем)
    Танков осталось: 2964/3000
    Цена сейчас: 8000 золота
    Следующая цена: 7250 золота (через 21 часов)

• Т-44-85 (https://old.wotblitz.eu/ru/encyclopedia/vehicles/ussr/R98_T44_85) (СТ-7 🌍 прем)
    Танков осталось: 2956/3000
    Цена сейчас: 5000 золота
    Следующая цена: 4500 золота (через 21 часов)

• 121B (https://old.wotblitz.eu/ru/encyclopedia/vehicles/china/Ch25_121_mod_1971B) (СТ-10 🇨🇳 прем)
    Танков осталось: 2916/3000
    Цена сейчас: 15000 золота
    Следующая цена: 14000 золота (через 21 часов)

• AMX Canon d'assaut 105 (https://old.wotblitz.eu/ru/encyclopedia/vehicles/france/F89_Canon_dassaut_105) (ПТ-8 🇫🇷 прем)
    Танков осталось: 2899/3000
    Цена сейчас: 8500 золота
    Следующая цена: 7750 золота (через 21 часов)

• Centurion Mk. 5/1 RAAC (https://old.wotblitz.eu/ru/encyclopedia/vehicles/uk/GB94_Centurion_Mk5-1_RAAC) (СТ-8 🇬🇧 прем)
    Танков осталось: 2892/3000
    Цена сейчас: 8500 золота
    Следующая цена: 8000 золота (через 21 часов)

• Škoda T 27 (https://old.wotblitz.eu/ru/encyclopedia/vehicles/european/Cz13_T-27) (СТ-8 🇪🇺 прем)
    Танков осталось: 2833/3000
    Цена сейчас: 9000 золота
    Следующая цена: 8500 золота (через 21 часов)

• Titan H-Nd (https://old.wotblitz.eu/ru/encyclopedia/vehicles/other/Oth28_Sturmfeur_HW) (ТТ-7 🏴 коллекционный)
    Танков осталось: 2814/3000
    Цена сейчас: 7500 золота
    Следующая цена: 7000 золота (через 21 часов)

• Krupp-Steyr Waffenträger (https://old.wotblitz.eu/ru/encyclopedia/vehicles/germany/G109_Steyr_WT) (ПТ-7 🇩🇪 прем)
    Танков осталось: 2807/3000
    Цена сейчас: 6000 золота
    Следующая цена: 5500 золота (через 21 часов)

• Titan-54d (https://old.wotblitz.eu/ru/encyclopedia/vehicles/other/Oth30_T54MS) (СТ-8 🏴 прем)
    Танков осталось: 2800/3000
    Цена сейчас: 9000 золота
    Следующая цена: 8500 золота (через 21 часов)

• EMIL 1951 (https://old.wotblitz.eu/ru/encyclopedia/vehicles/european/S25_EMIL_51) (ТТ-8 🇪🇺 прем)
    Танков осталось: 2782/3000
    Цена сейчас: 9500 золота
    Следующая цена: 8800 золота (через 21 часов)

• Ликан (https://old.wotblitz.eu/ru/encyclopedia/vehicles/other/Oth23_Werewolf) (ТТ-7 🏴 прем)
    Танков осталось: 2769/3000
    Цена сейчас: 7500 золота
    Следующая цена: 6500 золота (через 21 часов)

• Kampfpanzer 70 (https://old.wotblitz.eu/ru/encyclopedia/vehicles/germany/G_KpfPz_70) (ТТ-9 🇩🇪 прем)
    Танков осталось: 2688/3000
    Цена сейчас: 10000 золота
    Следующая цена: 9000 золота (через 21 часов)

• Progetto M35 mod. 46 (https://old.wotblitz.eu/ru/encyclopedia/vehicles/european/It13_Progetto_M35_mod_46) (СТ-8 🇪🇺 прем)
    Танков осталось: 2324/3000
    Цена сейчас: 10000 золота
    Следующая цена: 9250 золота (через 21 часов)

• VK 90.01 (P) (https://old.wotblitz.eu/ru/encyclopedia/vehicles/germany/G_VK9001P) (ТТ-10 🇩🇪 коллекционный)
    Танков осталось: 0/3000
    Цена сейчас: 17500 золота
    Следующая цена: 16500 золота (через 21 часов)
```
</details>


# Использование и разработка

1. Клонируйте репозиторий: `https://github.com/tankalxat34/BlitzAuctionBot.git`
2. Установите зависимости: `pip install -r requirements.txt`
3. Создайте файл `.env` в клонированном репозитории. 
    - Введите в него переменную `TOKEN` с полученным от бота-отца токеном.
    - Введите переменную `PARSE_MODE="html"`.
4. Запустите файл `main.py`.
