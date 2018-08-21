from __future__ import print_function
#######################################################################
#       myspace scraper - returns user url of email address           #
#######################################################################

from ..base import PageGrabber
from ...colors.default_colors import DefaultBodyColors as bc
import re
import logging

try:
    import __builtin__ as bi
except BaseException:
    import builtins as bi


class MySpaceGrabber(PageGrabber):
    """
    Myspace.com scraper for email lookups
    """

    def __init__(self):
        """
        Load up MySpaceGrabber plugin configs
        """
        super(MySpaceGrabber, self).__init__()

    def get_name(self, soup):
        """
        Check if a name exists
        """
        name = False
        try:
            name = soup.select('h6')[0].text.strip()
        except BaseException:
            print("  [" + bc.CRED + "X" + bc.CEND + "] " +
                  bc.CYLW + "No Myspace account found.\n" + bc.CEND)
        finally:
            return name

    def get_acct_dets(self, soup):
        """
        Get the account details
        """
        account = False
        try:
            accountr = soup.select('h6')[0].a.get('href').strip()
            account = "https://myspace.com{}".format(accountr)
        except BaseException:
            print("  [" + bc.CRED + "X" + bc.CEND + "] " +
                  bc.CYLW + "No Myspace account found.\n" + bc.CEND)
        finally:
            return account

    def get_location_from_acct(self, account):
        """
        Get location data using the
        account data
        """
        location = "Unknown"
        try:
            source = self.get_source(account)
            soup = self.get_dom(source)
            location = soup.find('div', attrs={'class': 'location_white location '})[
                'data-display-text']
        except BaseException:
            print("  [" + bc.CRED + "X" + bc.CEND + "] " + bc.CYLW +
                  "Unable to find location data for "+account+".\n" + bc.CEND)
        finally:
            return location


    def get_info(self, email, category):
        """
        Looksup user accounts by given email
        """
        print("[" + bc.CPRP + "?" + bc.CEND + "] " +
              bc.CCYN + "Myspace" + bc.CEND)
        url = 'https://myspace.com/search/people?q={}'.format(email)
        source = self.get_source(url)
        soup = self.get_dom(source)
        name = self.get_name(soup)
        location = "Unknown"
        account = "Not found"

        if name != False:
            account = self.get_acct_dets(soup)
            if account != False:
                location = self.get_location_from_acct(account)

        print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
              bc.CRED + "Acct: " + bc.CEND + str(account))
        print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
              bc.CRED + "Name: " + bc.CEND + str(name))
        print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
              bc.CRED + "Loc:  " + bc.CEND + str(location) + "\n")
        self.info_dict.update({
            "name": name,
            "account": account,
            "location": location,
        })

        return self.info_dict
