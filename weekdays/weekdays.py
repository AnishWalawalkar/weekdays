__all__ = [
    'is_weekday', 'weekdays_passed', 'weekdays_until',
    'range_weekdays', 'prev_weekdays', 'next_weekday'
]

import datetime


def is_weekday(date):
    '''Checks if the date provided as an arguement is a weekday or not'''
    return True if date.weekday() in range(0, 5) else False

def weekdays_passed(start, end):
    '''
    returns the numbers of weekdays between the start date and end date
    note: start > end
    '''
    return weekdays_until(end, start)

def weekdays_until(start, end):
    '''
    returns the numbers of weekdays between the start date and end date
    note : end > start
    '''
    if end < start:
        return 0
    daydiff = end.weekday() - start.weekday()
    return ((end-start).days - daydiff) / 7 * 5 + min(daydiff,5) - (max(end.weekday() - 4, 0) % 5)

def range_weekdays(start, end):
    '''returns a generator that can be used to iterate over the weekdays in the range start to end-1'''
    if start > end:
        return []
    while not start == end:
        if is_weekday(start):
            yield start
        start += datetime.timedelta(days=1)

def prev_weekday(date, num_days=0):
    '''returns "date" if "date" is a weekday else the previous weekday. num_days is used to specify "how many weekdays before current date"'''
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
    '''returns "date" if "date" is a weekday else the next weekday. num_days is used to specify "how many weekdays after current date"'''
    def inner(date):
        if is_weekday(date):
            return date

        day_count = 2 if date.weekday() == 5 else 1
        return date + datetime.timedelta(days=day_count)

    if not num_days:
        return inner(date)

    new_date = date + datetime.timedelta(days=num_days)
    return inner(new_date)
