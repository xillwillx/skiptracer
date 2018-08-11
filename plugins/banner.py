# -*- coding: utf-8 -*-
from __future__ import print_function
from plugins.colors import BodyColors as bc


class Logo:

    def __init__(self):
        pass

    def banner(self):
        print("")
        print("\t\t.▄▄ · ▄ •▄ ▪   ▄▄▄·▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄▄▄ .▄▄▄  ")
        print("\t\t▐█ ▀. █▌▄▌▪██ ▐█ ▄█•██  ▀▄ █·▐█ ▀█ ▐█ ▌▪▀▄.▀·▀▄ █·")
        print("\t\t▄▀▀▀█▄▐▀▀▄·▐█· ██▀· ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▪▄▐▀▀▄ ")
        print("\t\t▐█▄▪▐█▐█.█▌▐█▌▐█▪·• ▐█▌·▐█•█▌▐█ ▪▐▌▐███▌▐█▄▄▌▐█•█▌")
        print(
            ("\t\t       {},.-~*´¨¯¨`*·~-.¸{}-({}by{})-{},.-~*´¨¯¨`*·~-.¸{} \n").format(
                bc.CRED,
                bc.CYLW,
                bc.CCYN,
                bc.CYLW,
                bc.CRED,
                bc.CEND))
        print(
            ("\t\t\t      {}▀ █ █ █▀▄▀█ {}█▀▀█ {}█▀▀▄ {}").format(
                bc.CBLU,
                bc.CRED,
                bc.CBLU,
                bc.CEND))
        print(
            ("\t\t\t      {}█ █ █ █ ▀ █ {}█  █ {}█▀▀▄{}").format(
                bc.CBLU,
                bc.CRED,
                bc.CBLU,
                bc.CEND))
        print(
            ("\t\t\t      {}▀ ▀ ▀ ▀   ▀ {}▀▀▀▀ {}▀▀▀ {}").format(
                bc.CBLU,
                bc.CRED,
                bc.CBLU,
                bc.CEND))
        print(("\t\t\t      {}  https://illmob.org {}\n").format(bc.CYLW, bc.CEND))

