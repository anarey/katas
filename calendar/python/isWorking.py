import calendar
import re

class NotDayFound(Exception):
    pass

class IncorrectDay(Exception):
    pass

class NotDateFound(Exception):
    pass

class IncorrectDate(Exception):
    pass

def is_working_day(day):

    working_days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday"]
    non_working_days = ["Saturday", "Sunday"]
    is_working = ""
    
    if day in non_working_days:
        is_working =  False
    elif day in working_days:
        is_working = True
    elif day == "":
        raise NotDayFound
    else:
        raise IncorrectDay
    
    return is_working

def is_working_date(day):
    
    pattern = re.compile("\d{2}/\d{2}/\d{4}")

# TODO Refactorizar con expresion regular solo introducir
# 1-31 en dias y 1-12 en mes.
# Este patron falla por los 05/06/2023
#    pattern = re.compile("0?[1-31]/0?[1-12]/\d{4}")

    if not pattern.match(day): 
        if day == "":
            raise NotDateFound
        else: 
            raise IncorrectDate

    day, month, year = day.split("/")
    
    try:
        day_week = calendar.weekday(int(year), int(month), int(day))
    except   ValueError:
        raise IncorrectDate
    if day_week >= 0 and day_week <= 4:
        return True
    else:
        return False

def is_working_range(day_start, day_end):
    return [False, True, True, True]
