# from datetime import datetime
# import calendar
# now = datetime.now()
# print(now.strftime("%U"))

from datetime import datetime
import calendar
date_object = datetime.strptime("2023-11-15","%Y-%m-%d")
print(date_object.strftime("%U"))