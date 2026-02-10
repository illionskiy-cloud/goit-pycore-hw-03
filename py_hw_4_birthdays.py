from datetime import date, datetime, timedelta

def get_upcoming_birthdays(users):
    today = date.today()
    upcoming = []
    
    for user in users:
        # Форматування рядка в об'єкт date
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()        
        # Встановлення дня народження на поточний рік
        birthday_this_year = birthday_date.replace(year=today.year)        
        # Якщо день народження вже минув цього року, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=today.year + 1)
        
        # Перевіряємо, чи день народження в найближчі 7 днів
        days_until_birthday = (birthday_this_year - today).days        
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            
            # Перевірка, чи припадає на вихідні            
            if birthday_this_year.weekday() == 5:  
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6: 
                congratulation_date = birthday_this_year + timedelta(days=1)
            
            upcoming.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    
    return upcoming



users = [
    {"name": "John Doe", "birthday": "1985.02.13"},
    {"name": "Jane Smith", "birthday": "1990.02.16"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)