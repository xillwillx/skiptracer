from __future__ import absolute_import, print_function
import re
from plugins.base import PageGrabber
from .colors import BodyColors as bc
try:
    import __builtin__ as bi
except ImportError:
    import builtins as bi
try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

import re
import json
import requests

class SubDomainGrabber(PageGrabber):  # crt.sh scraper for abusing Certificate Transparency log lookups
    def get_info(self, domain):  # returns information about a domains subdomains
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "crt.sh " + bc.CEND)
        domain2 = domain.split("//")[-1].split("/")[0].split('?')[0] #strip the input to just the domain name and TLD only
        req = requests.get("https://crt.sh/?q=%.{}&output=json".format(domain2))
        if req.status_code != 200:
            print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found ...\n"+bc.CEND)
            exit(1)
        jsondata = json.loads('[{}]'.format(req.text.replace('}{', '},{')))
        
        subdomainlist = []     
        for (key,value) in enumerate(jsondata):
            subdomainlist.append(value['name_value'])

        subdomainlist = sorted(set(subdomainlist))

        for subdomain in subdomainlist:
            if not (re.search("^\*\.", subdomain)):
                print("["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Subdomain: "+bc.CEND+"{}".format(subdomain))
 

        self.info_dict.update({
            "subdomain": subdomain
        })
        bi.outdata['crt'] = self.info_dict
        if len(self.info_dict) == 0:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No source returned, try again later ...\n"+bc.CEND)
            return
        else:
            print()
            return