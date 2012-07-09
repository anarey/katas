class NotDayFound(Exception):
    pass

def is_working_day(day):
    if day == "":
        raise NotDayFound

    if day == "Sunday" or day == "Saturday":
        return False
    return True
