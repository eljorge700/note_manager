from datetime import datetime
from display_notes_function import display_notes # сделал добавление этой библиотеки уже после создания скрипта menu.py для улучшения интерфейса

# для правильной работы menu.py следующий блок пришлось закомментировать:

# note_to_update = [{'username' : 'George',
#          'titles' : ['To-do list', 'Help'],
#          'content' : 'Buy groceries for the week',
#          'status' : 'In progress',
#          'created date' : '15-01-2025',
#          'issue date' : '22-01-2025'}]
#
# display_notes(note_to_update)

# для правильной работы menu.py пришлось определить функции update_note() аргумент (note_to_update), для работы внутри скрипта его нужно убирать
# функция изменения заметки
def update_note(note_to_update):

    print("Note to update:")
    display_notes([note_to_update])

    updatable_fields = ["username", "titles", "content", "status", "issue date"]
    # цикл изменения заметки
    while True:
        field_to_update = input(f"What data do you want to update? Enter data ({', '.join(updatable_fields)}) or 'exit' to quit: ").lower()

        if field_to_update.lower() == "exit":
            print("Note update successfully")
            display_notes([note_to_update])
            break

        if field_to_update not in updatable_fields:
            print("Invalid field name. Please choose from the list.")
            continue

        if field_to_update == "issue date":
            # цикл обработки изменений дедлайна
            while True:
                new_issue_date_str = input("Enter the new issue date (dd-mm-yyyy): ")
                try:
                    new_issue_date = datetime.strptime(new_issue_date_str, "%d-%m-%Y")
                    note_to_update["issue date"] = new_issue_date.strftime('"%d-%m-%Y"')
                    break
                except ValueError:
                    print("Invalid date format. Please use dd-mm-yyyy.")

        elif field_to_update == "titles":
            print("Current titles: ")
            if note_to_update.get("titles"):
                for i, title in enumerate(note_to_update["titles"]):\
                    print(f"{i+1}. {title}")
            else:
                print("No titles found")
            # цикл обработки изменений заголовков, так как у меня реализовано создание нескольких заголовков, сделал возможность их добавлять, удалять, либо менять
            while True:
                titles_update = input('Enter the action for titles: "add", "delete", "change" or "exit" to quit: ')
                # добавление нового заголовка
                if titles_update == 'add':
                    new_title = input("Enter new title: ")
                    note_to_update["titles"].append(new_title)
                    break
                # удаление заголовка
                elif titles_update == 'delete':
                    if note_to_update.get('titles'):
                        # цикл обработки удаления заголовков
                        while True:
                            try:
                                index_to_delete = int(input("Enter number of title: ")) - 1
                                if 0 <= index_to_delete < len(note_to_update['titles']):
                                    del note_to_update['titles'][index_to_delete]
                                    break
                                else:
                                    print('Incorrect title number')
                            except ValueError:
                                print("Incorrect enter. Enter the number.")
                        break
                    else:
                        print("No titles fo delete")
                        break
                # замена заголовков
                elif titles_update == 'change':
                    new_title = input("Enter new titles separated by commas: ")
                    new_titles = [title.strip() for title in new_title.split(',')]
                    note_to_update['titles'] = new_titles
                    break

                elif titles_update == 'exit':
                    break
                else:
                    print("Wrong enter. Use words 'add', 'delete', 'change' or 'exit' to quit")

        else:
            new_value = input(f"Enter the new value for {field_to_update}: ")
            note_to_update[field_to_update] = new_value

        print("Note updated successfully:")
        display_notes([note_to_update])

    return note_to_update

if __name__ == "__main__":
    update_note()