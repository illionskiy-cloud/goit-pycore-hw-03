import random

# Вхідні дані
try:
    min = int(input("Enter the minimum number: "))
    max = int(input("Enter the maximum number: "))
    quantity = int(input("Enter the quantity: "))
except ValueError: # Виключення помилки при введенні != int
    print("Please enter valid integers for minimum, maximum, and quantity.")


def get_numbers_ticket(min, max, quantity):
    
        numbers = list(range(min, max + 1))
        if quantity > len(numbers): # quantity не може бути більше, ніж кількість чисел у діапазоні
            return print(f'Quantity cannot be greater than {max}')
        elif min < 1 or max > 1000: # за умовою - не більше 1000, не менше 1
            return print('Minimum and maximum nubers must be between 1 and 1000.')
        else:
            tickets = random.sample(numbers, k=quantity) # Випадкові унікальні числа з діапазону
            return sorted(tickets) # Повертаємо відсортований список
    
try:
    print(get_numbers_ticket(min, max, quantity))
except NameError:
    pass

# В останньому блоці додав try-except-pass, оскільки при спробі введення літери 
#  Видає помилку: NameError: name 'quantity' is not defined. Не зміг зрозуміти причину помилки





    