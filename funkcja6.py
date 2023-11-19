from datetime import datetime

roznica = (datetime.now())-(datetime.strptime("01/01/1900 00:00", "%d/%m/%Y %H:%M"))
print (roznica)
