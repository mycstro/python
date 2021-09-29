# -*- coding: utf-8 -*-
import time
import processCommand as pac
from progress.progress1bar import ProgressBar
from dbMySql.conMySql import ConnDB as cdb
from intro.pii import pis
from intro.agin import agins
from miloSystems.timin import gettimin


def getin_height(hes):
    try:
        heig = pac.cvert_fttoin(hes)
        return heig
    except IndexError:
        he = hes[1]
        return he


def getin_weight(wes):
    we = wes[0]
    return we


def gettin_login():
    l01 = pis.LogIn()
    logininfo = l01.login_info()
    _em = logininfo[0]
    _un = logininfo[1]
    _pa = logininfo[2]
    print("Let's build your profile....")

    p01 = pis.Pi()
    personalinfo = p01.personal_info()
    _na = personalinfo[0]
    _mi = personalinfo[1]
    _la = personalinfo[2]
    print("Hello, It's a pleasure to meet you {} {} {}".format(_na, _mi, _la))

    p02 = agins.Agein(_na)
    _ag = p02.age_getin()  ## user inputed age
    _ac = p02.age_check(_ag)  ## system predicted age of user
    if _ac:
        print("Thank you for your honesty {}".format(_na))
    else:
        print("You should be more honest.")
    p02.age_checkis(_ac)  ## Is there a match

    wehe = p01.getwehe()
    hei = wehe[1]
    wei = wehe[0]
    if wei == 'None':
        if hei == 'None':
            print("No information provided")
        elif int(hei) in range(1, 998):
            wehes = pac.cvert_intoft(hei)
            feets, inchs = map(int, str(wehes).split('.'))
            print('''Your height is {0}'{1}".'''.format(feets, inchs))
    if wei in range(1, 998):
        if hei == 'None':
            print("Your weight is {}lbs.".format(wei))
        elif int(hei) in range(1, 998):
            wehes = pac.cvert_intoft(hei)
            feets, inchs = map(int, str(wehes).split('.'))
            print('''Your height and weight is {0}lbs, {1}'{2}".'''.format(wei, feets, inchs))

    _ph = p01.phon_num()
    print("Your phone number is {}".format(_ph))

    locateinfo = p01.locat()
    _sa = locateinfo[0]
    _ca = locateinfo[1]
    _as = locateinfo[2]
    print("Current location: {} {}, {}".format(_sa, _ca, _as))

    _co = locateinfo[3]
    _so = locateinfo[4]
    print("You were born in {}, {}".format(_co, _so))

    gende = p01.getgend()
    print(gende)

    # ntnlty = p01.nationality()
    # print(ntnlty)


def main():
    gettin_login()


if __name__ == "__main__":
    main()
