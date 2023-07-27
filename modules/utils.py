from datetime import datetime as dt
import random

def validate_date(str_date):
    try:
        date = dt.strptime(str_date, "%d-%m-%Y %H:%M")
        if date.hour < 6: date = date.replace(hour=6)
        if date.hour > 22: date = date.replace(hour=22)
        return date
    except ValueError:
        return
    
def collect_date_range():
    start_date = validate_date(input("Fecha y hora de inicio de simulación (dd-mm-aa hh:mm): "))
    end_date = validate_date(input("Fecha y hora de fin de simulación (dd-mm-aa hh:mm): "))
    
    if(start_date is None or end_date is None or start_date > end_date):
        print("Alguna de las fechas introducidas es invalida")
        return collect_date_range()
    
    return {
        "start_date": start_date, 
        "end_date": end_date
    }

def getTrafficFlow(sense, date):
    if sense == "Norte":
        if int(date.date().strftime('%w')) >= 1 and int(date.date().strftime('%w')) <= 5:
            if date.hour >= 6 and date.hour <= 9:
                return 117
            elif date.hour >= 11 and date.hour <= 13:
                return 98
            elif date.hour >= 17 and date.hour <= 19:
                return 76
            else:
                return random.randint(76,117)
        else:
            if date.hour >= 7 and date.hour <= 9:
                return 105
            elif date.hour >= 4 and date.hour <= 22:
                return 54
            else:
                return random.randint(54, 105)
    elif sense == "Sur":
        if int(date.date().strftime('%w')) >= 1 and int(date.date().strftime('%w')) <= 5:
            if date.hour >= 6 and date.hour <= 9:
                return 119
            elif date.hour >= 11 and date.hour <= 13:
                return 105
            elif date.hour >= 17 and date.hour <= 19:
                return 120
            else:
                return random.randint(105, 120)
        else:
            if date.hour >= 7 and date.hour <= 9:
                return 107
            elif date.hour >= 4 and date.hour <= 22:
                return 80
            else:
                return random.randint(80, 107)