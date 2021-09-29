#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import hashlib
import getpass
from menyou import getmenus as menu

class LogIn:

    def login_info(self):
        em0 = str(input('What is your email?: '))
        un0 = str(input('What will your user name be?: '))
        un1 = un0.lower()
        pwd0 = hashlib.sha224(getpass.getpass('Please Enter a Password: ')).hexdigest()
        pwd1 = ''
        while pwd1 != pwd0:
            pwd1 = hashlib.sha224(getpass.getpass('Please Re-Enter the Password: ')).hexdigest()
            if pwd1 == pwd0:
                print('Passwords Matched')
                return em0, un1, pwd0
            else:
                print("The passwords don't match please try again.")

class Pi:

    def personal_info(self):
        fn0 = str(input('What is your first name: '))
        fn1 = fn0[0]
        fn2 = fn0[1:]
        fn = fn1.upper()+ fn2
        mn0 = str(input('What is your middle name: '))
        mn1 = mn0[0]
        mn2 = mn0[1:]
        mn = mn1.upper()+ mn2
        ln0 = str(input('What is your last name: '))
        ln1 = ln0[0]
        ln2 = ln0[1:]
        ln = ln1.upper()+ ln2
        return fn, mn, ln

    def getwehe(self):
        wehe = menu.menu_wehe(p1=self.personal_info)
        return wehe

    def phon_num(self):
        # Takes a 10 digit input and presents it in the [(###) ###-####] format
        # Avoids mistakes & stupidity surrounding 10-digit phone numbers
        phonez = input('Phone number [555-235-5555]: ')
        areacode, prefix, suffix = map(int, phonez.split('-'))
        phone = areacode, prefix, suffix
        if (len(phone) == 10) and phone[
                                  0:len(phone)] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0":
            tp = "1 " + "(" + repr(areacode) + ")" + " " + repr(prefix) + "-" + repr(suffix)
        else:
            tp = "Only numerals are accepted in this field"
        return tp

    def locat(self):
        st = str(input('What is your street address?: '))
        cc = str(input('What is your current City?: '))
        cs = str(input('What is your current State? [ OR ]: '))
        bc = str(input('Which city was you born in?: '))
        bs = str(input('Which state was you born in? [ OR ]: '))
        return st, cc, cs, bc, bs

    def getgend(self):
        gend = menu.menu_gend()
        return gend

    ## def nationality(self):
