import pathlib

path = pathlib.Path(__file__).parent

def get_cats_info(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            cats = []
            # Проходимо по кожному рядку, розділяємо id, ім'я та вік, та додаємо інформацію про кота до списку
            for line in lines:
                id, name, age = line.strip().split(',')
                # Додаємо словник з інформацією про кота до списку cats
                cats.append({"id": id, "name": name, "age": age})
            for cat in cats:
                print(cat)
            return cats
    except (FileNotFoundError, ValueError, ZeroDivisionError):
        return print("Error reading file or processing data.")

cats_info = get_cats_info("hw_6\\cats\\cats_file.txt")
cats_info

