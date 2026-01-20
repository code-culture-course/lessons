"""
Пример 5: Чтение из файла

Демонстрирует:
- Открытие файла для чтения
- Чтение всего содержимого файла
- Обработка случая когда файл не существует
- Построчное чтение
"""

print("Попытка прочитать game_log.txt...")
print()

# Сначала, проверить существует ли файл, попытавшись его прочитать
try:
    file = open("game_log.txt", "r")
    
    # Прочитать весь файл как одну строку
    content = file.read()
    
    # Закрыть файл
    file.close()
    
    print("Содержимое файла:")
    print("-" * 40)
    print(content)
    print("-" * 40)
    
except FileNotFoundError:
    print("Ошибка: game_log.txt не найден!")
    print("Запустите сначала 04_write_file.py чтобы создать его.")
    print()


# Построчное чтение (если файл существует)
print("\nТеперь читаем построчно:")
print("-" * 40)

try:
    file = open("game_log.txt", "r")
    
    # Прочитать все строки в список
    lines = file.readlines()
    
    file.close()
    
    # Обработать каждую строку
    for i, line in enumerate(lines, 1):
        # strip() удаляет символ новой строки в конце
        print(f"Строка {i}: {line.strip()}")
    
except FileNotFoundError:
    print("Файл не найден.")
