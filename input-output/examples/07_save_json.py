"""
Пример 7: Сохранение данных в формате JSON

Демонстрирует:
- Преобразование словарей Python в JSON
- Запись JSON в файл
- Почему JSON полезен для структурированных данных
"""

import json

# Данные игрока как словарь Python
player = {
    "name": "Торин",
    "level": 5,
    "health": 150,
    "max_health": 150,
    "mana": 80,
    "experience": 1250,
    "inventory": ["меч", "щит", "зелье_здоровья", "зелье_здоровья"],
    "gold": 340,
    "completed_quests": ["Спасти деревню", "Победить короля гоблинов"]
}

print("Сохраняю данные игрока в player_save.json...")
print()

# Открываем файл для записи
file = open("player_save.json", "w", encoding="utf-8")

# json.dump() записывает объект Python как JSON в файл
# indent=2 делает его читаемым с красивым форматированием
# ensure_ascii=False позволяет сохранять кириллицу
json.dump(player, file, indent=2, ensure_ascii=False)

file.close()

print("Данные игрока сохранены!")
print()
print("Сохранённые данные:")
print("-" * 40)
print(f"Имя: {player['name']}")
print(f"Уровень: {player['level']}")
print(f"Здоровье: {player['health']}/{player['max_health']}")
print(f"Золото: {player['gold']}")
print(f"Инвентарь: {len(player['inventory'])} предметов")
print(f"Выполнено заданий: {len(player['completed_quests'])}")
print("-" * 40)
print()
print("Проверьте player_save.json в вашей директории!")
print("Он читаемый и структурированный.")
