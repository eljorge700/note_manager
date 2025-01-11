def update_status(note_status):
    if "Current status" not in note_status: # проверяем наличие ключа в словаре
        note_status["Current status"] = "empty" # начальное значение, если статуса нет
    current_status = note_status["Current status"] # получаем текущее значение статуса из словаря

    print(f"Current note status: \"{current_status}\"") # выводим значение текущего статуса в консоль

    valid_statuses = ["completed", "in progress", "paused"] # создаем список доступных статусов
    while True: # запускаем цикл
        print("\nEnter a new note status (or a number to select from the list):") # просим пользователя ввести новый статус или выбрать значение из списка
        for i, status in enumerate(valid_statuses): # перебираем список статусов
            print(f"{i + 1}. {status}") # выводим их с номерами для ввода

        user_input = input("Enter your choice: ") # выводим в консоль запрос на ввод статуса пользователем

        if user_input.isdigit():
            user_choice = int(user_input) # пытаемся преобразовать введенное значение в целое число
            if 1 <= user_choice <= len(valid_statuses): # проверяем, является ли введенное число допустимым значением
                new_status = valid_statuses[user_choice - 1] # если является, то берем новый статус из списка
                break # выходим из цикла
            else:
                print("Incorrect choice. Please select a number from the list or enter text.") # если не является выводим сообщение об ошибке
        elif "." not in user_input:  # проверяем, что введено не дробное число
            new_status = user_input.strip().lower() # считаем его текстовым и переводим в нижний регистр
            if new_status: # проверяем, что строка не пустая
                break # выходим из цикла
            else:
                print("Status couldn't be empty") # если строка пустая, выводим сообщение об ошибке
        else:
            print("Invalid input. Please enter a whole number or text (without a period)")

    note_status["Current status"] = new_status # обновляем статус в словаре
    return note_status["Current status"] # возвращаем обновленный статус

note_data = {} # создаем пустой словарь
updated_status = update_status(note_data) # сохраняем результат в переменной
print(f"\nThe note status has been successfully updated to: \"{updated_status}\"") # выводим обновленный статус в консоль
print(f'{note_data}') # выводим словарь для проверки.