from __future__ import absolute_import, print_function

#
# TruePeopleSearch.com scraper
#
from ..base import PageGrabber
from .. import proxygrabber
from ...colors.default_colors import DefaultBodyColors as bc
import re

try:
    import __builtin__ as bi
except ImportError:
    import builtins as bi

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

import operator

class TruePeopleGrabber(PageGrabber):
    """
    Check for CAPTCHA, if proxy enabled,try new proxy w/ request, else
    report to STDOUT about CAPTCHA
    """
    source = ""
    soup = ""
    url = ""
    url2 = "" #rid URL

    def __init__(self):
        """
        Load up LinkedIn plguin configs
        """
        super(TruePeopleGrabber, self).__init__()


    def get_info(self, information, lookup):
        """
        Uniform call for framework to launch function in a way to single out the
        calls per URL
        """
        print("[" + bc.CPRP + "?" + bc.CEND + "] " +
              bc.CCYN + "TruePeopleSearch" + bc.CEND)

        self.true_try(lookup, information)


    def check_for_captcha(self):
        captcha = self.soup.find('div', attrs={'class': 'g-recaptcha'})
        print(captcha)
        if bi.webproxy and captcha is not None:
            try:
                print("  [" + bc.CRED + "X" + bc.CEND + "] " + bc.CYLW +
                      "Switching proxy, trying again...\n" + bc.CEND)
                bi.proxy = proxygrabber.new_proxy()
                self.true_try(lookup, information)
                return True
            except Exception as badproxy:
                print("  [" + bc.CRED + "X" + bc.CEND + "] " + bc.CYLW +
                      "Bad proxy...\n" + bc.CEND)
                pass
        if captcha is not None:
            print(
                "  [" +
                bc.CRED +
                "X" +
                bc.CEND +
                "] " +
                bc.CYLW +
                "Captch detected, use a proxy or complete challenge in browser\n" +
                bc.CEND)
            return True
        else:
            return False


    def makephone(self, information):
        """
        Find user supplied data format, adjust as needed for URL
        """
        try:
            if str(information).split("-")[1]:
                dashphone = '({})-{}-{}'.format(
                    information[0:3], information[5:8], information[9:])
                return dashphone
        except Exception as e:
            pass
        try:
            if str(information).split(" ")[
                    1]:  # Can it be split by a whitespace, if so, break and format as needed for the URL
                dashphone = '({})-{}-{}'.format(
                    information[0:3], information[5:8], information[9:])
                return dashphone
        except Exception as e:
            pass
        try:
            # If len of data is 10 and is an integer, break and format
            # as needed for URL
            if len(information) == 10:
                dashphone = '({})-{}-{}'.format(
                    information[0:3], information[3:6], information[6:])
                return dashphone
        except Exception as e:
            print(
                "  [" +
                bc.CRED +
                "X" +
                bc.CEND +
                "] " +
                bc.CYLW +
                "Did not detect a phone number\n" +
                bc.CEND)
            return

    def phone(self, information):
        """
        Create the URL with the phone number
        """
        phonere = re.compile('(\d\d\d\d\d\d\d\d\d\d|\d\d\d[\s.-]\d\d\d[\s.-]\d\d\d\d)')

        if phonere.findall(information):
            self.url = 'https://www.truepeoplesearch.com/results?phoneno={}'.format(
                        makephone(information))


    def name(self, information):
        """
        City state and zip lookup
        """
        agerange = raw_input(
            "  [" + bc.CRED + "!" + bc.CEND + "] " + bc.CYLW +
            "Please enter an age range, ex: 18-120 " + bc.CEND)
        citystatezip = raw_input(
            "  [" + bc.CRED + "!" + bc.CEND + "] " + bc.CYLW +
            "Please enter a city,state,or zip - ex: (AL|Alabama|12345) " +
            bc.CEND)
        if str(information).split(' ')[1]:
            self.url = "https://www.truepeoplesearch.com/results?name={}&agerange={}&citystatezip={}".format(
                str(information).replace(' ', '%20'), agerange, citystatezip)


    def find_all_shallow(self):
        """
        Check if any records were found
        """

        recordcount = self.soup.findAll('div', {'class', 'card-summary'})

        if len(recordcount) == 0:
            print("  [" + bc.CRED + "X" + bc.CEND + "] " +
                  bc.CYLW + "No results were found.\n" + bc.CEND)
            return False

        return True



    def get_rid(self, lookup, x):
        """
        Attempt to grab the
        rid.
        """
        rid = False
        try:
            if lookup == 'name':
                rid = str(x).split(";")[3].split('"')[0]
            if lookup == 'phone':
                rid = str(x).split(";")[1].split('"')[0]
        except Exception as e:
            print("  [" + bc.CRED + "X" + bc.CEND + "] " +
                  bc.CYLW + "No results were found.\n" + bc.CEND)
        finally:
            return rid


    def get_rid_source(self):
        """
        Grab the source of the page linked to
        the rid
        """
        got_source = False
        try:
            self.source2 = self.get_source(self.url2)
            got_source = True
        except Exception as e:
            print(e)
            got_source = False
        finally:
            return got_source


    def grab_name(self):
        """
        Grab the users name from
        the DOM
        """
        name = "Unknown"
        try:
            nc = self.soup2.find('span', {'class': 'h2'})
            nc1 = str(nc).split(">")[3]
            name = str(" ".join(str(nc1).split())).split("<")[0]
            print(("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                    bc.CRED + "Name: " + bc.CEND + "%s") % (name))
        except Exception as e:
            print(e)
        finally:
            return name

    def grab_age(self):
        """
        Grab the user age from the
        DOM
        """
        age = "Unknown"
        try:
            age1 = self.soup2.find('span', {'class': 'content-value'})
            age2 = " ".join(str(age1).split())
            age = age2.split(">")[1].split("<")[0].split()[1]
            print(("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                   bc.CRED + "Age: " + bc.CEND + "%s") % (age))
        except Exception as e:
            print(e)
        finally:
            return age


    def grab_akalist(self):
        """
        Grab the users AKA list from
        the DOM
        """
        aklist = "Unknown"
        try:
            aklist = []
            aka = self.soup2.find_all(
                'a', {'class': 'link-to-more', 'data-link-to-more': 'aka'})
            if len(aka) >= 1:
                print(
                    "  [" +
                    bc.CGRN +
                    "+" +
                    bc.CEND +
                    "] " +
                    bc.CRED +
                    "Alias: " +
                    bc.CEND)
                aka = set(aka)
                for xaka in aka:
                    print (xaka)
                    xakas = str(xaka).split('>')[1].split('<')[0]
                    aklist.append(xakas)
                    print(("    [" +
                           bc.CGRN +
                           "=" +
                           bc.CEND +
                           "] " +
                           bc.CRED +
                           "AKA: " +
                           bc.CEND +
                           "%s") %
                          (xakas))
        except Exception as e:
            print(e)
        finally:
            return aklist


    def grab_address(self):
        """
        Grab the users address
        from the DOM
        """
        address = "Unknown"
        try:
            address = self.soup2.find_all(
                'a', {'class': 'link-to-more', 'data-link-to-more': 'address'})
        except Exception as e:
            print(e)
        finally:
            return address

    def grab_related(self):
        """
        Grab the related values
        from the DOM
        """
        rellist = "Unknown"
        try:
            related = self.soup2.find_all(
                'a', {'class': 'link-to-more', 'data-link-to-more': 'relative'})
            print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                  bc.CRED + "Related:" + bc.CEND)
            related = set(related)
            rellist = []
            for xrelate in related:
                xrels = str(xrelate).split(">")[1].split("<")[0]
                rellist.append(xrels)
            for xrel in set(rellist):
                print(("      [" +
                       bc.CGRN +
                       "=" +
                       bc.CEND +
                       "] " +
                       bc.CRED +
                       "Known Relative: " +
                       bc.CEND +
                       "%s") %
                      xrel)
        except Exception as e:
            print(e)
        finally:
            return rellist


    def grab_associate(self):
        """
        Grab a list of associate data
        from the DOM
        """
        asso = "Unknown"
        try:
            associate = self.soup2.find_all(
                'a', {'class': 'link-to-more', 'data-link-to-more': 'associate'})
            associate = set(associate)
            print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                  bc.CRED + "Associate(s):" + bc.CEND)
            asso = []
            for xassociate in associate:
                assoc = str(xassociate).split(">")[1].split("<")[0]
                asso.append(assoc)
                print(("      [" +
                       bc.CGRN +
                       "=" +
                       bc.CEND +
                       "] " +
                       bc.CRED +
                       "Known Associate: " +
                       bc.CEND +
                       "%s") %
                      assoc)
        except Exception as e:
            print(e)
        finally:
            return asso

    def grab_prev_addr(self):
        """
        Grab previous address info
        from the DOM
        """
        prev = "Unknown"
        lives = "Unknown"
        try:
            curaddr = 0
            print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                  bc.CRED + "Address:" + bc.CEND)
            prev = []
            for xaddr in address:
                adr = " ".join(str(xaddr).split())
                adrs = " ".join(adr.split(">")[1::])
                addr = adrs.replace(
                    "<br/ ",
                    "").replace(
                    "</a",
                    "").strip()
                if curaddr == 0:
                    print(("    [" +
                           bc.CGRN +
                           "=" +
                           bc.CEND +
                           "] " +
                           bc.CRED +
                           "Current: " +
                           bc.CEND +
                           "%s") %
                          addr)
                    lives = addr
                else:
                    print(("    [" +
                           bc.CGRN +
                           "=" +
                           bc.CEND +
                           "] " +
                           bc.CRED +
                           "Previous: " +
                           bc.CEND +
                           "%s") %
                          addr)
                    prev.append(addr)
                curaddr += 1
        except Exception as e:
            print(e)
        finally:
            return prev, lives


    def grab_phone_list(self):
        """
        Grab a list of phone numbers
        from the DOM
        """
        plist = "Unknown"
        try:
            phone = self.soup2.find_all(
                'a', {'class': 'link-to-more', 'data-link-to-more': 'phone'})
            plist = []
            if len(phone) >= 1:
                print(
                    "  [" +
                    bc.CGRN +
                    "+" +
                    bc.CEND +
                    "] " +
                    bc.CRED +
                    "Phone: " +
                    bc.CEND)
                for xnum in phone:
                    try:
                        xnums = str(xnum).split(">")[1].split("<")[0]
                        plist.append(xnums)
                        print(("    [" +
                               bc.CGRN +
                               "=" +
                               bc.CEND +
                               "] " +
                               bc.CRED +
                               "#: " +
                               bc.CEND +
                               "%s") %
                              xnums)
                    except Exception as w:
                        pass
        except Exception as e:
            print(e)
        finally:
            return plist


    def find_all_deep(self, lookup):
        """
        Deep search for records
        """
        age = ""
        name = ""
        aklist = ""
        rellist = ""
        asso = ""
        prev = ""
        lives = ""
        plist = ""


        try:

            deep = self.soup.find_all(
                'a', {
                    'class': [
                        'btn', 'btn-success', 'btn-lg',
                        'detail-link', 'shadow-form'
                     ]}
            )

            for x in set(deep):
                rid = self.get_rid(lookup, x)
                if rid == False:
                    return False

                self.url2 = self.url + "&" + rid
                if self.get_rid_source() == False:
                    return False

                try:
                    self.soup2 = self.get_dom(self.source2)
                except Exception as e:
                    print(e)

                name = self.grab_name()
                age = self.grab_age()
                aklist = self.grab_akalist()
                address = self.grab_address()
                relist = self.grab_related()
                asso = self.grab_associate()
                prev, lives = self.grab_prev_addr()
                plist = self.grab_phone_list()

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


    def get_source_html(self):
        """
        grab the source files
        """
        self.source = self.get_source(self.url)
        self.soup = self.get_dom(self.source)

    def true_try(self, lookup, information):
        """
        Determins different URL constructs based on user supplied data
        """
        address_list = []
        if lookup == "phone":
            self.phone(information)

        if lookup == "name":
            self.name(information)

        if lookup in ['name', 'phone']:
            self.get_source_html()

        if self.check_for_captcha() == True:
            print(("  [" + bc.CRED + "X" + bc.CEND + "] " +
                   bc.CYLW + "Goto: {}" + bc.CEND).format(self.url)
            )

            self.iscomplete = raw_input(
                "  [" + bc.CRED + "!" + bc.CEND + "] " + bc.CYLW +
                "Have you completed the CAPTCHA? " + bc.CEND
            )

            if str(self.iscomplete).lower() in ['no', False, 0]:
                print("  [" + bc.CRED + "X" + bc.CEND + "] " + bc.CYLW +
                      "User has not completed the CAPTCHA\n" + bc.CEND)
                return
            else:
                self.get_source_html()

        if self.find_all_shallow():
            self.find_all_deep(lookup)
        else:
            return False


        print()
        return self.info_dict
