#
# KnowEm Module - 0daysimpson & illwill
#
import re
import logging
import requests
from plugins.base import PageGrabber
from colors import BodyColors as bc
try:
    import __builtin__ as bi
except:
    import builtins as bi

class KnowemGrabber(PageGrabber):  # knowem.com scraper for screenname lookups
    def get_info(self, username):  # returns information about given hndle
        try:
            username = username.split("@")[0]
            print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "Knowem" + bc.CEND)
            url = "https://knowem.com/usercheckv2.php?target="
            networks = ["Blogger","BuzzFeed","DailyMotion","Etsy",
            "facebook","foursquare","Hubpages","Imgur","Issuu",
            "LinkedIn","LiveJournal","MySpace","Photobucket","Pinterest",
            "reddit","scribd","soundcloud","Tumblr","Twitter",
            "Typepad","vimeo","Wordpress","YouTube"]
            for social in networks:
                request_url = url + social +"&username="+ username
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
                headers ={"referer":("https://knowem.com/checkusernames.php?u="+username),"X-Requested-With":"XMLHttpRequest","User-Agent":user_agent}
                response = requests.get(url=request_url,headers=headers).text
                if (re.search(pattern='Sorry',string=response)):
                    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Account: "+bc.CEND+ str(social))
                    self.info_dict.update({
                        "Account": social})
        except Exception as staging:
            if bi.debug: print (("  ["+bc.CRED+"DEBUG"+bc.CEND+"] "+bc.CYLW+"Failed at staging: "+bc.CEND) % staging)
        bi.outdata['knowem'] = self.info_dict
        if bi.debug: print ("  ["+bc.CRED+"DEBUG"+bc.CEND+"] "+bc.CYLW+"Passed dictionary production"+bc.CEND)
        if len(self.info_dict) == 0:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No source returned, try again later ...\n"+bc.CEND)
            return
        else:
            print
            return
