from __future__ import print_function
from __future__ import absolute_import
#
# Advancedbackgroundchecks.com scraper
#

import re
import logging
import json
from plugins.base import PageGrabber
import base64 as b64
from .colors import BodyColors as bc
from time import sleep
from bs4 import BeautifulSoup

try:
    import __builtin__ as bi
except:
    import builtins as bi
import sys

class AdvanceBackgroundGrabber(PageGrabber):
    def check_for_captcha(self):  # Check for CAPTCHA, if proxy enabled,try new proxy w/ request, else report to STDOUT about CAPTCHA
        captcha = self.soup.find('div', attrs={'class':'g-recaptcha'})
        if not captcha:
            captcha = self.soup.body.findAll(text=re.compile('Custom Script'))
        if captcha:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Captcha detected, use a proxy or complete challenge in browser\n"+bc.CEND)
            return True
        else:
            return False

    def abc_try(self,lookup,information):  # Determins different URL constructs based on user supplied data
        address_list = []
        if lookup == "phone":
            try:
                phonere = re.compile('(\d\d\d\d\d\d\d\d\d\d|\d\d\d[\s.-]\d\d\d[\s.-]\d\d\d\d)')
            except Exception as e:
                pass
            def makephone(information):  # Find user supplied data format, adjust as needed for URL
                try:
                    if str(information).split("-")[1]:  # Can it be split by a "-", everything is ok
                        dashphone = information
                        return dashphone
                except:
                    pass
                try:
                    if str(information).split(" ")[1]:  # Can it be split by a whitespace, if so, break and format as needed for the URL
                        dashphone = '{}-{}-{}'.format(information[0:3], information[5:8], information[9:])
                        return dashphone
                except:
                    pass
                try:
                    if len(information) == 10:  # If len of data is 10 and is an integer, break and format as needed for URL
                        dashphone = '{}-{}-{}'.format(information[0:3], information[3:6], information[6:])
                        return dashphone
                    if len(information) != 10:
                        print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Check search string, should be 10 digits.\n"+bc.CEND)
                        return
                except:
                    return
            try:
                self.num = makephone(information)
                if self.num == None:
                    return
                self.url = "https://www.advancedbackgroundchecks.com/{}".format(self.num)
                email = False
            except Exception as e:
                print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Could not produce required URL.\n"+bc.CEND)
                return
        if lookup == "email":  # Make the URL for email lookup, set email True
            if str(information).split('@')[1]:
                self.url = "https://www.advancedbackgroundchecks.com/emails/{}".format(b64.b64encode(str(information)))
                email = True
        if lookup == "name":  # Make the URL for name lookup, set email to False
            if str(information).split(' ')[1]:
                age = raw_input("[{}?{}] {}Whats the target's suspected age?{} [ex: 40{}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
                loc = raw_input("[{}?{}] {}Whats the target's area of residency?{} [ex: MO/11123/Chicago{}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))

                #age = raw_input(" [{}?{}] {}What is the targets suspected/known age?:{} ".format(bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
                #loc = raw_input(" [{}?{}] {}What is the targets suspected/known area of residency?:{} ".format(bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
                self.url = "https://www.advancedbackgroundchecks.com/name/{}_{}_age_{}".format(str(information).replace(' ','-'), loc, age)
                print("full url: %s" % self.url)
                email = False
        try:
            self.source = self.get_source(self.url)
            self.soup = self.get_dom(self.source)
            #print(self.soup)
            if self.check_for_captcha() == True:  # Check responce for sign of captcha
                print("Captcha Detected")
                return
        except Exception as e:
            print(e)
            return
        try:
            if self.soup.find('div', {'id': 'no-result-widgets'}):  # Report if there are no results to STDOUT
                print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found.\n"+bc.CEND)
                return
            checkres = self.soup.findAll("h1")
            if lookup == "phone":
             for xcheck in checkres:
              if xcheck.text in ["We could not find any results based on your search criteria.  Please review your search and try again, or try our sponsors for more information.", "Top Results for "+str(self.num)]:
               print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found.\n"+bc.CEND)
               return
            script_html = self.soup.find_all('script', type="application/ld+json") #.contents  # Scrape for JSON within DOM
        except Exception as findallfail:
            print("failed with findall: %s" % (findallfail))
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found.\n"+bc.CEND)
            return
        if len(script_html) == 3:  # Check len on results
            #print("Script is 3")
            script_html = script_html[2]  # Set the desired value to iterate over
            #print(script_html)
        try:
         #print(script_html)
         script_htmla = script_html.get_text().strip()  # Format data for JSON load
         #print("script htmla: %s" % script_htmla)
         script_htmla = str(script_htmla).strip()  # Format data for JSON load
         script_htmla = script_htmla.replace("\n","")
         script_htmla = script_htmla.replace("\t","")
         person_list = json.loads(script_htmla)  # Loads data as JSON
         #print("person list length: %s" % len(person_list))
         #print("person list contents: %s" % person_list)
        except Exception as e:
         pass
         #print("scripthtml failed: %s" % (e))
        for person in person_list:  # Iterate entries and store their values, return results in different outputs, STDOUT, Dict()
            #print("Person in person list: %s" % person)
            try:
             #print("Next person in person list: %s" %(person))
             addrfirst = 0
             pnext = 0
             if pnext >= 1:
              print(" ["+bc.CGRN+"!"+bc.CEND+"] "+bc.CRED+"Next finding: "+bc.CEND)
             #print("person url: %s" % person['@id'])
             self.url2 = person['@id']  # set additional 2nd level URL
             self.source2 = self.get_source(self.url2)  # request 2nd level url
             self.soup2 = self.get_dom(self.source2)  # grab 2nd level DOM
             script_html2 = self.soup2.find_all('script', type="application/ld+json")  # Scrape for JSON within DOM
             print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Name: "+bc.CEND+ str(person.get("name")))
             if person.get("birthDate"):  # Set DoB
                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"D.o.B: "+bc.CEND+ str(person.get("birthDate")))
             if person.get("additionalName"):  # Set additional names AKA
                 print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Alias: "+bc.CEND)
                 for xaka in person.get("additionalName"):  # For each AKA, select the name
                     print("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"AKA: "+bc.CEND+ str(xaka))
             if len(script_html2) <=1:
                 print (" ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Unable to re-try request... Try again later...\n"+bc.CEND)
                 return
             else:
                 #print("Script html2: %s" % script_html2)
                 script_html2 = script_html2[2]
                 script_html2 = script_html2.get_text().strip()  # Format data for JSON load
                 script_html2 = script_html2.replace("\n","")
                 script_html2 = script_html2.replace("\t","")
                 person_list2 = json.loads(script_html2)  # Loads dat
                 #print(len(person_list2))
                 #print("Person list contents: %s" % person_list2)
                 if len(person_list2) > 1:
                  try:
                   print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Phone: "+bc.CEND)
                   for tele in person_list2['telephone']:
                    print("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"#: "+bc.CEND+ str(tele))
                  except Exception as e:
                   #print(e)
                   print("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"#: Not found"+bc.CEND)
                   pass
                  try:
                   print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Email: "+bc.CEND)
                   for email in person_list2['email']:
                    print("   ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Addr: "+bc.CEND+ str(email))
                  except Exception as e:
                   print("   ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Addr: "+bc.CEND)
                   pass
             if person.get("address"):  # Set Addresses
                 print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Addresses.: "+bc.CEND)
                 for addy in person.get("address"):  # For each address, select the information and store 
                     addrfirst += 1
                     if addrfirst == 1:
                         print("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Current Address: "+bc.CEND)
                     else:
                         print("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Prev. Address: "+bc.CEND)
                     print("      ["+bc.CGRN+"-"+bc.CEND+"] "+bc.CRED+"Street: "+bc.CEND+str(addy.get("streetAddress")))
                     print("      ["+bc.CGRN+"-"+bc.CEND+"] "+bc.CRED+"City: "+bc.CEND+str(addy.get("addressLocality")))
                     print("      ["+bc.CGRN+"-"+bc.CEND+"] "+bc.CRED+"State: "+bc.CEND+str(addy.get("addressRegion")))
                     print("      ["+bc.CGRN+"-"+bc.CEND+"] "+bc.CRED+"ZipCode: "+bc.CEND+str(addy.get("postalCode")))
                     address_list.append({"city": addy.get("addressLocality"),
                                          "state": addy.get("addressRegion"),
                                          "zip_code": addy.get("postalCode"),
                                          "address": addy.get("streetAddress")})
             if person.get("relatedTo"):  # Set Relatives
                 print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Related: "+bc.CEND)
                 for xrelate in [item.get("name") for item in person.get("relatedTo")]:  # For each relative, select the information and store
                     print("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Known Relative: "+bc.CEND+str(xrelate))
             self.info_list.append({"name": person.get("name"),
                                    "birth_date": person.get("birthDate"),
                                    "additional_names": person.get("additionalName"),
                                    "telephone": person_list2['telephone'],
                                    "email": person_list2['email'],
                                    "address_list": address_list,
                                    "related_to": [item.get("name") for item in person.get("relatedTo")]})
             pnext += 1
            except Exception as forloopperperson:
             print("For loop per person failed: %s"  % (forlooperperson))
        bi.outdata['advancedbackground'] = self.info_list  # Build out the dataset
        print()
        return

    def get_info(self, lookup, information):  # Uniform call for framework to launch function in a way to single out the calls per URL
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "AdvanceBackgroundChecks" + bc.CEND)
        self.abc_try(lookup,information)  # Actual login to run + re-try request
