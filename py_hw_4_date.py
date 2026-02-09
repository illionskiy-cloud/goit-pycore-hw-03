from datetime import datetime, date

# Поточна дата
today = date.today()

def get_days_from_today(date: str) -> int:
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        if date:
            delta_days = today.toordinal() - date.toordinal() # Різниця в днях
            return delta_days
    except ValueError:  # Виключення помилки формату дати
        print("Please provide a date in the format YYYY-MM-DD.")

        
print(get_days_from_today("2024-01-01"))

