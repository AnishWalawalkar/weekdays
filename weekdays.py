import datetime

def is_weekday(date):
    return True if date.weekday() in range(0, 5) else False

def weekdays_passed(start, end=datetime.datetime.now()):
    pass

def weekdays_until(end, start=datetime.datetime.now()):
    pass

def range_weekdays(start, end):
    while not start == end:
        if is_weekday(start):
            yield start
        start += datetime.timedelta(days=1)

def prev_weekdays(date, num_days=0):
    def inner(date):
        if is_weekday(date):
            return date

        day_count = 1 if date.weekday() == 5 else 2
        return date - datetime.timedelta(days=day_count)

    if not num_days:
        return inner(date)
    new_date = date - datetime.timedelta(days=num_days)
    return inner(new_date)

def next_weekday(date, num_days=0):
    def inner(date):
        if is_weekday(date):
            return date

        day_count = 2 if date.weekday() == 5 else 1
        return date + datetime.timedelta(days=day_count)

    if not num_days:
        return inner(date)

    new_date = date + datetime.timedelta(days=num_days)
    return inner(new_date)


