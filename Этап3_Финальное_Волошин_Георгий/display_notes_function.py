from colorama import Fore, Style
from datetime import datetime, timedelta

notes = [{'username' : 'George',
         'titles' : ['To-do list'],
         'content' : 'Buy groceries for the week',
         'status' : 'In progress',
         'created date' : '15-01-2025',
         'issue date' : '22-01-2025'},

         {'username': 'Nadya',
          'titles': ['To-do list', 'Shopping List'],
          'content': 'Shopping',
          'status': 'Done',
          'created date': '15-01-2025',
          'issue date': '22-01-2025'}]
# функция вывода заметок
def display_notes(notes):
    if not notes:
        print(Fore.RED + "Копировать код\nУ вас нет сохранённых заметок." + Style.RESET_ALL)
        return

    print(Fore.GREEN + "Notes List:" + Style.RESET_ALL)
    for i, note in enumerate(notes):
        print(Fore.GREEN + "------------------------------" + Style.RESET_ALL)
        print(Fore. MAGENTA + f"Note №{i + 1}:" + Style.RESET_ALL)
        print(Fore.BLUE + f"Username: {note.get('username')}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Titles: " + Style.RESET_ALL)
        if note['titles']:
            for title in note["titles"]:
                print(f"- {title}")
        else:
            print("No titles entered.")

        print(Fore.BLUE + f"Content: {note.get('content')}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Status: {note.get('status')}" + Style.RESET_ALL)
        print(Fore.BLUE + f"Created date: {note.get('created date')}" + Style.RESET_ALL)
        print(Fore.RED + f"Issue date: {note.get('issue date')}" + Style.RESET_ALL)
        # добавил дополнительно вывод данных дедлайна в заметках для информативности, чтобы в menu.py отображалось
        try:
            issue_date_str = note.get('issue date')
            issue_date = datetime.strptime(issue_date_str, '%d-%m-%Y')
            current_date = datetime.now()
            time_diff = issue_date.date() - current_date.date()

            if time_diff == timedelta(0):
                print(Fore.RED + "Attention! Deadline today!" + Style.RESET_ALL)
            elif time_diff < timedelta(0):
                print(Fore.RED + f"Attention! The deadline expired {abs(time_diff).days} days ago." + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"There are {time_diff.days} days left until the deadline." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid date format for issue date. Cannot calculate time remaining." + Style.RESET_ALL)

    print(Fore.GREEN + "------------------------------" + Style.RESET_ALL)
if __name__ == "__main__":
    display_notes(notes)