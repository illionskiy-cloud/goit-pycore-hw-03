from datetime import datetime, date

# Поточна дата
today = date.today()

def get_days_from_today(date: str) -> int:
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        if date:
            delta_days = (today - date.date()).days # Різниця в днях
            return delta_days
    except ValueError:  # Виключення помилки формату дати
        print("Please provide a date in the format YYYY-MM-DD.")

        
print(get_days_from_today("2027-01-01"))

