from __future__ import absolute_import, print_function

#
# TruePeopleSearch.com scraper
#
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


class TruthFinderGrabber(PageGrabber):
    def check_for_captcha(self):  # Check for CAPTCHA, if proxy enabled,try new proxy w/ request, else report to STDOUT about CAPTCHA
        captcha = self.soup.find('div', attrs={'class':'g-recaptcha'})
        if captcha != None:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Captcha detected, use a proxy or complete challenge in browser\n"+bc.CEND)
            return True
        else:
            return False

    def truth_try(self,lookup,information):  # builds out different URL constructs based on user supplied data
        address_list = []
        if lookup == "phone":
            phonere = re.compile('(\d\d\d\d\d\d\d\d\d\d|\d\d\d[\s.-]\d\d\d[\s.-]\d\d\d\d)')
            def makephone(information):  # Find user supplied data format, adjust as needed for URL
                try:
                    if str(information).split("-")[1]:  # Can it be split bu a "-", everything is ok
                        dashphone = '({})-{}-{}'.format(information[0:3], information[5:8], information[9:])
                        return dashphone
                except:
                    pass
                try:
                    if str(information).split(" ")[1]:  # Can it be split by a whitespace, if so, break and format as needed for the URL
                        dashphone = '({})-{}-{}'.format(information[0:3], information[5:8], information[9:])
                        return dashphone
                except:
                    pass
                try:
                    if len(information)== 10:  # If len of data is 10 and is an integer, break and format as needed for URL
                        dashphone = '({})-{}-{}'.format(information[0:3], information[3:6], information[6:])
                        return dashphone
                except:
                    print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Did not detect a phone number\n"+bc.CEND)
                    return
            if phonere.findall(information):  # Make the URL for a phone lookup, set email to False
                try:
                    self.url = 'https://www.truepeoplesearch.com/results?phoneno={}'.format(makephone(information))
                    email = False
                except Exception as e:
                    pass
        if lookup == "name":  # Make the URL for name lookup, set email to False
            citystatezip = raw_input("[{}?{}] {}Please enter a city,state,or zip?{} [ex:(AL=Alabama|CO=Colorado){}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
            gender = raw_input("[{}?{}] {}Please enter the targets biological sex?{} [ex:(M|F){}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
            age = raw_input("[{}?{}] {}Is the person older than 30?{} [ex:(Y|n){}]: ".format(bc.CRED,bc.CEND,bc.CRED,bc.CYLW,bc.CEND))
            def getlocal(citystatezip,gender,age):
                try:
                    if citystatezip:
                        self.state = citystatezip
                except:
                    self.state = "ALL"
                try:
                    if age:
                        self.age = "true"
                except:
                    self.age = "false"
                try:
                    if gender:
                        self.gndr = "&gender={}".format(gender)
                except:
                    self.gndr = "&gender="
                try:
                    if len(str(information).split(' ')) in [2,3]:
                        if len(str(information).split(' ')) == 2:
                            self.fname = str(information).split(" ")[0]
                            self.lname = str(information).split(" ")[1]
                        if len(str(information).split(' ')) == 3:
                            self.fname = str(information).split(" ")[0]
                            self.lname = str(information).split(" ")[2]
                except:
                    print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Failed to parse serarch string, lookup name.\n"+bc.CEND)
            getlocal(citystatezip,gender,age)
            self.url = "https://www.truthfinder.com/results/?utm_source=VOTER&traffic%5Bsource%5D=VOTER&utm_medium=pre-pop&traffic%5Bmedium%5D=pre-pop&utm_campaign=&traffic%5Bcampaign%5D=srapi%3A&utm_term=1&traffic%5Bterm%5D=1&utm_content=&traffic%5Bcontent%5D=&s1=&s2=srapi&s3=1&s4=&s5=&city=&firstName={}&lastName={}&page=r&state={}{}&qLocation=true&qRelatives=true&qOver30={}".format(self.fname, self.lname, self.state, self.gndr, self.age)
            email = False
        self.source = self.get_source(self.url)
        self.soup = self.get_dom(self.source)
        try:
            ul = self.soup.findAll("ul")
            for xul in ul:
                perlen = len(str(xul).split("\n"))
                broken = str(xul).split("\n")
                if perlen >=10:  # Check is len is greater than 10 to futher process
                    try:
                        name = broken[3].split("<")[0]  # should be static to the results (searched name)
                        print(("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Name: "+bc.CEND+"%s") % (name))
                        try:
                            akaloc = broken.index('aka:')+1  # find position + 1 space to left
                            aka = broken[akaloc].split("<")[0].replace(", ",",")  # grab actual dataset
                            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Alias: "+bc.CEND)
                            akalist = sorted(set(str(aka).split(",")))  # set sorted unique
                            for xaka in akalist:  # for each entry in sorted unique list
                                print(("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"AKA: "+bc.CEND+"%s") % (xaka))
                        except:  # in case of failure
                            akalist = ['unknown']
                            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"AKA: "+bc.CEND+"Unknown")
                            pass
                        try:
                            ageloc = broken.index('<li class="age">')+2
                            age = broken[ageloc].split(">")[1].split("<")[0]
                            if age:
                                print(("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Age: "+bc.CEND+"%s") % (age))
                        except:
                            age = 'unknown'
                            print(("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Age: "+bc.CEND+"%s") % (age))
                            pass
                        try:
                            locloc = broken.index('<li class="location">')+2
                            locations = broken[locloc]
                            locations = locations.replace(", <span>",":").replace("</span></li>",",").replace("<li>", " ").replace(", </ul>","")
                            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Location(s): "+bc.CEND)
                            for xlocal in locations.split(","):
                                print(("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"City:State:"+bc.CEND+"%s") % (xlocal))
                        except:
                            locals = ['unknown']
                            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Location: "+bc.CEND+"Unknown")
                            pass
                        try:
                            relloc = broken.index('<li class="relatives">')+1
                            if broken[relloc].split('"')[1] == "No Relatives":
                                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Relative(s): "+bc.CEND+"Unknown")
                            else:
                                print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Relative(s): "+bc.CEND)
                                relatives = broken[int(relloc)+2].replace("\n",",")
                                relatives = relatives.replace("</li>",",").replace("<li>","").replace(", </ul>","")
                                relate = relatives.split(",")
                                for xrel in sorted(set(relate)):
                                    print(("    ["+bc.CGRN+"="+bc.CEND+"] "+bc.CRED+"Related: "+bc.CEND+"%s") % (xrel))
                        except:
                            relate = ['unknown']
                            pass
                    except:
                        pass
                    print()
                    self.info_dict.update({
                                           "name": name,
                                           "age": age,
                                           "aka": sorted(set(akalist)),
                                           "locations": sorted(set(locals)),
                                           "relatives": sorted(set(relate)),
                                         })
                    bi.outdata['truthfinder'] = self.info_dict
        except:
            pass

    def get_info(self, lookup, information):  # Uniform call for framework to launch function in a way to single out the calls per URL
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "TruthFinder" + bc.CEND)
        self.truth_try(lookup,information)  # Actual logic to run + re-try request
