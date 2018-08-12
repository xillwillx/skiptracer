# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
# [Experimental]
from plugins.twitter import TwitterGrabber
# [Experimental]
from plugins.banner import Logo
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
import re, os, sys, signal

def signal_handler(signal, frame):
 print("")
 sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    import __builtin__ as bi
except:
    import builtins as bi

class menus():

  def helpmenu(self):
    try:
     os.system('clear')
     Logo().banner()
     print("\t[INFORMATION]::")
     print("""

This application is designed to query and parse 3rd party services in an automated fashion,
to increase productivity, while conducting a background investigation. This application
can be useful when trying to find hard to allocate targets. The following represent the types
of searches that can be performed.

\tEmail: 'Investigate with known email address'
\tName: 'Investigate with knwon First/Last name'
\tPhone: 'Investigate with known Phone Number'
\tScreenName: 'Investigate with known Screen Name'
\tPlate: 'Investigate with known License Plate'

Each of these catagories offers different modules that request 3rd party sites after the information
has been submitted by the user. for example the application may request a target email address.

Using these classifiers, can reveal additional information that can be utiized within the application.
These classifiers may reveal telephone, physicall address, or other useful data.

All modules included in the classifier may be run with the 'ALL' qualifier or individually. Additionally,
users can choose to reset the query string and continue using the same interface without having to restart
the application.

The following section will detail specifics about the modules offered for each classifier.

:: EMAIL ::
  Requires a user to supply a fully qualified Email address:

  -: Format: username@domain.tld

  This class of searches includes the following modules:

  -:  LinkedIn - Check if user exposes information through LinkedIn
  -:  HaveIBeenPwned - Check email against known compromised networks
  -:  Myspace - Check if users account has a registered account
  -:  WhoisMind - Check email to registered domains
  -:  AdvancedBackgroundChecks - Run email through public page of paid access




""")
     not raw_input("\nPress 'ENTER' key now to continue")
     self.intromenu()
    except Exception as helpfail:
     print(("Help failed: %s") & helpfail)

  def intromenu(self):
    bi.search_string = None
    bi.lookup = None
    os.system('clear')
    Logo().banner()
    print(" [{}!{}] {}Lookup menu:{}".format(bc.CYLW,bc.CEND,bc.CBLU, bc.CEND))
    print('\t[{}1{}] {}Email{} - {}Search targets by email address{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}2{}] {}Name{} - {}Search targets by First Last name combination{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}3{}] {}Phone{} - {}Search targets by telephone number{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}4{}] {}ScreenName{} - {}Search targets by known alias{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}5{}] {}Plate{} - {}Search targets by license plate{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}6{}] {}Profiler{} - {}Interactive Q&A for bulk lookups{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}7{}] {}Help{} - {}Details the application and use cases{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}8{}] {}Exit{} - {}Terminate the application{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    try:
     gselect = int(raw_input("[{}!{}] {}Select a number to continue:{} ".format(bc.CYLW,bc.CEND,bc.CBLU, bc.CEND)))
    except Exception as failintro:
     print("Failed Intro: %s" % failintro)
     self.intromenu()
    if gselect == 8:
     try:
      sys.exit(0)
     except Exception as noexit:
      sys.exit(0)
    else:
     try:
      if gselect == 1:
       self.emailmenu()
      if gselect == 2:
       self.namemenu()
      if gselect == 3:
       self.phonemenu()
      if gselect == 4:
       self.snmenu()
      if gselect == 5:
       self.platemenu()
      if gselect == 6:
       self.profiler()
      if gselect == 7:
       self.helpmenu()
     except:
      self.intromenu()
     self.intromenu()

  def emailmenu(self):
    os.system('clear')
    Logo().banner()
    if bi.search_string != None:
     print(" [{}!{}] {}E-Mail search menu: Target info{} - {}{}".format(bc.CYLW,bc.CEND,bc.CBLU,bc.CYLW,bi.search_string,bc.CEND))
    else:
     print(" [{}!{}] {}E-Mail search menu: Target info{}".format(bc.CYLW,bc.CEND,bc.CBLU,bc.CEND))
    print('\t[{}1{}] {}All{} - {}Run all modules associated to the email module group{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}2{}] {}LinkedIn{} - {}Check if user exposes information through LinkedIn{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}3{}] {}HaveIBeenPwned{} - {}Check email against known compromised networks{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}4{}] {}Myspace{} - {}Check if users account has a registered account{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}5{}] {}WhoisMind{} - {}Check email to registered domains{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}6{}] {}AdvancedBackgroundChecks{} - {}Run email through public page of paid access{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}7{}] {}Reset Target{} - {}Reset the Email to new target address{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}8{}] {}Back{} - {}Return to main menu{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    try:
     gselect = int(raw_input(" [{}!{}] {}Select a number to continue:{} ".format(bc.CYLW,bc.CEND,bc.CBLU, bc.CEND)))
    except:
     self.emailmenu()
    if gselect == 8:
     try:
      sys.exit(0)
     except Exception as noexit:
      sys.exit(0)
    else:
     try:
      if gselect != 8:
       if not bi.search_string or bi.search_string in ['',None]:
        #print("\n[{}PROFILE{}] {}Select a number to continue:{} ".format(bc.CYLW,bc.CEND,bc.CBLU, bc.CEND))
        bi.search_string = raw_input("\n  [{}PROFILE{}] {}Whats the target's email address?{} [ex: username@domain.tld{}]: ".format(bc.CBLU,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
      bi.lookup = "email"
      print()
      if gselect == 1:
       LinkedInGrabber().get_info(bi.search_string)
       MySpaceGrabber().get_info(bi.search_string)
       HaveIBeenPwwnedGrabber().get_info(bi.search_string)
       WhoisMindGrabber().get_info(bi.search_string)
       AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
      if gselect == 2:
       LinkedInGrabber().get_info(bi.search_string)
      if gselect == 3:
       HaveIBeenPwwnedGrabber().get_info(bi.search_string)
      if gselect == 4:
       MySpaceGrabber().get_info(bi.search_string)
      if gselect == 5:
       WhoisMindGrabber().get_info(bi.search_string)
      if gselect == 6:
       AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
      if gselect == 7:
       bi.search_string = raw_input("[{}?{}] {}Whats the target's email address?{} [ex: username@domain.tld{}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
       self.emailmenu()
     except:
      self.emailmenu()
     not raw_input("\nPress 'ENTER' key now to continue")
     self.emailmenu()

  def namemenu(self):
    os.system('clear')
    Logo().banner()
    print(" [{}!{}] {}Name search menu: Target info{} - {}{}".format(bc.CYLW,bc.CEND,bc.CBLU,bc.CYLW,bi.search_string,bc.CEND))
    print('\t[{}1{}] {}All{} - {}Run all modules associated to the name module group{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}2{}] {}Truth Finder{} - {}Run name through public page of paywall{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}3{}] {}True People{} - {}Run email through public page of paywall{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}4{}] {}AdvancedBackgroundChecks{} - {}Run email through public page of paywall{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}5{}] {}Reset Target{} - {}Reset the Email to new target address{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}6{}] {}Back{} - {}Return to main menu{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    try:
     gselect = int(raw_input(" [{}!{}] {}Select a number to continue:{} ".format(bc.CYLW,bc.CEND,bc.CBLU, bc.CEND)))
    except:
     self.namemenu()
    if gselect == 6:
     try:
      sys.exit(0)
     except Exception as noexit:
      sys.exit(0)
    else:
     try:
      if gselect != 6:
       if not bi.search_string or bi.search_string in ['',None]:
        bi.search_string = raw_input("[{}?{}] {}Whats the target's full name?{} [ex: Alice Smith{}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
      bi.lookup = 'name'
      print()
      if gselect == 1:
       TruthFinderGrabber().get_info(bi.lookup,bi.search_string)
       TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
       AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
      if gselect == 2:
       TruthFinderGrabber().get_info(bi.lookup,bi.search_string)
      if gselect == 3:
       TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
      if gselect == 4:
       AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
      if gselect == 5:
       bi.search_string = raw_input("[{}?{}] {}Whats the target's full name?{} [ex: Alice Smith{}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
       self.namemenu()
     except:
      self.namemenu()
     not raw_input("\nPress 'ENTER' key now to continue")
     self.namemenu()

  def phonemenu(self):
    os.system('clear')
    Logo().banner()
    print(" [{}!{}] {}Phone search menu: Target info{} - {}{}".format(bc.CYLW,bc.CEND,bc.CBLU,bc.CYLW,bi.search_string,bc.CEND))
    print('\t[{}1{}] {}All{} - {}Run all modules associated to the phone module group{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}2{}] {}TruePeopleSearch{} - {}Run email through public page of paid access{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}3{}] {}WhoCalld{} - {}Reverse phone trace on given number{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}4{}] {}411{} - {}Reverse phone trace on given number{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}5{}] {}AdvancedBackgroundChecks{} - {}Run number through public page of paid access{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}6{}] {}Reset Target{} - {}Reset the Phone to new target address{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}7{}] {}Back{} - {}Return to main menu{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    try:
     gselect = int(raw_input(" [{}!{}] {}Select a number to continue:{} ".format(bc.CYLW,bc.CEND,bc.CBLU, bc.CEND)))
    except:
     self.phonemenu()
    if gselect == 7:
     try:
      sys.exit(0)
     except Exception as noexit:
      sys.exit(0)
    else:
     try:
      if gselect != 7:
       if not bi.search_string or bi.search_string in ['',None]:
        bi.search_string = raw_input("[{}?{}] {}Whats the target's phone number?{} [ex: 1234567890{}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
      bi.lookup = 'phone'
      print()
      if gselect == 1:
       TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
       WhoCallIdGrabber().get_info(bi.search_string)
       FourOneOneGrabber().get_info(bi.search_string)
       AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
      if gselect == 2:
       TruePeopleGrabber().get_info(bi.lookup,bi.search_string)
      if gselect == 3:
       WhoCallIdGrabber().get_info(bi.search_string)
      if gselect == 4:
       FourOneOneGrabber().get_info(bi.search_string)
      if gselect == 5:
       AdvanceBackgroundGrabber().get_info(bi.lookup,bi.search_string)
      if gselect == 6:
       bi.search_string = raw_input("[{}?{}] {}Whats the target's phone number?{} [ex: 1234567890{}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
       self.phonemenu()
     except:
      self.phonemenu()
     not raw_input("\nPress 'ENTER' key now to continue")
     self.phonemenu()

  def snmenu(self):
    os.system('clear')
    Logo().banner()
    print(" [{}!{}] {}ScreenName search menu: Target info{} - {}{}".format(bc.CYLW,bc.CEND,bc.CBLU,bc.CYLW,bi.search_string,bc.CEND))
    print('\t[{}1{}] {}All{} - {}Run all modules associated to the email module group{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}2{}] {}Twitter{} - {}Run screenname and grab tweets{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}3{}] {}Knowem{} - {}Run screenname through to determin registered sites{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}4{}] {}NameChk{} - {}Run screenname through to determin registered sites{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}5{}] {}Tinder{} - {}Run screenname and grab information if registered{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}6{}] {}Reset Target{} - {}Reset the Phone to new target address{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}7{}] {}Back{} - {}Return to main menu{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    try:
     gselect = int(raw_input(" [{}!{}] {}Select a number to continue:{} ".format(bc.CYLW,bc.CEND,bc.CBLU, bc.CEND)))
    except:
     self.snmenu()
    if gselect == 7:
     try:
      sys.exit(0)
     except Exception as noexit:
      sys.exit(0)
    else:
     try:
      bi.lookup = 'sn'
      if gselect != 7:
       if not bi.search_string or bi.search_string in ['',None]:
        bi.search_string = raw_input("[{}?{}] {}Whats the target's screenname?{} [ex: (Ac1dBurn|Zer0C00l){}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
      print()
      if gselect == 1:
       TwitterGrabber().get_info(bi.search_string)
       KnowemGrabber().get_info(bi.search_string)
       NameChkGrabber().get_info(bi.search_string)
       TinderGrabber().get_info(bi.search_string)
      if gselect == 2:
       TwitterGrabber().get_info(bi.search_string)
      if gselect == 3:
       KnowemGrabber().get_info(bi.search_string)
      if gselect == 4:
       NameChkGrabber().get_info(bi.search_string)
      if gselect == 5:
       TinderGrabber().get_info(bi.search_string)
      if gselect == 6:
       bi.search_string = raw_input("[{}?{}] {}Whats the target's screenname?{} [ex: (Ac1dBurn|Zer0C00l){}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
     except:
      self.snmenu()
     not raw_input("\nPress 'ENTER' key now to continue")
     self.snmenu()

  def platemenu(self):
    os.system('clear')
    Logo().banner()
    print(" [{}!{}] {}ScreenName search menu: Target info{} - {}{}".format(bc.CYLW,bc.CEND,bc.CBLU,bc.CYLW,bi.search_string,bc.CEND))
    print('\t[{}1{}] {}All{} - {}Run all modules associated to the email module group{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}2{}] {}Plate Search{} - {}Run known vehicle plates against a database{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}3{}] {}Reset Target{} - {}Reset the Phone to new target address{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    print('\t[{}4{}] {}Back{} - {}Return to main menu{}'.format(bc.CBLU, bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
    try:
     gselect = int(raw_input(" [{}!{}] {}Select a number to continue:{} ".format(bc.CYLW,bc.CEND,bc.CBLU, bc.CEND)))
    except:
     self.platemenu()
    if gselect == 4:
     try:
      sys.exit(0)
     except Exception as noexit:
      sys.exit(0)
    else:
     try:
      if gselect != 4:
       if not bi.search_string or bi.search_string in ['',None]:
        bi.search_string = raw_input("[{}?{}] {}Whats the target's plate number?{} [ex: (XYZ123|0U812){}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
      bi.lookup = 'plate'
      print()
      if gselect == 1:
        VinGrabber().get_info(bi.search_string)
      if gselect == 2:
        VinGrabber().get_info(bi.search_string)
      if gselect == 3:
       bi.search_string = raw_input("[{}?{}] {}Whats the target's plate number?{} [ex: (XYZ123|0U812){}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
       self.platemenu()
     except:
      self.platemenu()
     not raw_input("\nPress 'ENTER' key now to continue")
     self.platemenu()

  def profiler(self):
    os.system('clear')
    Logo().banner()
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
    not raw_input("\nPress 'ENTER' key now to continue")
    self.intromenu()
