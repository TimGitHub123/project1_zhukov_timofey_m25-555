## Инструкция по сборке проекта и запуску игры:

1) Установка зависимостей: make install
2) Установка всех необходимых пакетов: make package-install
3) Запуск игры: make project
4) Сборка проекта: make build
5) Публикация: make publish
6) Проверка кода в соответствии с ruff: make lint

## Команды в игре:

**go <direction>** Перейти в направлении (north/south/east/west)
**<direction>**    Перейти в направлении (north/south/east/west)
**look**	   Осмотреть текущую комнату
**take <item>**	   Поднять предмет
**use <item>**	   Использовать предмет из инвентаря
**inventory**	   Показать инвентарь
**solve**          Попытаться решить загадку в комнате
**quit или exit**  Выйти из игры
**help**           Показать список команд

## Как победить?:

Добраться до комнаты treasure_room и открыть сундук помощью:
1) С помощью ключа (предмет treasure_key)
2) С помощью кода (команда solve)

## 🎥 Демонстрация asciinema

[![Demo](https://asciinema.org/a/uQTcHAqvCGZV8rzgDiwGK6jBm.svg)](https://asciinema.org/a/uQTcHAqvCGZV8rzgDiwGK6jBm)
