"""Whocallid.com search module"""
from __future__ import print_function
from __future__ import absolute_import

import re
import logging
from plugins.base import PageGrabber
from .colors import BodyColors as bc
try:
    import __builtin__ as bi
except:
    import builtins as bi

class WhoCallIdGrabber(PageGrabber):  # WhoCallID sales scraper for reverse telephone lookups
    def get_info(self, phone_number):  # Request, scrape and return values found
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "WhoCalld" + bc.CEND)
        url = 'https://whocalld.com/+1{}'.format(phone_number)
        source = self.get_source(url)
        soup = self.get_dom(source)
        if soup.body.find_all(string=re.compile('.*{0}.*'.format('country')), recursive=True):
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No WhoCallID data returned\n"+bc.CEND)
            return
        try:
            name = soup.find('h2', attrs={'class': 'name'})
            if name:
                name = name.text.strip()
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Name: "+bc.CEND+ str(name))
            else:
                name = "Unknown"
        except:
            pass
        try:
            location = soup.find('h3', attrs={'class': 'location'})
            if location:
                location = location.text.strip()
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Location: "+bc.CEND+ str(location))
            else:
                location = "Unknown"
        except:
            pass
        try:
            phone_type = soup.find("img").attrs['alt']
            if phone_type:
                phone_type = phone_type.strip()
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Phone Type: "+bc.CEND+ str(phone_type))
            else:
                phone_type = "Unknown"
        except:
            pass
        try:
            url = "https://whocalld.com/+1{}?carrier".format(phone_number)
            source = self.get_source(url)
            soup = self.get_dom(source)
            carrier = soup.find('span', attrs={'class': 'carrier'})
        except:
            pass
        try:
            if carrier:
                carrier = carrier.text
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Carrier: "+bc.CEND+ str(carrier))
            else:
                carrier = ""
        except:
            pass
        try:
            city = soup.find('span', attrs={'class': 'city'})
            if city:
                city = city.text
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"City: "+bc.CEND+ str(city))
            else:
                city = ""
        except:
            pass
        try:
            state = soup.find('span', attrs={'class': 'state'})
            if state:
                state = state.text
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"State: "+bc.CEND+ str(state))
            else:
                state = ""
        except:
            pass
        try:
            time = soup.find('span', attrs={'class': 'time'})
            if time:
                time = time.text
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Time: "+bc.CEND+ str(time))
            else:
                time = ""
        except:
            pass
        self.info_dict.update({
            "carrier": carrier,
            "city": city,
            "location": location,
            "name": name,
            "phone_type": phone_type,
            "state": state,
            "time": time
        })
        bi.outdata['whocallid'] = self.info_dict
        print()
        return
