# -*- coding: utf-8 -*-
import sys
import datetime


class get_time():
    def __init__(self):
        self.now = datetime.datetime.now()

    def getnowstr(self):
        """Current date and time using str method of datetime object:"""
        print()
        print("Current date and time")
        print(str(self.now))

    def getnowattr(self):
        """Current date and time using instance attributes:"""
        print()
        print("Current date and time")
        print("Current year: %d" % self.now.year)
        print("Current month: %d" % self.now.month)
        print("Current day: %d" % self.now.day)
        print("Current hour: %d" % self.now.hour)
        print("Current minute: %d" % self.now.minute)
        print("Current second: %d" % self.now.second)
        print("Current microsecond: %d" % self.now.microsecond)

    def getnowstrftime(self):
        """Current date and time using strftime"""
        print()
        print("Current date and time")
        print(self.now.strftime("%m-%d-%Y %H:%M"))

    def getnowiso(self):
        """Current date and time using isoformat:"""
        print()
        print("Current date and time:")
        print(self.now.isoformat())

    def getnow(self):
        """Current date and time using today."""
        print()
        print("Current date:")
        print(datetime.date.today())
