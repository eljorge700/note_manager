from datetime import datetime

# список для хранения информации о заметке
note = [] # пустой список, куда будут добавляться данные, введенные пользователем

# имя пользователя
username = input('Enter your name: ') # пользователь вводит свое имя
note.append(username) # передаем имя пользователя в список note

# описание заметки
content = input('Enter note description: ') # пользователь вводит описание заметки
note.append(content) # передаем описание заметки в список note

# статус заметки
status = input('Enter note status: ') # пользователь вводит статус заметки
note.append(status) # передаем статус заметки в список note

# дата создания заметки
current_time = datetime.now() # используем текущую дату
created_date = current_time.strftime('Created date: "%d-%m"') # конвертируем текущую дату в формат для вывода дд-мм(день-месяц), который будет отражать дату создания заметки
temp_created_date = current_time # сохранение текущей даты в первоначальном формате
note.append(created_date) # передаем дату создания в список note

# дата истечения заметки
current_year = current_time.year # получаем текущий год и сохраняем его
while True: # запускаем цикл
    try:
        issue_month = int(input("Enter issue month (1-12): ")) # пользователь вводит месяц завершения заметки
        issue_day = int(input("Enter issue day (1-31): ")) # пользователь вводит день завершения заметки
        if 1 <= issue_month <= 12 and 1 <= issue_day <= 31: # добавляем условие, при котором введенные данные дня и месяца должны попадать в нужный диапазон
            issue_date = f'Issue date: "{issue_day:02d}-{issue_month:02d}"' # конвертируем дату в формат для вывода дд-мм
            temp_issue_date = datetime(current_year, issue_month, issue_day) # сохраняем дату истечения заметки, учитывая день, месяц и год(используем год создания)
            break # Выход из цикла, если ввод корректен
        else: # Если введенные значения дня или месяца не попадают в диапазон, то выводим сообщение:
            print("Invalid month or day. Please enter valid values.")
    except ValueError: # Если пользователь ввел не числовые значения, то выводим сообщение:
        print("Invalid input. Please enter numbers for month and day.") #
note.append(issue_date)

# заголовок заметки
titles = [] # список, куда будут добавляться заголовки, введенные пользователем
while True: # запускаем цикл
    title = input('Enter note title (enter "stop" or leave empty to complete): ') # пользователю предлагают ввести заголовок или завершить процесс
    if title.lower() == "stop" or not title: # Преобразуем "stop" в нижний регистр, в каком бы он не был введен. Завершаем, если введено "stop" или пустая строка.
        break # Выход из цикла
    if title in titles:  # Проверка на уникальность. Если в списке titles уже есть заметка с таким заголовков, выводим сообщение:
        print("This title already exists. Please enter a different title.")
    else: # Если такого заголовка еще нет, то добавляем его в список titles и возвращаемся к циклу
        titles.append(title) # добавляем заголовок в список titles
note.append(titles) # добавляем titles в список note

print(f"Username: {note[0]}") # Выводим на печать имя пользователя
print("Note titles: ") # Выводим на печать заголовки заметки
for title in note[5]:
    print(f"- {title}")
print(f"Note content: {note[1]}") # Выводим на печать описание заметки
print(f"Note status: {note[2]}") # Выводим на печать статус заметки
print({note[3]}) # Выводим на печать дату создания
print({note[4]}) # Выводим на печать дату завершения
