"""
Тесты для тестируемого менеджера задач

Запустить: pytest test_task_manager.py -v

Эти тесты показывают, как разделение логики от I/O
делает код намного легче для тестирования.
"""

from task_manager_testable import (
    validate_task_description,
    create_task_dict,
    add_task,
    get_task_by_index,
    complete_task,
    delete_task,
    format_task_list,
)


# ============================================================
# Тесты валидации
# ============================================================

def test_validate_task_description_valid():
    """Тест что валидные описания принимаются."""
    assert validate_task_description("Buy milk")
    assert validate_task_description("   Task with spaces   ")
    assert validate_task_description("A")


def test_validate_task_description_invalid():
    """Тест что невалидные описания отклоняются."""
    assert not validate_task_description("")
    assert not validate_task_description("   ")
    assert not validate_task_description(None)
    assert not validate_task_description(123)


# ============================================================
# Тесты создания задач
# ============================================================

def test_create_task_dict():
    """Тест что словари задач создаются корректно."""
    task = create_task_dict("Buy milk")
    
    assert task["description"] == "Buy milk"
    assert task["completed"] == False


def test_create_task_dict_strips_whitespace():
    """Тест что пробелы удаляются."""
    task = create_task_dict("   Buy milk   ")
    assert task["description"] == "Buy milk"


# ============================================================
# Тесты добавления задач
# ============================================================

def test_add_task_valid():
    """Тест добавления валидной задачи."""
    tasks = []
    result = add_task(tasks, "Buy milk")
    
    assert result == True
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Buy milk"


def test_add_task_invalid():
    """Тест что невалидные задачи не добавляются."""
    tasks = []
    result = add_task(tasks, "")
    
    assert result == False
    assert len(tasks) == 0


def test_add_multiple_tasks():
    """Тест добавления нескольких задач."""
    tasks = []
    add_task(tasks, "Task 1")
    add_task(tasks, "Task 2")
    add_task(tasks, "Task 3")
    
    assert len(tasks) == 3
    assert tasks[0]["description"] == "Task 1"
    assert tasks[2]["description"] == "Task 3"


# ============================================================
# Тесты получения задач
# ============================================================

def test_get_task_by_index_valid():
    """Тест получения задачи по валидному индексу."""
    tasks = [
        {"description": "Task 1", "completed": False},
        {"description": "Task 2", "completed": False},
    ]
    
    task = get_task_by_index(tasks, 1)
    assert task["description"] == "Task 1"
    
    task = get_task_by_index(tasks, 2)
    assert task["description"] == "Task 2"


def test_get_task_by_index_invalid():
    """Тест получения задачи по невалидному индексу."""
    tasks = [{"description": "Task 1", "completed": False}]
    
    assert get_task_by_index(tasks, 0) == None
    assert get_task_by_index(tasks, 2) == None
    assert get_task_by_index(tasks, -1) == None


def test_get_task_by_index_empty_list():
    """Тест получения из пустого списка задач."""
    tasks = []
    assert get_task_by_index(tasks, 1) == None


# ============================================================
# Тесты выполнения задач
# ============================================================

def test_complete_task_valid():
    """Тест выполнения задачи."""
    tasks = [
        {"description": "Task 1", "completed": False},
        {"description": "Task 2", "completed": False},
    ]
    
    result = complete_task(tasks, 1)
    
    assert result == True
    assert tasks[0]["completed"] == True
    assert tasks[1]["completed"] == False


def test_complete_task_invalid():
    """Тест выполнения с невалидным индексом."""
    tasks = [{"description": "Task 1", "completed": False}]
    
    result = complete_task(tasks, 2)
    assert result == False
    assert tasks[0]["completed"] == False


# ============================================================
# Тесты удаления задач
# ============================================================

def test_delete_task_valid():
    """Тест удаления задачи."""
    tasks = [
        {"description": "Task 1", "completed": False},
        {"description": "Task 2", "completed": False},
        {"description": "Task 3", "completed": False},
    ]
    
    result = delete_task(tasks, 2)
    
    assert result == True
    assert len(tasks) == 2
    assert tasks[0]["description"] == "Task 1"
    assert tasks[1]["description"] == "Task 3"


def test_delete_task_invalid():
    """Тест удаления с невалидным индексом."""
    tasks = [{"description": "Task 1", "completed": False}]
    
    result = delete_task(tasks, 2)
    assert result == False
    assert len(tasks) == 1


def test_delete_task_first():
    """Тест удаления первой задачи."""
    tasks = [
        {"description": "Task 1", "completed": False},
        {"description": "Task 2", "completed": False},
    ]
    
    delete_task(tasks, 1)
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Task 2"


def test_delete_task_last():
    """Тест удаления последней задачи."""
    tasks = [
        {"description": "Task 1", "completed": False},
        {"description": "Task 2", "completed": False},
    ]
    
    delete_task(tasks, 2)
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Task 1"


# ============================================================
# Тесты форматирования
# ============================================================

def test_format_task_list_empty():
    """Тест форматирования пустого списка задач."""
    tasks = []
    lines = format_task_list(tasks)
    
    assert len(lines) == 1
    assert "задач" in lines[0].lower()


def test_format_task_list_with_tasks():
    """Тест форматирования списка задач."""
    tasks = [
        {"description": "Task 1", "completed": False},
        {"description": "Task 2", "completed": True},
        {"description": "Task 3", "completed": False},
    ]
    
    lines = format_task_list(tasks)
    
    assert len(lines) == 3
    assert "1." in lines[0]
    assert "Task 1" in lines[0]
    assert "[ ]" in lines[0]
    
    assert "2." in lines[1]
    assert "Task 2" in lines[1]
    assert "[✓]" in lines[1]


def test_format_task_list_numbering():
    """Тест что задачи нумеруются корректно."""
    tasks = [
        {"description": "A", "completed": False},
        {"description": "B", "completed": False},
        {"description": "C", "completed": False},
    ]
    
    lines = format_task_list(tasks)
    assert lines[0].startswith("1.")
    assert lines[1].startswith("2.")
    assert lines[2].startswith("3.")
