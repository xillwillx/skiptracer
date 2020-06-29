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


class HelpMenu():
    """
    Default help menu
    and text.
    """

    def __init__(self):
        self.display_help()


    def display_help(self):
        """
        Help text
        """

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
  This class of searches include the following modules:
  -:  LinkedIn - Check if user exposes information through LinkedIn
  -:  HaveIBeenPwned - Check email against known compromised networks
  -:  Myspace - Check if users account has a registered account
  -:  AdvancedBackgroundChecks - Run email through public page of paid access
:: NAME ::
  Requires a user to supply a First and Last name:
  -: Format: Alice Smith
  This class of searches include the following modules:
  -: Truth Finder - Check if a targets name using Truth Finder
  -: True People - Check a targets name using True People
  -: AdvancedBackgroundChecks - Checks targets name through ABC
:: PHONE ::
  Requires a user to supply a US based telephone number
  -: Format: 123 456 7890
  This class of searches include the following modules
  -: True People - Check if targets phone number using True People
  -: WhoCalled - WhoCalled reverse lookup of telephone number
  -: 411 - Reverse telephone lookup from 411 of telephone number
  -: AdvancedBackgroundChecks - Checks targets phone number through ABC
:: SCNAME ::
  Requires a user to supply a known screenname:
 -: Format: crazy8s
 This class of searches icludes the following modules:
  -: Knowem - Checks screen name against numerous sites for registered account
  -: NameChk - Checks screen name against numerous sites for registered account
  -: Tinder - Checks if screen name against Tinder known users
:: PLATE ::
  Requires user to supply a known plate
  -: Format: 123456
  This class of searche include the following modules:
  -: Plate Search - Runs known plates through nationwide Database
""")
