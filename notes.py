import os
import time


IMPORTANCE_LEVELS = ("низкая", "средняя", "высокая")


def load_notes(usr_name):
    path = f"files/{usr_name}.txt"
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf8") as file:
        notes = [line for line in file.readlines() if line.strip()]
    return notes


def get_note_names(usr_name):
    notes = load_notes(usr_name)
    if not notes:
        return []
    return [note.strip().split("|")[0] for note in notes]


def importance_label(importance):
    if importance == "высокая":
        return f"{importance} (ВАЖНАЯ ЗАМЕТКА)"
    return importance


def print_note(note):
    print(f"Название: {note[0]}")
    print(f"Содержание: {note[1]}")
    print(f"Важность: {importance_label(note[2])}")
    print(f"Владелец: {note[3]}")
    print(f"Дата: {note[4]}")
    print(f"Тип: {note[5]}")


def create_note(usr_name):
    os.makedirs("files", exist_ok=True)
    with open(f"files/{usr_name}.txt", "a+", encoding="utf8") as usr_note:
        note_name = input("Введите имя для заметки >>> ")
        note_content = input("Введите содержание для заметки >>> ")
        while True:
            note_importance = input("Введите важность (низкая/средняя/высокая) >>> ").lower()
            if note_importance in IMPORTANCE_LEVELS:
                break
            print("Введите одно из значений: низкая, средняя, высокая")
        note_type = input("Введите тип заметки >>> ")
        time_creat = time.strftime("%Y-%m-%d %H:%M")
        usr_note.write(f"{note_name}|{note_content}|{note_importance}|{usr_name}|{time_creat}|{note_type}\n")
        print("Заметка сохранена!")
        input("Нажмите Enter чтобы вернуться в меню >>> ")


def read_note(usr_name):
    notes = load_notes(usr_name)
    if not notes:
        print("У вас пока нет заметок")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return

    print("1 - Прочитать одну заметку")
    print("2 - Прочитать все заметки")
    choice = input(">>> ")

    if choice == "1":
        for i, note in enumerate(notes):
            name = note.strip().split("|")[0]
            print(f"{i + 1} - {name}")
        choice = input("Какую заметку посмотреть? >>> ")
        if not choice.isdigit() or not (1 <= int(choice) <= len(notes)):
            print("Неверный номер")
            input("Нажмите Enter чтобы вернуться в меню >>> ")
            return
        note = notes[int(choice) - 1].strip().split("|")
        print_note(note)
        input("Нажмите Enter чтобы вернуться в меню >>> ")
    elif choice == "2":
        for i, note in enumerate(notes):
            note = note.strip().split("|")
            print(f"--- Заметка {i + 1} ---")
            print_note(note)
            print()
        input("Нажмите Enter чтобы вернуться в меню >>> ")
    else:
        print("Введите 1 или 2")
        input("Нажмите Enter чтобы вернуться в меню >>> ")


def find_note(usr_name):
    notes = load_notes(usr_name)
    if not notes:
        print("У вас пока нет заметок")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return

    found = False
    search_name = input("Введите имя заметки для поиска >>> ")
    for i, note in enumerate(notes):
        name = note.strip().split("|")[0]
        if name == search_name:
            found = True
            note = notes[i].strip().split("|")
            print("--- Заметка ---")
            print_note(note)
            input("Нажмите Enter чтобы вернуться в меню >>> ")
    if not found:
        print("Такой заметки нет")
        input("Нажмите Enter чтобы вернуться в меню >>> ")


def edit_note(usr_name):
    notes = load_notes(usr_name)
    if not notes:
        print("У вас пока нет заметок")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return

    for i, note in enumerate(notes):
        name = note.split("|")[0]
        print(f"{i + 1} - {name}")

    choice = input("Какую заметку редактировать? >>> ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(notes)):
        print("Неверный номер")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return
    choice = int(choice) - 1
    note = notes[choice].strip().split("|")

    print("Оставьте пустым если не хотите менять")
    new_name = input(f"Название ({note[0]}) >>> ") or note[0]
    new_content = input(f"Содержание ({note[1]}) >>> ") or note[1]

    new_importance = input(f"Важность ({note[2]}) - низкая/средняя/высокая >>> ").lower() or note[2]
    while new_importance not in IMPORTANCE_LEVELS:
        new_importance = input("Введите одно из значений: низкая, средняя, высокая >>> ").lower()

    notes[choice] = "|".join([new_name, new_content, new_importance, note[3], note[4], note[5]]) + "\n"
    with open(f"files/{usr_name}.txt", "w", encoding="utf8") as file:
        file.writelines(notes)
    print("Заметка изменена!")
    input("Нажмите Enter чтобы вернуться в меню >>> ")


def delete_note(usr_name):
    notes = load_notes(usr_name)
    if not notes:
        print("У вас пока нет заметок")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return

    for i, note in enumerate(notes):
        name = note.strip().split("|")[0]
        print(f"{i + 1} - {name}")

    choice = input("Какую заметку удалить? >>> ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(notes)):
        print("Неверный номер")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return
    choice = int(choice) - 1

    note_name = notes[choice].strip().split("|")[0]
    confirm = input(f"Удалить заметку '{note_name}'? (да/нет) >>> ")
    if confirm == "да":
        del notes[choice]
        with open(f"files/{usr_name}.txt", "w", encoding="utf8") as file:
            file.writelines(notes)
        print("Заметка удалена")
    else:
        print("Отмена удаления")
    input("Нажмите Enter чтобы вернуться в меню >>> ")
