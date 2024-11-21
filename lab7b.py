#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum_time = Time()
    sum_time.hour = t1.hour + t2.hour
    sum_time.minute = t1.minute + t2.minute
    sum_time.second = t1.second + t2.second

    # Handle carry-over for seconds and minutes
    if sum_time.second >= 60:
        sum_time.minute += sum_time.second // 60
        sum_time.second %= 60
    if sum_time.minute >= 60:
        sum_time.hour += sum_time.minute // 60
        sum_time.minute %= 60

    return sum_time

def valid_time(t):
    """Check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0
    """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):
    """Modify a time object by adding/subtracting seconds."""
    time.second += seconds

    # Handle positive overflow
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    # Handle negative overflow
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

