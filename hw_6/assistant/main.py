# Функція, яка розбиратиме введений користувачем рядок на команду та її аргументи
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
# Додавання контакту
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
# Зміна номера контакту
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact updated'
# Показати номер контакта
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]
# Показати всі контакти
def show_all(contacts):
    return contacts
# основна функція
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    # Нескінченний цикл
    while True:
        user_input = input("Enter a command: ")  
        command, *args = parse_input(user_input)
    # Закриття програми
        if command in ["close", "exit"]:
            print("Good bye!")
            break
    # Вітання
        elif command == "hello":
            print("How can I help you?")
    # Реалізація додавання контакту(2 аргументи)
        elif command == 'add':
            if len(args) != 2:
                print('Enter name and phone number')
            else:
                print(add_contact(args, contacts))
    # Реалізація зміни контакту(2 аргументи)
        elif command == 'change':
            if len(args) != 2:
                print('Enter name and phone number')
            else:
                if args[0] not in contacts:     # Якщо контакту не існує
                    print(f'Contact not found')
                else:
                    print(change_contact(args, contacts))
    # Реалізація показу номера(1 аргумент)
        elif command == 'phone':
            if len(args) != 1:
                print('Enter name only')
            else:
                print(show_phone(args, contacts))
    # Реалізація показу всіх команд(кількість аргументів неважлива)      
        elif command == 'all':
            print(show_all(contacts))
    # Невірна команда
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

