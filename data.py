from datetime import datetime
from datetime import timedelta
now = datetime.now()
date_first = datetime(2004, 1, 1) # <--- Tutaj wprowadź swoją datę urodzenia
day = now - date_first
print(day.days)