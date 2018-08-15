# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
from pkg_resources import get_distribution

import sys
import configparser
import pkg_resources
import ast

try:
    import __builtin__ as bi
except BaseException:
    import builtins as bi




class DefaultMenus():

    plugin_list = {}
    config = []
    emodules = []
    nmodules = []
    pmodules = []
    snmodules = []
    plmodules = []

    default_items = [
        {'key':'all', 'text':'All - Run all modules associated with this group'},
        {'key':'back', 'text':'Back - Return to main menu'},
        {'key':'exit', 'text':'Exit - Terminate the application'}
    ]

    ltypes = [
        {'key':'email', 'text':'Email - Search targets by email address'},
        {'key':'name', 'text':'Name - Search targets by First Last name combination'},
        {'key':'phone', 'text':'Phone - Search targets by telephone number'},
        {'key':'screen', 'text':'Screen Name - Search targets by known alias'},
        {'key':'license', 'text':'License Plate - Search targets by license plate'},
        {'key':'profiler', 'text':'Profiler - A "Guess Who" Q&A interactive user interface'},
        {'key':'help', 'text':'Help - Details the application and use cases'},
        {'key':'exit', 'text':'Exit - Terminate the application'}
    ]


    def __init__(self, plugins):
        """
        Get a list of plugins
        """
        self.plugin_list = plugins
        self.config = configparser.ConfigParser()
        get_plugin_cats = pkg_resources.resource_filename('skiptracer','../../setup.cfg')
        self.config.read(get_plugin_cats)


    def useproxy(self):
        """
        Generate a new proxy
        for masking requests
        """
        if str(bi.webproxy).lower() == "y":
            bi.proxy = pg.new_proxy()
            return True
        else:
            return False


    def helpmenu(self):
        """
        Display help text
        to user
        """
        print("Skiptracer")


    def intromenu(self):
        """
        Top level intro menu
        """
        bi.search_string = ''
        bi.lookup = ''
        if self.useproxy():
            print("\t  [" + bc.CRED + "::ATTENTION::" + bc.CEND + "]" +
                bc.CYLW + " Proxied requests are unreliable " + bc.CEND +
                "[" + bc.CRED + "::ATTENTION::" + bc.CEND + "]")

        gselect = ""
        for i,v in enumerate(self.ltypes):
            print('['+str(i+1)+'] -' + self.ltypes[i]['text'])

        try:
            selection = int(input("[!] Lookup menu - Please select a number:"))
            gselect = self.ltypes[selection-1]['key']
        except Exception as failselect:
            print("Please use an integer value for your selection!")

        if gselect == "":
            self.intromenu()
        if gselect == "exit":
            sys.exit()
        if gselect == "email":
            self.emailmenu()
        if gselect == "name":
            self.namemenu()
        if gselect == "phone":
            self.phonemenu()
        if gselect == "screen":
            self.snmenu()
        if gselect == "license":
            self.platemenu()
        if gselect == "profiler":
            self.profiler()
        if gselect == "help":
            self.helpmenu()


    def grabplugins(self, plugin_type, plugin_list):
        """
        Grab a list of relevant plugins.
        plugin_type = ref to variable to store list of plugin modules
        plugin_list = the list from the setup.cfg to use
        """
        for i in plugin_list:
            tc = ast.literal_eval(plugin_list[i])
            plugin_type.append({'key': i, 'text': tc[0] + " - " + tc[1]})

        plugin_type = plugin_type + self.default_items


    def grabuserchoice(self, plugin_type, textsub):
        """
        Function to grab user choice.
        plugin_type = var with list of plugin modules
        textsub = String to display in menu e.g. Email, Name
        """
        gselect = ""

        print(" [!] "+textsub+" search menu - Please select a number")
        for i,v in enumerate(plugin_type):
            print(' ['+str(i+1)+'] -' + plugin_type[i]['text'])

        try:
            selection = int(input(" [!] Select a number to continue: "))
            gselect = plugin_type[selection-1]['key']
        except Exception as failselect:
            print("Please use an integer value for your selection!")

        return gselect


    def selectchoice(self, menu, mtype, error, plugins, gselect):
        """
        Select a menu item and then
        action it.
        """
        if gselect == "":
            menu()
        if gselect == "exit":
            sys.exit()
        if gselect == "back":
            self.intromenu()

        if not bi.search_string or bi.search_string == '':
            bi.search_string = input(error)

        print()
        print(bi.search_string)
        self.useproxy()
        if gselect != "all":
            self.plugin_list[gselect]().get_info(bi.search_string, mtype)

        if gselect == "all":
            for i in plugins:
                self.plugin_list[i]().get_info(bi.search_string, mtype)
        menu()


    def emailmenu(self):
        """
        Display the email modules to the
        user.
        """

        self.emodules = []
        self.grabplugins(self.emodules, self.config['plugins.email'])
        gselect = self.grabuserchoice(self.emodules, "E-Mail")

        self.selectchoice(
            self.emailmenu,
            "email",
            "[What is the marks email address? - ex: username@domain.tld]:",
            self.config['plugins.email'],
            gselect
        )

    def namemenu(self):
        """
        Print menu for
        name matching plugins
        """
        self.nmodules = []
        self.grabplugins(self.nmodules, self.config['plugins.name'])
        gselect = self.grabuserchoice(self.nmodules, "Name")

        self.selectchoice(
            self.namemenu,
            "name",
            "[What is the marks name? - ex: First Lastname]: ",
            self.config['plugins.name'],
            gselect
        )

    def phonemenu(self):
        """
        Display the phone
        menu to the user.
        """
        self.pmodules = []
        self.grabplugins(self.pmodules, self.config['plugins.phone'])
        gselect = self.grabuserchoice(self.pmodules, "Phone")
        self.selectchoice(
            self.phonemenu,
            "phone",
            "[What is the marks phone number? - ex: 1234567890]: ",
            self.config['plugins.phone'],
            gselect
        )

    def snmenu(self):
        """
        Screen Name grabbing tools menu
        """
        self.grabplugins(self.snmodules, self.config['plugins.screenname'])
        gselect = self.grabuserchoice(self.snmodules, "Screen Name")
        self.selectchoice(
            self.snmenu,
            "screenname",
            "[What is the marks screenname? - ex: (Ac1dBurn|Zer0Cool)]: ",
            self.config['plugins.screenname'],
            gselect
        )

    def platemenu(self):
        """
        Enter a plate number
        """
        self.grabplugins(self.plmodules, self.config['plugins.plate'])
        gselect = self.grabuserchoice(self.plmodules, "Plate Number")

        self.selectchoice(
            self.platemenu,
            "plate",
            "[What is the marks vehicle plate number? - ex: (XYZ123|0U812)]: ",
            self.config['plugins.plate'],
            gselect
        )

    def profiler(self):
        """
        Profiler output - guess who interactive interface
        """
        fname = input("\t[Whats the users first name? - ex: Alice]: ")
        lname = input("\t[Whats the users last name? - ex: Smith]: ")
        bi.name = fname + " " + lname
        bi.agerange = input("\t[Whats the marks age range? - ex: 18-100]: ")
        bi.apprage = input("\t[Whats the marks suspected age? - ex: 18]: ")
        bi.state = input(
            "\t[Whats state does the mark live in? - ex: (FL|Florida)]: ")
        bi.city = input(
            "\t[Whats city does the mark live in? - ex: Orlando]: ")
        bi.zip = input(
            "\t[Whats the zipcode the mark lives in? - ex: 12345]: ")
        bi.phone = input(
            "\t[What is a known phone number for the mark? - ex: 1234567890]: ")
        bi.screenname = input(
            "\t[What are the known aliasis of the mark? - ex: (Ac1dBurn|Zer0cool)]: ")
        bi.plate = input(
            "\t[Does the mark have a known license plate? - ex: (ABC1234|XYZ123)]: ")
        bi.email = input(
            "\t[What is the marks email address? - ex: username@domain.tld]: ")
