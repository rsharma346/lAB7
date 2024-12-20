#!/usr/bin/env python3
# Student ID: [seneca_id]
class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def time_to_sec(self):
        """Convert a time object to a single integer representing the number of seconds from midnight"""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check if the time object attributes are valid"""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object"""
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour % 24, minute, second)

