# имя пользователя
username = input('Enter your name: ')

# заголовок заметки
title = input('Enter note title: ')

# описание заметки
content = input('Enter note description: ')

# статус заметки
status = input('Enter note status: ')

# дата создания заметки
from datetime import datetime
current_time = datetime.now()
created_date = current_time.strftime('Created date: "%d-%m"')
temp_created_date = current_time

# дата истечения заметки
current_year = current_time.year
issue_month = int(input("Enter issue month: "))
issue_day = int(input("Enter issue day: "))
issue_date = f'Issue date: "{issue_day:02d}-{issue_month:02d}"'
temp_issue_date = datetime(current_year, issue_month, issue_day)

print(f"Username: {username}\nNote title: {title}\nNote content: {content}\nNote status: {status}")
print(created_date, issue_date, sep='\n')
