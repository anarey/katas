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

    is_working = ""
    if (day == "Sunday" 
      or day == "Saturday"):
        is_working =  False
    elif (day == "Monday" 
      or day == "Tuesday" 
      or day == "Wednesday" 
      or day == "Tuesday" 
      or day == "Friday"):
        is_working = True
    elif day == "":
        raise NotDayFound
    else:
        raise IncorrectDay
    
    return is_working

def is_working_date(day):
    
    pattern = re.compile("\d{2}/\d{2}/\d{4}")

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
