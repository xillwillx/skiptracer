#######################################################################
#   hackedemail scraper - returns breach name and date for email     #
#######################################################################

import re
import logging
import simplejson as json
from plugins.base import PageGrabber
from plugins.colors import BodyColors as bc
import proxygrabber
import ast

try:
    import __builtin__ as bi
except:
    import builtins as bi

class HackedEmailGrabber(PageGrabber):    # HackedEmails.com scraper for email compromise lookups
    def get_info(self,email):  # Uniform call for framework
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "Hacked-Emails" + bc.CEND)
        self.count = 0
        self.resurl = 0
        self.trymore(email)
    def trymore(self, email):  # Actual logic for lookup and re-try
        while self.resurl == 0:
            try:
                self.count += 1
                url = 'https://hacked-emails.com/check_email?email={}'.format(email).replace("@","%40")
                self.source = self.get_source(url).encode("ascii","ignore").decode("utf8")
                self.soup = self.get_html(self.source)
            except Exception as badres:
                print "Bad Res: %s" % badres
            try:
                reres = re.findall("Congratulations", str(self.soup))
                if reres:
                    self.resurl = 1
                    print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found.\n"+bc.CEND)
                    return
            except Exception as badres:
                print "Bad Res: %s" % badres
            try:
                trclass = self.soup.find_all("div", {"class":"table-responsive"})
                trsplit = str(trclass[1]).split("<tr>")
                trsplit.pop(0)
                trsplit.pop(0)
            except Exception as badres:
                print "Bad Res: %s" % badres
            try:
                for xtr in trsplit:
                    xlist = xtr.split("</td>")
                    exposed = str(xlist[0]).split(">")[1]
                    listname = xlist[1].split("/")[5].split("\"")[0].replace("-"," ").replace(" com","")
                    self.info_dict.update({listname: exposed})
                    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Found on:"+bc.CEND+" %s "+bc.CRED+"In:"+bc.CEND+" %s ") % (exposed,listname)
                bi.outdata['hackedemails'] = self.info_dict
                print
                return
            except Exception as badres:
                print "Bad Res: %s" % badres
                if bi.webproxy and self.count < 5:
                    if not self.soup:
                         print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Attempting to get source.."+bc.CEND)
                    try:
                        proxygrabber.new_proxy()
                        self.trymore(email)

                    except Exception as proxygrabfail:
                        print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No new proxy could be found.\n"+bc.CEND)
                        return
                else:
                    if self.count < 5:
                        print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Attempting to get source, again ..."+bc.CEND)
                        self.trymore(email)
                    else:
                        print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Failed at accessing site ... Try again later ...\n"+bc.CEND)
                        return
                return
