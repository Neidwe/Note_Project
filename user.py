import os


def load_users():
    if not os.path.exists("files/users.txt"):
        return []
    with open("files/users.txt", "r", encoding="utf8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def save_users(users):
    with open("files/users.txt", "w", encoding="utf8") as f:
        for u in users:
            f.write(u + "\n")


def create_user():
    os.makedirs("files", exist_ok=True)
    usr_name = input("Введите имя пользователя >>> ")
    os.system("clear")
    users = load_users()
    if usr_name not in users:
        users.append(usr_name)
        save_users(users)
    notes_path = f"files/{usr_name}.txt"
    if not os.path.exists(notes_path):
        open(notes_path, "a", encoding="utf8").close()
    return usr_name, users


def list_users():
    users = load_users()
    if not users:
        print("Пользователей пока нет")
        return
    print("Список пользователей:")
    for i, name in enumerate(users):
        print(f"{i + 1} - {name}")


def edit_user(usr_name):
    new_name = input(f"Введите новый никнейм ({usr_name}) >>> ") or usr_name
    if new_name == usr_name:
        print("Никнейм не изменён")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return usr_name

    users = load_users()
    if new_name in users:
        print("Такой никнейм уже занят")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return usr_name

    users = [new_name if u == usr_name else u for u in users]
    save_users(users)

    old_path = f"files/{usr_name}.txt"
    new_path = f"files/{new_name}.txt"
    if os.path.exists(old_path):
        with open(old_path, "r", encoding="utf8") as f:
            notes = f.readlines()
        notes = [note.replace(f"|{usr_name}|", f"|{new_name}|") for note in notes]
        with open(new_path, "w", encoding="utf8") as f:
            f.writelines(notes)
        os.remove(old_path)

    print(f"Никнейм изменён на {new_name}")
    input("Нажмите Enter чтобы вернуться в меню >>> ")
    return new_name


def delete_user(usr_name):
    confirm = input(f"Вы уверены что хотите удалить пользователя {usr_name} и все его заметки? (да/нет) >>> ")
    if confirm == "да":
        if os.path.exists(f"files/{usr_name}.txt"):
            os.remove(f"files/{usr_name}.txt")
        users = [u for u in load_users() if u != usr_name]
        save_users(users)
        print(f"Пользователь {usr_name} удалён")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return True
    else:
        print("Отмена удаления")
        input("Нажмите Enter чтобы вернуться в меню >>> ")
        return False
