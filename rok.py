from datetime import datetime
# Wyświetl różnicę w dniach między 1 stycznia 2023 a dzisiaj
def dddd():
    now = datetime.now()
    past_date = datetime(2023, 1, 1)
    day = now - past_date
    return day.days

