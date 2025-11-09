from datetime import date

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day   = int(input("Enter your birth day (1-31): "))

today = date.today()
age = today.year - birth_year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

print(f"You are {age} years old.")
