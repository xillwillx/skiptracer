# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
# [Experimental]
from plugins.twitter import TwitterGrabber
# [Experimental]
from plugins.fouroneone_info import FourOneOneGrabber
from plugins.who_call_id import WhoCallIdGrabber
from plugins.advance_background_checks import AdvanceBackgroundGrabber
from plugins.myspace import MySpaceGrabber
from plugins.whoismind import WhoisMindGrabber
from plugins.linkedin import LinkedInGrabber
from plugins.true_people import TruePeopleGrabber
from plugins.truthfinder import TruthFinderGrabber
from plugins.haveibeenpwned import HaveIBeenPwwnedGrabber
from plugins.namechk2 import NameChkGrabber
from plugins.plate import VinGrabber
from plugins.knowem import KnowemGrabber
from plugins.tinder import TinderGrabber
from plugins.colors import BodyColors as bc
import plugins.proxygrabber as pg
try:
    import __builtin__ as bi
except:
    import builtins as bi
import sys

bi.funclist = {
	'linkedin':LinkedInGrabber,
	'myspace':MySpaceGrabber,
	'haveibeenpwned':HaveIBeenPwwnedGrabber,
	'whoismind':WhoisMindGrabber,
	'truth':TruthFinderGrabber,
	'true':TruePeopleGrabber,
	'advancedbackgroundchecks':AdvanceBackgroundGrabber,
	'who':WhoCallIdGrabber,
	'four':FourOneOneGrabber,
	'twitter':TwitterGrabber,
	'knowem':KnowemGrabber,
	'namechk':NameChkGrabber,
	'tinder':TinderGrabber,
	'vin':VinGrabber
}

class menus():

  def help(self):
    print("Describe application here")

  def printfun(self,modules):
    keylist = list()
    for xmod in range(1,len(modules)+1):
     keylist.append(xmod)
    moddict = dict(zip(keylist,modules))
    for xmd in moddict.keys():
     print(("  [%s-%s] %s: %s") % (bc.CRED, bc.CEND, xmd, moddict[xmd]))
    try:
     selection = int(raw_input((" [{}!{}] Select a number to continue: ").format(bc.CRED,bc.CEND)))
     gselect = str(moddict[int(selection)].split()[0]).lower()
     return gselect
    except Exception as failselect:
     print((" [{}!{}] Please use an integer value for your selection").format(bc.CRED,bc.CEND))
     pass

  def intromenu(self):
    bi.search_string = ''
    bi.lookup = ''
    ltypes = [
	'{}Email{} - {}Search targets by email address{}'.format(bc.CRED, bc.CEND, bc.CYLW, bc.CEND),
	'{}Name{} - {}Search targets by First Last name combination{}'.format(bc.CRED, bc.CEND, bc.CYLW, bc.CEND),
	'{}Phone{} - {}Search targets by telephone number{}'.format(bc.CRED, bc.CEND, bc.CYLW, bc.CEND),
	'{}Screen Name{} - {}Search targets by known alias{}'.format(bc.CRED, bc.CEND, bc.CYLW, bc.CEND),
	'{}License Plate{} - {}Search targets by license plate{}'.format(bc.CRED, bc.CEND, bc.CYLW, bc.CEND),
	'{}Profiler{} - {}Interactive Q&A for bulk lookups{}'.format(bc.CRED, bc.CEND, bc.CYLW, bc.CEND),
	'{}Help{} - {}Details the application and use cases{}'.format(bc.CRED, bc.CEND, bc.CYLW, bc.CEND),
	'{}Exit{} - {}Terminate the application{}'.format(bc.CRED, bc.CEND, bc.CYLW, bc.CEND)]
    print(" [!] Lookup menu - Please select a number")
    gselect = self.printfun(ltypes)
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

  def emailmenu(self):
    emodules = [
	'All - Run all modules associated to the email module group',
	'LinkedIn - Check if user exposes information through LinkedIn',
	'HaveIBeenPwned - Check email against known compromised networks',
	'Myspace - Check if users account has a registered account',
	'WhoisMind - Check email to registered domains',
	'AdvancedBackgroundChecks - Run email through public page of paid access',
	'Back - Return to main menu',
	'Exit - Terminate the application']
    print(" [!] E-Mail search menu - Please select a number")
    gselect = self.printfun(emodules)
    if gselect == "":
     self.emailmenu()
    if gselect == "exit":
     sys.exit()
    if gselect == "back":
     self.intromenu()
    if not bi.search_string:
     bi.search_string = raw_input("[What is the target's email address? - ex: username@domain.tld]: ")
    if bi.search_string == '':
     bi.search_string = raw_input("[What is the target's email address? - ex: username@domain.tld]: ")
    bi.lookup = "email"
    print()
    if gselect != "all":
     try:
      bi.funclist[gselect]().get_info(bi.search_string)
     except:
      bi.funclist[gselect]().get_info(bi.lookup,bi.search_string)
    if gselect == "all":
     LinkedInGrabber().get_info(bi.search_string)
     MySpaceGrabber().get_info(bi.search_string)
     HaveIBeenPwwnedGrabber().get_info(bi.search_string)
     WhoisMindGrabber().get_info(bi.search_string)
     AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
    self.emailmenu()

  def namemenu(self):
    nmodules = [
	'All - Run all modules associated to the email module group',
	'Truth Finder - Run name through public page of paid access',
	'True People - Run email through public page of paid access',
	'AdvancedBackgroundChecks - Run email through public page of paid access',
	'Back - Return to main menu',
	'Exit - Terminate the application']
    gselect = self.printfun(nmodules)
    if gselect == "":
     self.namemenu()
    if gselect == "exit":
     sys.exit()
    if gselect == "back":
     self.intromenu()
    if not bi.search_string:
     bi.search_string = raw_input("[What is the target's name? - ex: FirstName LastName]: ")
    if bi.search_string == '':
     bi.search_string = raw_input("[What is the target's name? - ex: FirstName LastName]: ")
    bi.lookup = 'name'
    print()
    if gselect != "all":
     try:
      bi.funclist[gselect]().get_info(bi.search_string)
     except:
      bi.funclist[gselect]().get_info(bi.lookup,bi.search_string)
    if gselect == "all":
     TruthFinderGrabber().get_info(bi.lookup,bi.search_string)
     TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
     AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
    self.namemenu()

  def phonemenu(self):
    pmodules = [
	'All - Run all modules associated to the phone module group',
	'TruePeopleSearch - Run email through public page of paid access',
	'WhoCalld - Reverse phone trace on given number',
	'411 - Reverse phone trace on given number',
	'AdvancedBackgroundChecks - Run number through public page of paid access',
	'Back - Return to main menu',
	'Exit - Terminate the application']
    gselect = self.printfun(pmodules)
    if gselect == "":
     self.phonemenu()
    if gselect == "exit":
     sys.exit()
    if gselect == "back":
     self.intromenu()
    if not bi.search_string:
     bi.search_string = raw_input("[What is the marks phone number? - ex: 1234567890]: ")
    if bi.search_string == '':
     bi.search_string = raw_input("[What is the marks phone number? - ex: 1234567890]: ")
    bi.lookup = 'phone'
    print()
    if gselect != "all":
     try:
      bi.funclist[gselect]().get_info(bi.search_string)
     except:
      bi.funclist[gselect]().get_info(bi.lookup,bi.search_string)
    if gselect == "all":
     TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
     WhoCallIdGrabber().get_info(bi.search_string)
     FourOneOneGrabber().get_info(bi.search_string)
     AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
    self.phonemenu()

  def snmenu(self):
    snmodules = [
	'All - Run all modules associated to the email module group',
	'Twitter - Run screenname and grab tweets',
	'Knowem - Run screenname through to determin registered sites',
	'NameChk - Run screenname through to determin registered sites',
	'Tinder - Run screenname and grab information if registered',
	'Back - Return to main menu',
	'Exit - Terminate the application']
    gselect = self.printfun(snmodules)
    if gselect == "":
     self.snmenu()
    if gselect == "exit":
     sys.exit()
    if gselect == "back":
     self.intromenu()
    if not bi.search_string:
     bi.search_string = raw_input("[What is the target's screenname? - ex: (Ac1dBurn|Zer0Cool)]: ")
    if bi.search_string == '':
     bi.search_string = raw_input("[What is the target's screenname? - ex: (Ac1dBurn|Zer0Cool)]: ")
    bi.lookup = 'sn'
    print()
    if gselect != "all":
     try:
      bi.funclist[gselect]().get_info(bi.search_string)
     except:
      bi.funclist[gselect]().get_info(bi.lookup,bi.search_string)
    if gselect == "all":
     TwitterGrabber().get_info(bi.search_string)
     KnowemGrabber().get_info(bi.search_string)
     NameChkGrabber().get_info(bi.search_string)
     TinderGrabber().get_info(bi.search_string)
    self.snmenu()

  def platemenu(self):
    try:
        platemenu = [
        'All - Run all modules associated to the email module group',
        'Plate Search - Run known vehicle plates against a database',
        'Back - Return to main menu',
        'Exit - Terminate the application']
        gselect = self.printfun(platemenu)
    except Exception as e:
        print(e)
    if gselect == "":
     self.platemenu()
    if gselect == "exit":
     sys.exit()
    if gselect == "back":
     self.intromenu()
    if not bi.search_string:
     bi.search_string = raw_input("[What is the target's vehicle plate number? - ex: (XYZ123|0U812)]: ")
    if bi.search_string == '':
     bi.search_string = raw_input("[What is the target's vehicle plate number? - ex: (XYZ123|0U812)]: ")
    if gselect == "exit":
     sys.exit()
    bi.lookup = 'plate'
    print()
    if gselect in ["plate","all"]:
      VinGrabber().get_info(bi.search_string)
    self.platemenu()

  def profiler(self):
    fname = raw_input("\t[Whats the target's first name? - ex: Alice]: ")
    lname = raw_input("\t[Whats the target's last name? - ex: Smith]: ")
    bi.name = fname+" "+lname
    bi.agerange = raw_input("\t[Whats the target's age range? - ex: 18-100]: ")
    bi.apprage = raw_input("\t[Whats the target's suspected age? - ex: 18]: ")
    bi.state = raw_input("\t[Whats state does the target's live in? - ex: (FL|Florida)]: ")
    bi.city = raw_input("\t[Whats city does the target's live in? - ex: Orlando]: ")
    bi.zip = raw_input("\t[Whats the zipcode the target's lives in? - ex: 12345]: ")
    bi.phone = raw_input("\t[What is a known phone number for the target's? - ex: 1234567890]: ")
    bi.screenname = raw_input("\t[What are the known aliasis of the target's? - ex: (Ac1dBurn|Zer0cool)]: ")
    bi.plate = raw_input("\t[Does the target's have a known license plate? - ex: (ABC1234|XYZ123)]: ")
    bi.email = raw_input("\t[What is the target's email address? - ex: username@domain.tld]: ")
    self.intromenu()
