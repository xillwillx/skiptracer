# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
import click
# [Experimental]
from plugins.twitter import TwitterGrabber
# [Experimental]
from plugins.fouroneone_info import FourOneOneGrabber
from plugins.who_call_id import WhoCallIdGrabber
from plugins.advance_background_checks import AdvanceBackgroundGrabber
from plugins.myspace import MySpaceGrabber
from plugins.whoismind import WhoisMindGrabber
from plugins.linkedin import LinkedInSalesGrabber
from plugins.true_people import TruePeopleGrabber
from plugins.truthfinder import TruthFinderGrabber
from plugins.haveibeenpwned import HaveIBeenPwwnedGrabber
from plugins.hackedemails import HackedEmailGrabber
from plugins.namechk2 import NameChkGrabber
from plugins.plate import VinGrabber
from plugins.knowem import KnowemGrabber
from plugins.tinder import TinderGrabber
import plugins.proxygrabber as pg
import sys
import signal

def signal_handler(signal, frame):
 print("")
 sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
try:
    import __builtin__ as bi
except:
    import builtins as bi
import ast
from plugins.colors import BodyColors as bc
bi.search_string = ''
bi.lookup = ''
bi.outdata = dict()
bi.webproxy = ""
bi.proxy = ""
bi.debug = False
def banner():
    print ("")
    print ("\t\t.▄▄ · ▄ •▄ ▪   ▄▄▄·▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄▄▄ .▄▄▄  ")
    print ("\t\t▐█ ▀. █▌▄▌▪██ ▐█ ▄█•██  ▀▄ █·▐█ ▀█ ▐█ ▌▪▀▄.▀·▀▄ █·")
    print ("\t\t▄▀▀▀█▄▐▀▀▄·▐█· ██▀· ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▪▄▐▀▀▄ ")
    print ("\t\t▐█▄▪▐█▐█.█▌▐█▌▐█▪·• ▐█▌·▐█•█▌▐█ ▪▐▌▐███▌▐█▄▄▌▐█•█▌")
    print(("\t\t       {},.-~*´¨¯¨`*·~-.¸{}-({}by{})-{},.-~*´¨¯¨`*·~-.¸{} \n").format(bc.CRED,bc.CYLW,bc.CCYN,bc.CYLW,bc.CRED,bc.CEND))
    print(("\t\t\t      {}▀ █ █ █▀▄▀█ {}█▀▀█ {}█▀▀▄ {}").format(bc.CBLU,bc.CRED,bc.CBLU,bc.CEND))
    print(("\t\t\t      {}█ █ █ █ ▀ █ {}█  █ {}█▀▀▄{}").format(bc.CBLU,bc.CRED,bc.CBLU,bc.CEND))
    print(("\t\t\t      {}▀ ▀ ▀ ▀   ▀ {}▀▀▀▀ {}▀▀▀ {}").format(bc.CBLU,bc.CRED,bc.CBLU,bc.CEND))
    print(("\t\t\t      {}  https://illmob.org {}\n").format(bc.CYLW,bc.CEND))

banner()

def intromenu():
  bi.search_string = ''
  bi.lookup = ''
  if str(bi.webproxy).lower() == "y":  # If true, call proxygrabber.new_proxy(), set new proxy address to bi.proxy, else set to ""
   print ("\t  ["+bc.CRED+"::ATTENTION::"+bc.CEND+"]"+bc.CYLW+" Proxied requests are unreliable "+bc.CEND+"["+bc.CRED+"::ATTENTION::"+bc.CEND+"]")
   bi.proxy = pg.new_proxy()
  ltypes = ['Email - Search targets by email address',
           'Name - Search targets by First Last name combination',
           'Phone - Search targets by telephone number',
           'Screen Name - Search targets by known alias',
           'License Plate - Search targets by license plate',
           'Profiler - A "Guess Who" Q&A interactive user interface',
           'Help - Details the application and use cases',
           'Exit - Terminate the application']
  keylist = list()
  for xmod in range(1,len(ltypes)+1):
   keylist.append(xmod)
  moddict = dict(zip(keylist,ltypes))
  print(" [!] Lookup menu - Please select a number")
  for xmd in moddict.keys():
   print(("  [-] %s: %s") % (xmd, moddict[xmd]))
  try:
   selection = raw_input(" [!] Select a number to continue: ")
   gselect = str(moddict[int(selection)].split()[0]).lower()
  except Exception as failselect:
   print (("Please use an integer value for your selection!: %s") % failselect)
   intromenu()
  if gselect == "":
   intromenu()
  if gselect == "exit":
   sys.exit()
  if gselect == "email":
   emailmenu()
  if gselect == "name":
   namemenu()
  if gselect == "phone":
   phonemenu()
  if gselect == "screen":
   snmenu()
  if gselect == "license":
   platemenu()
  if gselect == "profiler":
   profiler()
  if gselect == "help":
   helpmenu()

def emailmenu():
  if str(bi.webproxy).lower() == "y":  # If true, call proxygrabber.new_proxy(), set new proxy address to bi.proxy, else set to ""
   bi.proxy = pg.new_proxy()
  emodules = ['Hacked Email - Check email against known compromised networks',
              'LinkedIn-Sales - Check if user exposes information through LinkedIn',
              'HaveIBeenPwned - Check email against known compromised networks',
              'Myspace - Check if users account has a registered account',
              'WhoisMind - Check email to registered domains',
              'AdvancedBackgroundChecks - Run email through public page of paid access',
              'All - Run all modules associated to the email module group',
              'Back - Return to main menu',
              'Exit - Terminate the application']
  keylist = list()
  for xmod in range(1,len(emodules)+1):
   keylist.append(xmod)
  moddict = dict(zip(keylist,emodules))
  print(" [!] E-Mail search menu - Please select a number")
  for xmd in moddict.keys():
   print(("  [-] %s: %s") % (xmd, moddict[xmd]))
  try:
   selection = int(raw_input(" [!] Select a number to continue: "))
   gselect = str(moddict[int(selection)].split()[0]).lower()
  except Exception as failselect:
   print(("Please use an integer value for your selection!: %s") % failselect)
   emailmenu()
  if gselect == "":
   emailmenu()
  gselect = str(moddict[int(selection)].split()[0]).lower()
  if gselect == "exit":
   sys.exit()
  if gselect == "back":
   intromenu()
  if not bi.search_string:
   bi.search_string = raw_input("[What is the marks email address? - ex: username@domain.tld]: ")
  bi.lookup = lookup
  print()
  if gselect == "hacked":
   print("Hacked Email Module")
   HackedEmailGrabber().get_info(bi.search_string)
  if gselect == "linkedin-sales":
   print("LinkedIn Module")
   LinkedInSalesGrabber().get_info(bi.search_string)
  if gselect == "haveibeenpwned":
   print("HaveIBeenPwned Module")
   HaveIBeenPwwnedGrabber().get_info(bi.search_string)
  if gselect == "myspace":
   print("Myspace Module")
   MySpaceGrabber().get_info(bi.search_string)
  if gselect == "whoismind":
   print("WhoisMind Module")
   WhoisMindGrabber().get_info(bi.search_string)
  if gselect == "advancedbackgroundchecks":
   print("AdvancedBackgroundChecks Module")
   AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
  if gselect == "all":
   HackedEmailGrabber().get_info(bi.search_string)
   LinkedInSalesGrabber().get_info(bi.search_string)
   MySpaceGrabber().get_info(bi.search_string)
   HaveIBeenPwwnedGrabber().get_info(bi.search_string)
   WhoisMindGrabber().get_info(bi.search_string)
   AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
  emailmenu()

def namemenu():
  if str(bi.webproxy).lower() == "y":  # If true, call proxygrabber.new_proxy(), set new proxy address to bi.proxy, else set to ""
   bi.proxy = pg.new_proxy()
  nmodules = ['Truth Finder - Run name through public page of paid access',
              'True People - Run email through public page of paid access',
              'AdvancedBackgroundChecks - Run email through public page of paid access',
              'All - Run all modules associated to the email module group',
              'Back - Return to main menu',
              'Exit - Terminate the application']
  keylist = list()
  for xmod in range(1,len(nmodules)+1):
   keylist.append(xmod)
  moddict = dict(zip(keylist,nmodules))
  print(" [!] Name search menu - Please select a number")
  for xmd in moddict.keys():
   print(("  [-] %s: %s") % (xmd, moddict[xmd]))
  try:
   selection = raw_input(" [!] Select a number to continue: ")
   gselect = str(moddict[int(selection)].split()[0]).lower()
  except Exception as failselect:
   print("Please use an integer value for your selection!")
   namemenu()
  if gselect == "":
   namemenu()
  if gselect == "exit":
   sys.exit()
  if gselect == "back":
   intromenu()
  if not bi.search_string:
   bi.search_string = raw_input("[What is the marks name? - ex: First Lastname]: ")
  bi.lookup = 'name'
  print()
  if gselect == "truth":
   print("TruthFinder Module")
   TruthFinderGrabber().get_info(bi.lookup,bi.search_string)
  if gselect == "true":
   print("TruePeople Module")
   TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
  if gselect == "advancedbackgroundchecks":
   print("TruePeople Module")
   AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
  if gselect == "all":
   print("All Name Modules")
   TruthFinderGrabber().get_info(bi.lookup,bi.search_string)
   TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
   AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
  namemenu()

def phonemenu():
  if str(bi.webproxy).lower() == "y":  # If true, call proxygrabber.new_proxy(), set new proxy address to bi.proxy, else set to ""
   bi.proxy = pg.new_proxy()
  pmodules = ['True People - Run email through public page of paid access',
              'Who Called - Reverse telehone trace on given number',
              'Four One One - Reverse telehone trace on given number',
              'Adv. Bkgnd. Chks - Run number through public page of paid access',
              'All - Run all modules associated to the phone module group',
              'Back - Return to main menu',
              'Exit - Terminate the application']
  keylist = list()
  for xmod in range(1,len(pmodules)+1):
   keylist.append(xmod)
  moddict = dict(zip(keylist,pmodules))
  print(" [!] Phone search menu - Please select a number")
  for xmd in moddict.keys():
   print(("  [-] %s: %s") % (xmd, moddict[xmd]))
  try:
   selection = raw_input(" [!] Select a number to continue: ")
   gselect = str(moddict[int(selection)].split()[0]).lower()
  except Exception as failselect:
   print("Please use an integer value for your selection!")
   phonemenu()
  if gselect == "":
   phonemenu()
  if gselect == "exit":
   sys.exit()
  if gselect == "back":
   intromenu()
  if not bi.search_string:
   bi.search_string = raw_input("[What is the marks phone number? - ex: 1234567890]: ")
  bi.lookup = 'phone'
  print()
  if gselect == "true":
   print("True People Module")
   TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
  if gselect == "who":
   print("Who Call ID Module")
   WhoCallIdGrabber().get_info(bi.search_string)
  if gselect == "four":
   print("411 Info Module")
   FourOneOneGrabber().get_info(bi.search_string)
  if gselect == "adv.":
   print("AdvancedBackgroundChecks Module")
   AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
  if gselect == "all":
   print("All Name Modules")
   TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
   WhoCallIdGrabber().get_info(bi.search_string)
   FourOneOneGrabber().get_info(bi.search_string)
   AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
  phonemenu()


def snmenu():
  if str(bi.webproxy).lower() == "y":  # If true, call proxygrabber.new_proxy(), set new proxy address to bi.proxy, else set to ""
   bi.proxy = pg.new_proxy()
  snmodules = ['Twitter - Run screenname and grab tweets',
              'Knowem - Run screenname through to determin registered sites',
              'NameChk - Run screenname through to determin registered sites',
              'Tinder - Run screenname and grab information if registered',
              'All - Run all modules associated to the email module group',
              'Back - Return to main menu',
              'Exit - Terminate the application']
  keylist = list()
  for xmod in range(1,len(snmodules)+1):
   keylist.append(xmod)
  moddict = dict(zip(keylist,snmodules))
  print(" [!] ScreenName search menu - Please select a number")
  for xmd in moddict.keys():
   print(("  [-] %s: %s") % (xmd, moddict[xmd]))
  try:
   selection = raw_input(" [!] Select a number to continue: ")
   gselect = str(moddict[int(selection)].split()[0]).lower()
  except Exception as failselect:
   print("Please use an integer value for your selection!")
   snmenu()
  if gselect == "":
   snmenu()
  if gselect == "exit":
   sys.exit()
  if gselect == "back":
   intromenu()
  if not bi.search_string:
   bi.search_string = raw_input("[What is the marks screenname? - ex: (Ac1dBurn|Zer0Cool)]: ")
  bi.lookup = 'sn'
  print()
  if gselect == "twitter":
   print("Twitter Module")
   TwitterGrabber().get_info(bi.search_string)
  if gselect == "knowem":
   print("Knowem Module")
   KnowemGrabber().get_info(bi.search_string)
  if gselect == "namechk":
   print("NameChk Module")
   NameChkGrabber().get_info(bi.search_string)
  if gselect == "tinder":
   print("Tinder Module")
   TinderGrabber().get_info(bi.search_string)
  if gselect == "all":
   print("All Screenname Modules")
   TwitterGrabber().get_info(bi.search_string)
   KnowemGrabber().get_info(bi.search_string)
   NameChkGrabber().get_info(bi.search_string)
   TinderGrabber().get_info(bi.search_string)
  snmenu()

def platemenu():
  if str(bi.webproxy).lower() == "y":  # If true, call proxygrabber.new_proxy(), set new proxy address to bi.proxy, else set to ""
   bi.proxy = pg.new_proxy()
  plmodules = ['Plate Search - Run known vehicle plates against a database',
              'All - Run all modules associated to the email module group',
              'Back - Return to main menu',
              'Exit - Terminate the application']
  keylist = list()
  for xmod in range(1,len(plmodules)+1):
   keylist.append(xmod)
  moddict = dict(zip(keylist,plmodules))
  print(" [!] Plate search menu - Please select a number")
  for xmd in moddict.keys():
   print(("  [-] %s: %s") % (xmd, moddict[xmd]))
  try:
   selection = raw_input(" [!] Select a number to continue: ")
   gselect = str(moddict[int(selection)].split()[0]).lower()
  except Exception as failselect:
   print("Please use an integer value for your selection!")
   platemenu()
  if gselect == "":
   platemenu()
  if gselect == "exit":
   sys.exit()
  if gselect == "back":
   intromenu()
  if not bi.search_string:
   bi.search_string = raw_input("[What is the marks vehicle plate number? - ex: (XYZ123|0U812)]: ")
  if gselect == "exit":
   sys.exit()
  bi.lookup = 'plate'
  print()
  if gselect in ["plate","all"]:
    VinGrabber().get_info(bi.search_string)
  platemenu()

def profiler():
  fname = raw_input("\t[Whats the users first name? - ex: Alice]: ")
  lname = raw_input("\t[Whats the users last name? - ex: Smith]: ")
  bi.name = fname+" "+lname
  bi.agerange = raw_input("\t[Whats the marks age range? - ex: 18-100]: ")
  bi.apprage = raw_input("\t[Whats the marks suspected age? - ex: 18]: ")
  bi.state = raw_input("\t[Whats state does the mark live in? - ex: (FL|Florida)]: ")
  bi.city = raw_input("\t[Whats city does the mark live in? - ex: Orlando]: ")
  bi.zip = raw_input("\t[Whats the zipcode the mark lives in? - ex: 12345]: ")
  bi.phone = raw_input("\t[What is a known phone number for the mark? - ex: 1234567890]: ")
  bi.screenname = raw_input("\t[What are the known aliasis of the mark? - ex: (Ac1dBurn|Zer0cool)]: ")
  bi.plate = raw_input("\t[Does the mark have a known license plate? - ex: (ABC1234|XYZ123)]: ")
  bi.email = raw_input("\t[What is the marks email address? - ex: username@domain.tld]: ")

def writeout():
 if str(bi.output).lower() == "y":  # If true, import JSON, dump data, write bi.outdata to given file name -o FILENAME
  import json
  try:
   pg.write_file(json.dumps(bi.outdata), output)
   print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+" Output written to disk: ./%s\n"+bc.CEND) % output)
  except Exception as nowriteJSON:
   if bi.debug: 
    print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND) % nowriteJSON)
   else:
    print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND)

if __name__ == "__main__":  # If true, run main function of framework
 try:
  bi.webproxy = raw_input("[Do we wish to enable proxy support? (Y/n)]: ")
  bi.output = raw_input("[Do we wish to save returned data to disk? (Y/n)]: ")
 except:
   pass
 intromenu()
 writout()

