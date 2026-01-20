"""
Пример 9: Полный цикл персистентности JSON

Демонстрирует:
- Загрузку данных, если они существуют
- Использование данных по умолчанию, если их нет
- Изменение данных
- Сохранение обратно в файл
"""

import json

SAVE_FILE = "game_state.json"


def load_game_state():
    """
    Загружает состояние игры из файла.
    Если файл не существует, возвращает состояние по умолчанию.
    """
    try:
        file = open(SAVE_FILE, "r", encoding="utf-8")
        state = json.load(file)
        file.close()
        print("Состояние игры загружено из файла.")
        return state
    except FileNotFoundError:
        print("Файл сохранения не найден. Начинаю новую игру.")
        # Возвращаем состояние по умолчанию для новой игры
        return {
            "player_name": "Неизвестный",
            "gold": 0,
            "level": 1,
            "sessions": 0
        }


def save_game_state(state):
    """Сохраняет состояние игры в файл."""
    file = open(SAVE_FILE, "w", encoding="utf-8")
    json.dump(state, file, indent=2, ensure_ascii=False)
    file.close()
    print("Состояние игры сохранено.")


# Основная программа
print("=" * 40)
print("ДЕМО ПЕРСИСТЕНТНОЙ ИГРЫ")
print("=" * 40)
print()

# Загружаем существующее состояние или создаём новое
game = load_game_state()

# Увеличиваем счётчик сессий
game["sessions"] += 1

print()
print(f"Добро пожаловать, {game['player_name']}!")
print(f"Уровень: {game['level']}")
print(f"Золото: {game['gold']}")
print(f"Это сессия #{game['sessions']}")
print()

# Получаем имя игрока, если это первый запуск
if game["player_name"] == "Неизвестный":
    name = input("Введите имя вашего персонажа: ")
    game["player_name"] = name
    print()

# Симулируем игровой процесс
print("Вы исследовали лес и нашли сокровище!")
gold_found = 25
game["gold"] += gold_found
print(f"Вы нашли {gold_found} золота!")
print(f"Всего золота: {game['gold']}")
print()

# Сохраняем обновлённое состояние
save_game_state(game)

print()
print("Запустите эту программу несколько раз, чтобы увидеть, как работает сохранение данных!")
print(f"Ваш прогресс сохраняется в файле {SAVE_FILE}")
