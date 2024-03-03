import datetime

year = int(input("Enter the year of birth (YYYY): "))
month = int(input("Enter the month of birth (MM): "))
day = int(input("Enter the day of birth (DD): "))

date = datetime.date(year, month, day)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(days[date.weekday()])
