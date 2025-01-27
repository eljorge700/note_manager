from colorama import init, Fore, Style

from create_note_function import create_note, print_note
from update_note_function import update_note
from display_notes_function import display_notes
from search_notes_function import search_notes

init(autoreset=True)

notes = [{'username': 'Алексей', 'titles': ['Список покупок'], 'content': 'Купить продукты на неделю', 'status': 'новая', 'created date': '27-11-2024', 'issue date': '30-11-2024'},

    {'username': 'Мария', 'titles': ['Учеба'], 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created date': '25-11-2024', 'issue date': '01-12-2024'},

    {'username': 'Иван', 'titles': ['План работы', 'План учебы'], 'content': 'Завершить проект', 'status': 'выполнено', 'created date': '20-11-2024', 'issue date': '26-11-2024'}]
# функция удаления заметки по индексу
def delete_note():
    note_index = int(input("Enter note number to delete: ")) - 1
    try:
        if 0 <= note_index < len(notes):
            del notes[note_index]
            print("Note deleted successfully!")
        else:
            print("Invalid note index.")
    except IndexError:
        print("Invalid note index.")
# функция меню
def show_menu():
    print(f"{Fore.GREEN}\nHello! This is your Note Manager!")

    while True:

        print(f"{Fore.CYAN}\n______Notes Menu______")
        print(f"{Fore.BLUE}1. Создать новую заметку")
        print(f"{Fore.RED}2. Показать все заметки")
        print(f"{Fore.BLUE}3. Обновить заметку")
        print(f"{Fore.RED}4. Удалить заметку")
        print(f"{Fore.BLUE}5. Найти заметки")
        print(f"{Fore.RED}6. Выйти из программы")

        choice = input(f"{Fore.GREEN}\nWhat do you want to do?(Enter a number from 1 to 6): ")
        # блок для вызова функции создания заметки(create_note())
        if choice == '1':
            note = create_note()
            notes.append(note)
            print_note(note)
        # блок для вызова функции вывода всех заметок на экран(display_notes())
        elif choice == '2':
            display_notes(notes)
        # блок для вызова функции изменения заметки(update_note())
        elif choice == '3':
            if notes:
                display_notes(notes)
                index = int(input(f"{Fore.GREEN}Введите номер заметки для обновления: ")) - 1
                if 0 <= index < len(notes):
                    notes[index] = update_note(notes[index])
                else:
                    print(f"{Fore.RED}Неверный номер заметки.")
            else:
                print(f"{Fore.RED}Список заметок пуст.")
        # блок для вызова функции удаления заметки(delete_note())
        elif choice == '4':
            if notes:
                display_notes(notes)
                delete_note()
        # блок для вызова функции поиска заметки(search_notes())
        elif choice == '5':
            while True:
                keyword = input(f"{Fore.GREEN}Введите ключевое слово для поиска: ")
                status = input(f"{Fore.GREEN}Введите статус для поиска (или оставьте пустым): ")
                found_notes = search_notes(notes, keyword, status)
                display_notes(found_notes)
                while True:
                    continue_search = input(f"{Fore.GREEN}Start new search? (Enter {Fore.RED}'Y' {Fore.GREEN}to continue or {Fore.RED}'N' {Fore.GREEN}to return to menu): ").lower()
                    if continue_search == 'Y'.lower():
                        break
                    elif continue_search == 'N'.lower():
                        break
                    else:
                        print(f"{Fore.RED}Error: enter 'Y' or 'N'.")
                        continue
                if continue_search == 'Y'.lower():
                    continue
                elif continue_search == 'N'.lower():
                    break
        # завершение работы программы
        elif choice == '6':
            print(f"{Fore.GREEN}Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid input. Please select a number from the list (1-6): ")

if __name__ == "__main__":
    show_menu()

