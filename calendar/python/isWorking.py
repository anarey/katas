class NotDayFound(Exception):
    pass

class IncorrectDay(Exception):
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
    if day == "09/07/2012":
        return True
    else:
        return False
