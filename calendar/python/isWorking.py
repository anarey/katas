class NotDayFound(Exception):
    pass

class IncorrectDay(Exception):
    pass

def is_working_day(day):
    if day == "":
        raise NotDayFound

    if (day != "Monday" 
        and  day != "Tuesday" 
        and  day != "Wednesday" 
        and day != "Tuesday" 
        and day != "Friday" 
        and day != "Saturday" 
        and day != "Sunday"):
            raise IncorrectDay
    
    if day == "Sunday" or day == "Saturday":
        return False
    return True
