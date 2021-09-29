# -*- coding: utf-8 -*-
import sys

import menyou.menus as menyu
import menyou.choices as choice


def menu_wehe(p1):

    menyu.wehe_menu()    ## Displays menu
    choi = choice.WeHeChoices(p1) ##Display choices
    return choi

def menu_gend():
    menyu.gend_menu() ## Display menu
    choi = choice.GendChoices()
    return choi