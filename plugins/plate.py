from __future__ import absolute_import, print_function
from time import sleep
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


class VinGrabber(PageGrabber):  # faxvin.com scraper for plate lookups
    def get_info(self, plate):  # returns information about given plate number
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "FaxVin" + bc.CEND)
        state = raw_input("  ["+bc.CRED+"!"+bc.CEND+"] "+bc.CYLW+ "Please enter 2 letter abbreviated state - ex: (AL=Alabama|CO=Colorado) "+bc.CEND).upper()
        plate = plate.upper()
        url = 'https://www.faxvin.com/license-plate-lookup/result?plate={}&state={}'.format(plate,state)
        #print("URL generated: %s" %url)
        try:
         source = self.get_source(url)
         sleep(0.5)
         soup = self.get_html(source)
         sleep(0.5)
        except Exception as e:
         print("Fault: %s" % e)
        #print("Soup returned: %s" % soup)
        if soup.body.find_all(string=re.compile('.*{0}.*'.format('Sorry, the plate your currently looking for is not available.')), recursive=True):
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No plate found.\n"+bc.CEND)
            return
        try:
            table = soup.find('table', attrs={'class': 'tableinfo'})
        except:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No source returned, try again later ...\n"+bc.CEND)
            return
        try:
            cells = table.findAll("td")
        except:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found ...\n"+bc.CEND)
            return
        vin = cells[0].b.text
        make = cells[1].b.text
        model = cells[2].b.text
        year = cells[3].b.text
        trim = cells[4].b.text
        style = cells[5].b.text
        engine = cells[6].b.text
        plant = cells[7].b.text
        age = cells[8].b.text
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Plate: "+bc.CEND+ str(plate))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"State: "+bc.CEND+ str(state))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"VIN: "+bc.CEND+ str(vin))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Make: "+bc.CEND+ str(make))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Model: "+bc.CEND+ str(model))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Year: "+bc.CEND+ str(year))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Trim: "+bc.CEND+ str(trim))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Style: "+bc.CEND+ str(style))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Engine: "+bc.CEND+ str(engine))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Plant: "+bc.CEND+ str(plant))
        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Age: "+bc.CEND+ str(age))

        self.info_dict.update({
            "plate": plate,
            "state": state,
            "vin": vin,
            "make": make,
            "model": model,
            "year": year,
            "trim": trim,
            "style": style,
            "engine": engine,
            "plant": plant,
            "age": age
        })
        bi.outdata['faxvin'] = self.info_dict
        if len(self.info_dict) == 0:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No source returned, try again later ...\n"+bc.CEND)
            return
        else:
            print()
            return
