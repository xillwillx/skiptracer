from __future__ import print_function
from __future__ import absolute_import
#
# Tinder Module - illwill
#
import re
import logging
import requests
from plugins.base import PageGrabber
from .colors import BodyColors as bc
try:
    import __builtin__ as bi
except:
    import builtins as bi

class TinderGrabber(PageGrabber):  # tinder scraper for screenname lookups

    def get_info(self, username):  # returns information about given hndle
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "Tinder" + bc.CEND)
        url = "https://www.gotinder.com/@%s" % (username)
        source = self.get_source(url) 
        soup = self.get_dom(source)
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+ "User: "+bc.CEND+"%s" % username)
        if soup.body.findAll(text='Looking for Someone?'):                     #check if CAPTCHA was triggered
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No Profile Found.\n"+bc.CEND)
            return
        try:
            photo = soup.find("img", id="user-photo")
            if photo:
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Photo: "+bc.CEND+(photo['src']))
            else:
                photo = "unknown"
        except:
            pass
        try:
            name = soup.find("span", id="name")
            if name:
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Name: "+bc.CEND+name.text)
            else:
                photo = "unknown"
        except:
            pass
        try:
            teaser = soup.find("span", id="teaser")
            if name:
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Bio: "+bc.CEND+teaser.text)
            else:
                photo = "unknown"
        except:
            pass
        try:
            age = soup.find("span", id="age")
            if name:
                age = (age.text).replace(',','')
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Age: "+bc.CEND+age.strip())
            else:
                photo = "unknown"
        except:
            pass

        self.info_dict.update({
            "photo": photo,
            "name": name,
            "bio": teaser,
            "age": age
        })
        bi.outdata['knowem'] = self.info_dict
        if len(self.info_dict) == 0:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No source returned, try again later ...\n"+bc.CEND)
            return
        else:
            print()
        return
