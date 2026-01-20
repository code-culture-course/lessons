"""
Пример 8: Загрузка данных из JSON

Демонстрирует:
- Чтение JSON из файла
- Преобразование JSON обратно в объекты Python
- Работу с загруженными данными
"""

import json

print("Загружаю данные игрока из player_save.json...")
print()

try:
    # Открываем файл для чтения
    file = open("player_save.json", "r", encoding="utf-8")
    
    # json.load() читает JSON и преобразует его в объекты Python
    player = json.load(file)
    
    file.close()
    
    print("Данные игрока успешно загружены!")
    print("=" * 40)
    print(f"С возвращением, {player['name']}!")
    print("=" * 40)
    print(f"Уровень: {player['level']}")
    print(f"Здоровье: {player['health']}/{player['max_health']}")
    print(f"Мана: {player['mana']}")
    print(f"Опыт: {player['experience']}")
    print(f"Золото: {player['gold']}")
    print()
    print("Инвентарь:")
    for item in player['inventory']:
        print(f"  - {item}")
    print()
    print("Выполненные задания:")
    for quest in player['completed_quests']:
        print(f"  ✓ {quest}")
    print("=" * 40)
    
except FileNotFoundError:
    print("Ошибка: player_save.json не найден!")
    print("Сначала запустите 07_save_json.py, чтобы создать файл сохранения.")
except json.JSONDecodeError:
    print("Ошибка: Файл существует, но содержит некорректный JSON.")
