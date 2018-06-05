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

class FourOneOneGrabber(PageGrabber):  # 411.com scraper for reverse telephone lookups
    def get_info(self, phone_number):  # returns information about given telephone number
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "411" + bc.CEND)
        url = 'https://411.info/reverse/?r={}'.format(phone_number)
        source = self.get_source(url)
        try:
            soup = self.get_dom(source)
            name = soup.find('div', attrs={'class': 'cname'})
            if name:
                name = name.text.strip()
            else:
                name = "Unknown"
        except:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No source returned, try again later ...\n"+bc.CEND)
            return
        for itemText in soup.find_all('div', attrs={'class': re.compile('adr_.*')}):
            street = itemText.find('span', itemprop='streetAddress')
            if street:
                street = street.text.replace("\t", "").replace(",", "")
                street = street.strip()
            else:
                street = "Unknown"
            town = itemText.find('span', itemprop='addressLocality')
            if town:
                town = town.text.strip()
            else:
                town = "Unknown"
            state = itemText.find('span', itemprop='addressRegion')
            if state:
                state = state.text.strip()
            else:
                state = "Unknown"
            zipcode = itemText.find('span', itemprop='postalCode')
            if zipcode:
                zipcode = zipcode.text.strip()
            else:
                zipcode = "Unknown"
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Name: "+bc.CEND+ str(name))
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Street: "+bc.CEND+ str(street))
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"State: "+bc.CEND+ str(state))
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"City: "+bc.CEND+ str(town))
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Zip: "+bc.CEND+ str(zipcode))
            self.info_dict.update({
                "name": name,
                "street": street,
                "town": town,
                "state": state,
                "zipcode": zipcode
            })
        bi.outdata['fouroneone'] = self.info_dict
        if len(self.info_dict) == 0:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No source returned, try again later ...\n"+bc.CEND)
            return
        else:
            print()
            return
