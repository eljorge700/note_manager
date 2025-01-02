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

print(created_date, issue_date, sep='\n')
print(f'Temp created date: {temp_created_date}')
print(f'Temp issue date: {temp_issue_date}')
