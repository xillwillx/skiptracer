from __future__ import print_function
from __future__ import absolute_import
#
#   haveibeenpwned scraper - returns breach name and date for email
#

import re
import logging
import simplejson as json
from plugins.base import PageGrabber
from plugins.colors import BodyColors as bc
import ast
import cfscrape
try:
    import __builtin__ as bi
except:
    import builtins as bi

class HaveIBeenPwwnedGrabber(PageGrabber):    # HackedEmails.com scraper for email compromise lookups
    def get_info(self,email):  # Uniform call for framework
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "HaveIbeenPwned" + bc.CEND)
        self.count = 0
        self.resurl = 0
        self.trymore(email)
    def trymore(self, email):  # Actual logic for lookup and re-try
        while self.resurl == 0:
            try:
                self.count += 1
                url = 'https://haveibeenpwned.com/api/v2/breachedaccount/{}'.format(email)
                scraper = cfscrape.create_scraper()
                self.source = scraper.get(url).content
                self.source = str(self.source).replace("true","True").replace("false","False")
                self.source = ast.literal_eval(self.source)
                self.resurl = 1
                for dataset in self.source:
                    self.result = dataset
                    try:
                        if self.result:
                            self.breach = self.result['BreachDate']
                            self.domain = self.result['Domain']
                            self.title = self.result['Title']
                            self.exposes = self.result['DataClasses']
                            self.info_dict.update({"BreachDate": self.breach, "Domain": self.domain, "Title": self.title, "DataExposed": self.exposes})
                            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Dump Name: "+bc.CEND+ self.title)
                            print("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Domain: "+bc.CEND+ self.domain)
                            print("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Breach: "+bc.CEND+ self.breach)
                            print("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Exposes: "+bc.CEND)
                            for xpos in self.exposes:
                                print("      ["+bc.CGRN+"-"+bc.CEND+"] "+bc.CRED+"DataSet: "+bc.CEND + xpos)
                        else:
                            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found.\n"+bc.CEND)
                    except Exception as nojson:
                        print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found.\n"+bc.CEND)
                        return #pass  ## Needed to write out the results to JSON output
                bi.outdata['haveibeenpwned'] = self.info_dict
                print()
                return
            except Exception as badres:
                print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Failed at accessing site ... Try again later ...\n"+bc.CEND)
                return

