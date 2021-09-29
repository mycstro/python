# -*- coding: utf-8 -*-
import sys
import datetime
from intro.datin.dates import format_dbirth as format_date



class Agein:
    def __init__(self, nam):
        ag = 1
        self._na1 = nam

    def age_getin(self):
        ag = int(input('How old are you?: '))
        if ag >= 21:
            print("Hope you had a wonderful childhood {}".format(self._na1))
        else:
            print("{0}! Wow your not even old enough to drink {1}.".format(ag, self._na1))
        print("Ok, Let's move on.")
        return ag


    def age_check(self, ages):
        bir_dat = input('Ok {}, When is your birthday? [MM/DD/YYYY]'.format(self._na1))
        self.birdat = format_date(bir_dat)
        self._by = self.birdat[2]
        now = datetime.datetime.now()
        spaou = now.year - self._by - 1
        if ages == spaou:
            return True
        else:
            return False

    def age_checkis(self, agechk):
        if agechk == False:
            print("Oops, we've found an error somewhere, \nLet's try again")
            self.age_getin()
