from datetime import datetime, timedelta

# функция создания новой заметки
def create_note():

    note = {}

    note["titles"] = []
    while True:
        title = input('\nEnter note title (enter "stop" or leave empty to complete): ')
        if title.lower() == "stop" or not title:
            break
        if title in note["titles"]:
            print("This title already exists. Please enter a different title.")
        else:
            note["titles"].append(title)

    note["content"] = input('Enter note description: ')

    # функция создания статуса
    def get_note_status(note):

        if "status" not in note:
            note["status"] = "empty"
        while True:
            print(f"\nCurrent note status: \"{note['status']}\"")
            valid_statuses = ["completed", "in progress", "paused"]
            print("Enter a new note status (or a number to select from the list):")
            for i, status in enumerate(valid_statuses):
                print(f"{i + 1}. {status}")
            user_input = input("Enter your choice: ").strip().lower()
            if user_input.isdigit():
                try:
                    user_choice = int(user_input)
                    if 1 <= user_choice <= len(valid_statuses):
                        note["status"] = valid_statuses[user_choice - 1]
                        break
                    else:
                        print("Invalid choice. Please select a number within the range.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif user_input:
                note["status"] = user_input
                break
            else:
                print("Status cannot be empty.")

    get_note_status(note)

    # дата создания заметки
    current_time = datetime.now()
    note["created_date"] = current_time.strftime('"%d-%m-%Y"')

    # дата окончания заметки
    while True:
        try:
            issue_year = int(input("Enter issue year (2025-2099): "))
            issue_month = int(input("Enter issue month (1-12): "))
            issue_day = int(input("Enter issue day (1-31): "))
            temp_issue_date = datetime(issue_year, issue_month, issue_day)
            if 2025 <= issue_year <= 2099:
                note["issue_date"] = temp_issue_date.strftime('"%d-%m-%Y"')
                time_diff = temp_issue_date.date() - current_time.date()
                if time_diff == timedelta(0):
                    print("Attention! Deadline today!")
                elif time_diff < timedelta(0):
                    print(f"Attention! The deadline expired {abs(time_diff).days} days ago.")
                else:
                    print(f"There are {time_diff.days} days left until the deadline.")
                break
            else:
                print("Invalid year. Please enter a year between 2025 and 2099.")
        except ValueError:
            print("Invalid input. Please enter numbers for year, month and day.")

    return note


# функция вывода информации о заметке
def print_note(note):

    print("\n--- Note ---")
    print(f"Username: {note['username']}")
    print("Note titles:")
    if note['titles']:
        for title in note["titles"]:
            print(f"- {title}")
    else:
        print("No titles entered.")

    print(f"Note content: {note['content']}")
    print(f"Note status: {note['status']}")
    print(f"Created date: {note['created_date']}")
    print(f"Issue date: {note['issue_date']}")
    issue_date_obj = datetime.strptime(note['issue_date'], '"%d-%m-%Y"').date()
    today = datetime.now().date()
    time_diff = issue_date_obj - today
    if time_diff == timedelta(0):
        print("Attention! Deadline today!")
    elif time_diff < timedelta(0):
        print(f"Attention! The deadline expired {abs(time_diff).days} days ago.")
    else:
        print(f"There are {time_diff.days} days left until the deadline.")

# функция вывода заметок по пользователю
def print_notes_by_user(notes, username):

    user_notes = [note for note in notes if note.get("username") == username]
    if user_notes:
        for note in user_notes:
            print_note(note)
    else:
        print(f"No notes found for user {username}.")


# функция вывода заметок по заголовку
def print_notes_by_title(notes, title_substring):

    found_notes = []
    for note in notes:
        if any(title_substring.lower() in title.lower() for title in note.get("titles", [])):
            found_notes.append(note)

    if found_notes:
        for note in found_notes:
            print_note(note)
    else:
        print(f"No notes found with title containing '{title_substring}'.")

# функция вывода заметок по статусу
def print_notes_by_status(notes, status):

    status_notes = [note for note in notes if note.get("status").lower() == status.lower()]
    if status_notes:
        for note in status_notes:
            print_note(note)
    else:
        print(f"No notes found with status '{status}'.")

# функция удаления заметок
def delete_note(notes, note_index):

    try:
        if 0 <= note_index < len(notes):
            del notes[note_index]
            print("Note deleted successfully!")
        else:
            print("Invalid note index.")
    except IndexError:
        print("Invalid note index.")

# приветствие
print('Hello, this is note manager!')

# основной цикл

# ввод имени пользователя
username = input("Enter your name: ")
notes = []
# запрос выбора действия
while True:
    action = input(f"\n{username}, what do you want to do? (create(1), print_all(2), print_by_user(3), print_by_title(4), print_by_status(5), delete(6), exit(7)): ").lower()
    try:
        action_num = int(action)
    except ValueError:
        action_num = None
    # запуск функции создания заметки
    if action == "create" or action_num == 1:
        new_note = create_note()
        new_note["username"] = username
        notes.append(new_note)
        print("Note created successfully!")

    # запуск вывода всех заметок
    elif action == "print_all" or action_num == 2:
        if notes:
            for i, note in enumerate(notes):
                print(f"Note index: {i}")
                print_note(note)
        else:
            print("No notes created yet.")


    # запуск вывода заметок по определенному пользователю
    elif action == "print_by_user" or action_num == 3:
        username_to_print = input("Enter username to print notes for: ")
        print_notes_by_user(notes, username_to_print)

    # запуск вывода заметок по заголовку
    elif action == "print_by_title" or action_num == 4:
        title_substring = input("Enter part of the title to search for: ")
        print_notes_by_title(notes, title_substring)

    # запуск вывода заметок по статусу
    elif action == "print_by_status" or action_num == 5:
        status_to_search = input("Enter the status to search for: ")
        print_notes_by_status(notes, status_to_search)

    # запуск удаления заметок
    elif action == "delete" or action_num == 6:
        try:
            print("\nAll created notes:")
            for i, note in enumerate(notes):
                print(f"Note index: {i}")
                print_note(note)
            note_index = int(input("\nEnter the index of the note to delete: "))
            delete_note(notes, note_index)
        except ValueError:
            print("Invalid input. Please enter a number for the note index.")

    # выход
    elif action == "exit" or action_num == 7:
        break

    else:
        print("Invalid action.")
