from notes import create_note, edit_note, read_note, find_note, delete_note, get_note_names
from user import create_user, list_users, edit_user, delete_user
import os


def main_menu():
    usr_name, users = create_user()
    print(f"Здравствуйте {usr_name}")
    while True:
        os.system("cls")
        print(f"Вы вошли как {usr_name}")
        print("1 - Меню пользователя")
        print("2 - Меню заметок")
        print("0 - Выйти")
        choice = input(">>> ")
        if choice == "1":
            result = user_menu(usr_name)
            if result is None:
                usr_name, users = create_user()
            else:
                usr_name = result
        elif choice == "2":
            notes_menu(usr_name)
        elif choice == "0":
            break
        else:
            print("Введите 1, 2 или 0")
            input("Нажмите Enter чтобы продолжить >>> ")


def notes_menu(usr_name):
    while True:
        os.system("cls")
        print("1 - Создать заметку")
        print("2 - Редактировать заметку")
        print("3 - Прочитать заметку")
        print("4 - Поиск заметки")
        print("5 - Удалить заметку")
        print("0 - Выйти в главное меню")
        choice = input(">>> ")
        if choice == "1":
            create_note(usr_name)
        elif choice == "2":
            edit_note(usr_name)
        elif choice == "3":
            read_note(usr_name)
        elif choice == "4":
            find_note(usr_name)
        elif choice == "5":
            delete_note(usr_name)
        elif choice == "0":
            break
        else:
            print("Введите число от 0 до 5")
            input("Нажмите Enter чтобы продолжить >>> ")


def user_menu(usr_name):
    while True:
        os.system("cls")
        print(f"Ваш текущий никнейм: {usr_name}")
        note_names = get_note_names(usr_name)
        if note_names:
            print("Ваши текущие заметки:")
            for name in note_names:
                print(f"  - {name}")
        else:
            print("У вас пока нет заметок")
        print()
        print("1 - Список всех пользователей")
        print("2 - Изменить никнейм")
        print("3 - Удалить пользователя")
        print("0 - Назад в главное меню")
        choice = input(">>> ")
        if choice == "1":
            list_users()
            input("Нажмите Enter чтобы продолжить >>> ")
        elif choice == "2":
            usr_name = edit_user(usr_name)
        elif choice == "3":
            deleted = delete_user(usr_name)
            if deleted:
                return None
        elif choice == "0":
            return usr_name
        else:
            print("Введите число от 0 до 3")
            input("Нажмите Enter чтобы продолжить >>> ")


main_menu()
