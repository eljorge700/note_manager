from datetime import datetime, timedelta


# создание новой заметки
def create_note():

    note = {}

    # заголовки заметки
    note["titles"] = []
    while True:
        title = input('Enter note title (enter "stop" or leave empty to complete): ')
        if title.lower() == "stop" or not title:
            break
        if title in note["titles"]:
            print("This title already exists. Please enter a different title.")
        else:
            note["titles"].append(title)

    note["content"] = input('Enter note description: ')

    # статус заметки
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

    # текущая дата
    current_time = datetime.now()
    note["created_date"] = current_time.strftime('"%d-%m-%Y"')
    # дата дедлайна
    while True:
        try:
            issue_year = int(input("Enter issue year (2025-2099): "))
            issue_month = int(input("Enter issue month (1-12): "))
            issue_day = int(input("Enter issue day (1-31): "))
            temp_issue_date = datetime(issue_year, issue_month, issue_day)
            if 2025 <= issue_year <= 2099:
                note["issue_date"] = temp_issue_date.strftime('"%d-%m-%Y"')

                time_diff = temp_issue_date.date() - current_time.date()  # Работаем только с датами

                if time_diff == timedelta(0):
                    print("Attention! Deadline today!")
                elif time_diff < timedelta(0):
                    print(f"Attention! The deadline expired {abs(time_diff).days} days ago.")
                else:
                    print(f"There are {time_diff.days} days left until the deadline.")

                break
            else:
                print("Invalid year. Please enter a year between 2024 and 2099.")


        except ValueError:
            print("Invalid input. Please enter numbers for year, month and day.")

    return note

# вывод информации о созданной заметке
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

# приветствие в начале
print('Hello, this is note manager!')
# основная часть
username = input("Enter your name: ")
notes = []
while True:
    action = input(f"\n{username}, do you want to create a new note? (yes/no): ").lower()
    if action == "yes":
        new_note = create_note()
        new_note["username"] = username
        notes.append(new_note)
        print_note(notes[-1])
    elif action == "no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
# вывод всех заметок
print("\nAll created notes:")
for note in notes:
    print_note(note)
