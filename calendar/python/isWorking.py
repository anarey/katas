import calendar
import re
import datetime
import time

class NotDayFound(Exception):
    pass

class IncorrectDay(Exception):
    pass

class NotDateFound(Exception):
    pass

class IncorrectDate(Exception):
    pass

class IncorrectRange(Exception):
    pass
class InvalidDate(Exception):
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

def is_working_range(range_start, range_end):

    pattern = re.compile("\d{2}/\d{2}/\d{4}")

    if not pattern.match(range_start) or not pattern.match(range_end):
        raise IncorrectRange

    day_s, month_s, year_s = range_start.split("/")
    day_e, month_e, year_e = range_end.split("/")
    day_start = datetime.date(int(year_s), int(month_s), int(day_s))
    day_end = datetime.date(int(year_e), int(month_e), int(day_e))
    try:
        if time.mktime(day_start.timetuple()) > time.mktime(day_end.timetuple()):
            raise IncorrectRange
    except ValueError:
        raise InvalidDate

    range_working = []
    day = day_start
    finish_range = False
    one_day = datetime.timedelta(days=1)

    while (not finish_range):
        day_temp = day.strftime("%d/%m/%Y")
        is_working = is_working_date(day_temp)
        range_working.append(is_working)
        if day == day_end:
            finish_range = True
        else:
            day = day + one_day
        
    return range_working
