from __future__ import print_function
#######################################################################
#       myspace scraper - returns user url of email address           #
#######################################################################
import re
import logging
from plugins.base import PageGrabber
from plugins.colors import BodyColors as bc
try:
    import __builtin__ as bi
except:
    import builtins as bi

class MySpaceGrabber(PageGrabber):  # Myspace.com scraper for email lookups
    def get_info(self,email):  # Looks up user accounts by given email
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "Myspace" + bc.CEND)
        url = 'https://myspace.com/search/people?q={}'.format(email)
        source = self.get_source(url)
        soup = self.get_dom(source)
        try:
            name = soup.select('h6')[0].text.strip()
        except:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No Myspace account found.\n"+bc.CEND)
            return
        try:
            accountr = soup.select('h6')[0].a.get('href').strip()
            account = "https://myspace.com{}".format(accountr)
        except:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No Myspace account found.\n"+bc.CEND)
            return
        try:
            source = self.get_source(account)
            soup = self.get_dom(source)
            location = soup.find('div', attrs={'class': 'location_white location '})['data-display-text']
        except:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Unable to complete the request.\n"+bc.CEND)
            return
        if not location:
            location = "Unknown"
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Acct: "+bc.CEND+ str(account))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Name: "+bc.CEND+ str(name))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Loc:  "+bc.CEND+ str(location)+"\n")
        self.info_dict.update({
            "name": name,
            "account": account,
            "location": location,
        })
        bi.outdata['myspace'] = self.info_dict
        return
