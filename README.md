## Инструкция по сборке проекта и запуску игры:

1) Установка зависимостей: make install
2) Установка всех необходимых пакетов: make package-install
3) Запуск игры: make project
4) Сборка проекта: make build
5) Публикация: make publish
6) Проверка кода в соответствии с ruff: make lint

## Команды в игре:

1.1) **go <direction>** Перейти в направлении (north/south/east/west)
1.2) **<direction>**    Перейти в направлении (north/south/east/west)
2)   **look**	   Осмотреть текущую комнату
3)   **take <item>**	   Поднять предмет
4)   **use <item>**	   Использовать предмет из инвентаря
5)   **inventory**	   Показать инвентарь
6)   **solve**          Попытаться решить загадку в комнате
7)   **quit или exit**  Выйти из игры
8)   **help**           Показать список команд

## Как победить?:

Добраться до комнаты treasure_room и открыть сундук помощью:
1) С помощью ключа (предмет treasure_key)
2) С помощью кода (команда solve)

## 🎥 Демонстрация asciinema

[![Demo](https://asciinema.org/a/uQTcHAqvCGZV8rzgDiwGK6jBm.svg)](https://asciinema.org/a/uQTcHAqvCGZV8rzgDiwGK6jBm)
