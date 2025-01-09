from datetime import datetime, timedelta

current_time = datetime.now() # получаем текущую дату
created_date = current_time.strftime('Created date: "%d-%m-%Y"') # форматируем текущую дату в дд-мм-гггг

while True: # запускаем цикл
    try:
        issue_year = int(input("Enter issue year (2025-2099): ")) # пользователь вводит год завершения заметки
        issue_month = int(input("Enter issue month (1-12): ")) # пользователь вводит месяц завершения заметки
        issue_day = int(input("Enter issue day (1-31): ")) # пользователь вводит день завершения заметки
        if 1 <= issue_month <= 12 and 1 <= issue_day <= 31 and 2025 <= issue_year <= 2099: # добавляем условие, при котором введенные данные дня, месяца и года должны попадать в нужный диапазон
            issue_date = f'Issue date: "{issue_day:02d}-{issue_month:02d}-{issue_year:02d}"'  # форматируем дату истечения заметки в дд-мм-гггг
            temp_issue_date = datetime(issue_year, issue_month, issue_day) # создаем datetime из введенных данных
            break # выход из цикла, если ввод корректен
        else: # если введенные значения дня, месяца или года не попадают в диапазон, то выводим сообщение:
            print("Invalid year, month or day. Please enter valid values.")
    except ValueError: # если пользователь ввел не числовые значения, то выводим сообщение:
        print("Invalid input. Please enter numbers for year, month and day.")
print(created_date, issue_date, sep='\n') # выводим дату создания и дату истечения

time_diff = temp_issue_date - current_time # разница между датой завершения и текущей датой

if temp_issue_date.date() == current_time.date():  # проверяем на совпадение с текущей датой
    print("Attention! Deadline today!") # если текущая дата и дата истечения совпадают, то выводим сообщение
elif time_diff < timedelta(0): # если дедлайн прошел
     days_past = abs(time_diff).days # вычисляем количество дней разницы
     print(f"Attention! The deadline expired {days_past} days ago.") # выводим сообщение
else: # если дедлайн не наступил
    time_diff += timedelta(days=1)  # Добавляем один день к разнице
    days_left = time_diff.days # вычисляем количество оставшихся дней
    print(f"There are {days_left} days left until the deadline.") # выводим сообщение
