def is_working_day(day):
    if day == "Monday":
        return True
    elif day == "Sunday":
        return False
    elif day == "Saturday": 
        return False
    else:
        return True
