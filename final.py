from datetime import datetime

# список для хранения информации о заметке
note = []

# имя пользователя
username = input('Enter your name: ')
note.append(username)

# описание заметки
content = input('Enter note description: ')
note.append(content)

# статус заметки
status = input('Enter note status: ')
note.append(status)

# дата создания заметки
current_time = datetime.now()
created_date = current_time.strftime('Created date: "%d-%m"')
temp_created_date = current_time
note.append(created_date)

# дата истечения заметки
current_year = current_time.year
issue_month = int(input("Enter issue month: "))
issue_day = int(input("Enter issue day: "))
issue_date = f'Issue date: "{issue_day:02d}-{issue_month:02d}"'
temp_issue_date = datetime(current_year, issue_month, issue_day)
note.append(issue_date)

# заголовок заметки
titles = []
title_1 = input('Enter note title: ')
titles.append(title_1)
title_2 = input('Enter note subtitle: ')
titles.append(title_2)
title_3 = input('Enter note recommendations: ')
titles.append(title_3)
note.append(titles)

print(f"Username: {note[0]}")
print("Note titles: ")
for title in note[5]:
    print(f"- {title}")
print(f"Note content: {note[1]}")
print(f"Note status: {note[2]}")
print(f"created_date: {note[3]}")
print(f"issue_date: {note[4]}")
