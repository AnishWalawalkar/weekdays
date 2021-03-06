'''python module to work with weekdays'''
import time
from datetime import timedelta
from datetime import datetime

__all__ = [
    'is_weekday', 'weekdays_passed', 'weekdays_until',
    'date_range', 'prev_weekday', 'next_weekday', 'time_to_datetime'
]

def time_to_datetime(time_struct=None, time_in_seconds=None):
    '''heloper function to convert time object to datetime object'''
    if not  (time_struct or time_in_seconds):
        raise Exception(
            'One of "time_struct" or "time_in_seconds" keyword arguements must be provided')
    if time_struct:
        try:
            time_in_seconds = time.mktime(time_struct)
        except TypeError as e:
            raise Exception(e)
    return datetime.fromtimestamp(time_in_seconds)

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
    return ((end-start).days - daydiff) / 7 * 5 + min(daydiff, 5) - (max(end.weekday() - 4, 0) % 5)

def date_range(start, end):
    '''returns a generator that can be used to iterate over the weekdays in the range start to end-1'''
    if start > end:
        return
    while not start == end:
        if is_weekday(start):
            yield start
        start += timedelta(days=1)

def weekend_offset(date, flag=False):
    '''internal helper function'''
    if date.weekday() == 5:
        return 2 if flag else 1
    return 1 if flag else 2

def prev_weekday(date, num_days=1):
    '''return the previous weekday'''
    if num_days < 0:
        return date

    day_count = 0
    prev_day = date

    while day_count < num_days:
        prev_day -= timedelta(days=1)
        if is_weekday(prev_day):
            day_count += 1

    return prev_day

def next_weekday(date, num_days=1):
    '''return the next weekday'''
    if num_days < 0:
        return date

    day_count = 0
    next_day = date

    while day_count < num_days:
        next_day += timedelta(days=1)
        if is_weekday(next_day):
            day_count += 1

    return next_day
