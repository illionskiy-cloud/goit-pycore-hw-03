import pathlib

# Перетворовуємо шлях до файлу
path = pathlib.Path(__file__).parent

# Функція для для відкриття файлу та зчитування зарплат
def open_file(__file__):
    try:
        with open(__file__, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            salaries = []
            # Проходимо по кожному рядку, розділяємо ім'я та зарплату, та додаємо зарплату до списку
            for line in lines:
                name, salary = line.split(',') 
                salaries.append(int(salary)) 
            return salaries
    except (FileNotFoundError, ValueError):
        return None    
 
# Функція для обчислення загальної та середньої зарплати
def total_salary(path):
    salaries = open_file(path)
    # Якщо файл не знайдено або він пошкоджений, виводимо повідомлення та повертаємо (0, 0)
    if salaries is None:
        print('File not found or broken')
        return (0, 0) # Повертаємо кортеж (0, 0) для виключення помилки ValueError
    try:
        total = sum(salaries)
        average = total / len(salaries)
        return (int(total), int(average))
    except ZeroDivisionError:      # Виключення для випадку, коли файл порожній (ділення на нуль)
        return print("File is empty")

total, average = total_salary("hw_6\\salary\\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

