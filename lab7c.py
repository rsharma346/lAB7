#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second.
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def time_to_sec(time):
    """Convert a time object to a single integer representing seconds from midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def format_time(time):
    """Return a time object as a formatted string."""
    return f"{time.hour:02d}:{time.minute:02d}:{time.second:02d}"

def sum_times(t1, t2):
    """Add two time objects and return their sum."""
    seconds1 = time_to_sec(t1)
    seconds2 = time_to_sec(t2)
    total_seconds = seconds1 + seconds2
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Change a time object by adding a number of seconds."""
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second
    return None

