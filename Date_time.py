from datetime import date, time, datetime
import pytz

pk=pytz.timezone("Asia/Karachi")
today = date.today()
now = datetime.now()

print("Today's date is", today)
print("\n Current date and time is", now)

print("\n Date components", today.day, today.month, today.year)


