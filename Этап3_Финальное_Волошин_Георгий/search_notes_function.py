from colorama import Fore, Style
notes = [

    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},

    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},

    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}

]
# функция отображения заметок
def display_notes(notes):
    if not notes:
        print(Fore.RED + "You have no saved notes." + Style.RESET_ALL)
        return

    print(Fore.GREEN + "Notes List:" + Style.RESET_ALL)
    for i, note in enumerate(notes):
        print(Fore.GREEN + "------------------------------" + Style.RESET_ALL)
        print(Fore. MAGENTA + f"Note №{i + 1}:" + Style.RESET_ALL)
        print(Fore.BLUE + f"Username: {note.get('username')}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Title: {note.get('title')}" + Style.RESET_ALL)
        print(Fore.BLUE + f"Content: {note.get('content')}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Status: {note.get('status')}" + Style.RESET_ALL)
        print(Fore.BLUE + f"Created date: {note.get('created_date')}" + Style.RESET_ALL)
        print(Fore.RED + f"Issue date: {note.get('issue_date')}" + Style.RESET_ALL)
    print(Fore.GREEN + "------------------------------" + Style.RESET_ALL)
# функция поиска по заметкам
def search_notes(notes, keyword = None, status = None):

    found_notes = []
    for note in notes:
        match = True
        # поиск по ключам
        if keyword:
            keyword = keyword.lower()
            if not (
                    keyword in note.get('username', '').lower() or
                    keyword in note.get('title', '').lower() or
                    keyword in note.get('content', '').lower()
            ):
                match = False
        # поиск по статусам
        if status:
            status = status.lower()
            if not status == note.get('status', '').lower():
                match = False

        if match:
            found_notes.append(note)

    if found_notes:
        print(Fore.GREEN + "Notes found:" + Style.RESET_ALL)

        # ЗАКОММЕНТИРОВАЛ ДЛЯ КОРРЕКТНОЙ РАБОТЕ menu.py, ПРИ РАБОТЕ ВНУТРИ СКРИПТА НАДО РАСКОММЕНТИРОВАТЬ ДЛЯ ОТОБРАЖЕНИЯ НАЙДЕННЫХ ЗАМЕТОК!!!:
        # display_notes(found_notes)

        return found_notes
    else:
        print(Fore.RED + "Notes not found!" + Style.RESET_ALL)
        return []

if __name__ == "__main__":
    # цикл для работы поиска внутри скрипта
    while True:
        if not notes:
            print(Fore.RED + "Notes List is empty!" + Style.RESET_ALL)
            break
        keyword = input("Enter a keyword to search (or press Enter to skip): ")
        status = input("Enter note status to search (or press Enter to skip): ")

        search_results = search_notes(notes, keyword, status)
        # цикл для обработки продолжения или завершения поиска
        while True:
            continue_search = input("Start new search? (Enter 'Y' to continue or 'N' to quit): ").lower()
            if continue_search == 'Y'.lower():
                break
            elif continue_search == 'N'.lower():
                print(Fore.MAGENTA + 'Goodbye!' + Style.RESET_ALL)
                exit()
            else:
                print(Fore.RED + "Error: enter 'Y' or 'N'." + Style.RESET_ALL)



