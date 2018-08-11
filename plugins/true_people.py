from __future__ import absolute_import, print_function

#
# TruePeopleSearch.com scraper
#
import re

from plugins.base import PageGrabber

#from . import proxygrabber
from plugins.colors import BodyColors as bc

try:
    import __builtin__ as bi
except ImportError:
    import builtins as bi

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

class TruePeopleGrabber(PageGrabber):
    def check_for_captcha(self):  # Check for CAPTCHA, if proxy enabled,try new proxy w/ request, else report to STDOUT about CAPTCHA
        captcha = self.soup.find('div', attrs={'class':'g-recaptcha'})
        if captcha != None:
            print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Captcha detected, use a proxy or complete challenge in browser\n"+bc.CEND)
            return True
        else:
            return False

    def true_try(self,lookup,information):  # Determins different URL constructs based on user supplied data
        address_list = []
        if lookup == "phone":
            phonere = re.compile('(\d\d\d\d\d\d\d\d\d\d|\d\d\d[\s.-]\d\d\d[\s.-]\d\d\d\d)')
            def makephone(information):  # Find user supplied data format, adjust as needed for URL
                try:
                    if str(information).split("-")[1]:  # Can it be split bu a "-", everything is ok
                        dashphone = '({})-{}-{}'.format(information[0:3], information[5:8], information[9:])
                        return dashphone
                except Exception as e:
                    pass
                try:
                    if str(information).split(" ")[1]:  # Can it be split by a whitespace, if so, break and format as needed for the URL
                        dashphone = '({})-{}-{}'.format(information[0:3], information[5:8], information[9:])
                        return dashphone
                except Exception as e:
                    pass
                try:
                    if len(information)== 10:  # If len of data is 10 and is an integer, break and format as needed for URL
                        dashphone = '({})-{}-{}'.format(information[0:3], information[3:6], information[6:])
                        return dashphone
                except Exception as e:
                    print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Did not detect a phone number\n"+bc.CEND)
                    return
            if phonere.findall(information):  # Make the URL for a phone lookup, set email to False
                try:
                    self.url = 'https://www.truepeoplesearch.com/results?phoneno={}'.format(makephone(information))
                    email = False
                except Exception as e:
                    pass
        if lookup == "name":  # Make the URL for name lookup, set email to False
            agerange = raw_input("[{}?{}] {}Please enter an age range:{} [ex: 18-100{}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
            citystatezip = raw_input("[{}?{}] {}Please enter a city,state,or zip?{} [ex:(AL|Alabama|12345){}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
            if str(information).split(' ')[1]:
                self.url = "https://www.truepeoplesearch.com/results?name={}&agerange={}&citystatezip={}".format(str(information).replace(' ','%20'), agerange, citystatezip)
                email = False
        if lookup in ['name','phone']:
            self.source = self.get_source(self.url)
            self.soup = self.get_dom(self.source)
        if self.check_for_captcha() == True:  # Check responce for sign of captcha
            print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Goto: {}"+bc.CEND).format(self.url))
            self.iscomplete = raw_input("  ["+bc.CRED+"!"+bc.CEND+"] "+bc.CYLW+ "Have you completed the CAPTCHA? "+bc.CEND)
            """if str(self.iscomplete).lower() in ['no',False,0]:
                print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"User has not completed the CAPTCHA\n"+bc.CEND)
                return
            else:
                pass"""
        try:
            for xnotfound in self.soup.findAll('div',{'class','row pl-1 record-count'}):
                if str(xnotfound.div.text).strip() == "We could not find any records for that search criteria.":
                    print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found.\n"+bc.CEND)
                    return
        except:
           print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found.\n"+bc.CEND)
           return
        print('')
        try:
            deep = self.soup.find_all('a',{'class':['btn','btn-success','btn-lg','detail-link','shadow-form']})
            age = "Unknown"
            name = "Unknown"
            aklist = "Unknown"
            lives = "Unknown"
            prev = "Unknown"
            plist = "Unknown"
            rellist = "Unknown"
            asso = "Unknown"
            for x in sorted(set(deep)):
                try:
                    if lookup == 'name':
                        rid = str(x).split(";")[3].split('"')[0]
                    if lookup == 'phone':
                        rid = str(x).split(";")[1].split('"')[0]
                except Exception as e:
                    print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No results were found.\n"+bc.CEND)
                    return
                try:
                    self.url2 = self.url+"&"+rid
                except Exception as e:
                    print(e)
                try:
                    self.source2 = self.get_source(self.url2)
                except Exception as e:
                    print(e)
                try:
                    self.soup2 = self.get_dom(self.source2)
                except Exception as e:
                    print(e)
                try:
                    nc = self.soup2.find('span',{'class':'h2'})
                    nc1 = str(nc).split(">")[3]
                    name = str(" ".join(str(nc1).split())).split("<")[0]
                    print(("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Name: "+bc.CEND+"%s") % (name))
                except Exception as e:
                    print(e)
                    name = "Unknown"
                try:
                    age1 = self.soup2.find('span',{'class':'content-value'})
                    age2 = " ".join(str(age1).split())
                    age = age2.split(">")[1].split("<")[0].split()[1]
                    print(("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Age: "+bc.CEND+"%s") % (age))
                except:
                    age = "Unknown"
                try:
                    aklist = []
                    aka = self.soup2.find_all('a',{'class':'link-to-more','data-link-to-more':'aka'})
                    if len(aka) >= 1:
                        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Alias: "+bc.CEND)
                        aka = sorted(set(aka))
                        for xaka in aka:
                            xakas = str(xaka).split('>')[1].split('<')[0]
                            aklist.append(xakas)
                            print(("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"AKA: "+bc.CEND+"%s") % (xakas))
                except:
                    aklist = "Unknown"
                try:
                   address = self.soup2.find_all('a',{'class':'link-to-more','data-link-to-more':'address'})
                except:
                    address = "Unknown"
                try:
                    related = self.soup2.find_all('a',{'class':'link-to-more','data-link-to-more':'relative'})
                    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Related:"+bc.CEND)
                    related = sorted(set(related))
                    rellist = []
                    for xrelate in related:
                        xrels = str(xrelate).split(">")[1].split("<")[0]
                        rellist.append(xrels)
                    for xrel in sorted(set(relllist)):
                        print(("      ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Known Relative: "+bc.CEND+"%s") % xrel)
                except:
                    rellist = "Unknown"
                try:
                    associate = self.soup2.find_all('a',{'class':'link-to-more','data-link-to-more':'associate'})
                    associate = sorted(set(associate))
                    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Associate(s):"+bc.CEND)
                    asso = []
                    for xassociate in associate:
                        assoc = str(xassociate).split(">")[1].split("<")[0]
                        asso.append(assoc)
                        print(("      ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Known Associate: "+bc.CEND+"%s") % assoc)
                except:
                     asso = "Unknown"
                try:
                    curaddr = 0
                    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Address:"+bc.CEND)
                    prev = []
                    for xaddr in address:
                        adr = " ".join(str(xaddr).split())
                        adrs = " ".join(adr.split(">")[1::])
                        addr = adrs.replace("<br/ ","").replace("</a","").strip()
                        if curaddr == 0:
                            print(("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Current: "+bc.CEND+"%s") % addr)
                            lives = addr
                        else:
                            print(("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Previous: "+bc.CEND+"%s") % addr)
                            prev.append(addr)
                        curaddr += 1
                except:
                    prev = "Unknown"
                try:
                    phone = self.soup2.find_all('a',{'class':'link-to-more','data-link-to-more':'phone'})
                    plist = []
                    if len(phone) >= 1:
                        print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Phone: "+bc.CEND)
                        for xnum in phone:
                            try:
                                xnums = str(xnum).split(">")[1].split("<")[0]
                                plist.append(xnums)
                                print(("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"#: "+bc.CEND+"%s") % xnums)
                            except Exception as w:
                                pass
                except Exception as e:
                    print(e)
                    plist = "Unknown"
                self.info_dict.update({name: {
                                        "age": age,
                                        "alias": aklist,
                                        "lives": lives,
                                        "lived": prev,
                                        "phone": plist,
                                        "related": rellist,
                                        "associate": asso}
                                     })
        except Exception as e:
            print(e)
        bi.outdata['truepeoplesearch'] = self.info_dict  # Build out the dataset
        print()
        return

    def get_info(self, lookup, information):  # Uniform call for framework to launch function in a way to single out the calls per URL
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "TruePeopleSearch" + bc.CEND)
        self.true_try(lookup,information)  # Actual logic to run + re-try request
