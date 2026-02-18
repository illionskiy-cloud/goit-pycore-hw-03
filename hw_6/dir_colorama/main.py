import sys
from colorama import Fore, Style, init                             
from pathlib import Path

init()  # Ініціалізація colorama

if len(sys.argv) < 2:
    print('Введіть шлях до директорії')
    sys.exit()

path = Path(sys.argv[1])   
 
def print_tree(path, indent=0):

    # Обробка помилок
    if not path.exists() or not path.is_dir():
        print('Неправильний шлях до директорії')
        return None
    
    for el in path.iterdir():
        # Відступ через пробіли
        prefix = "  " * indent
        
        if el.is_dir():
            print(Fore.YELLOW + prefix + el.name + Style.RESET_ALL)
            print_tree(el, indent + 1)  # Рекурсія
        else:
            print(Fore.BLUE + prefix + el.name + Style.RESET_ALL)

print_tree(path)
