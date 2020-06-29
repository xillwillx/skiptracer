"""Whocallid.com search module"""
from __future__ import print_function
from __future__ import absolute_import
from ..base import PageGrabber
from ...colors.default_colors import DefaultBodyColors as bc
import re
import logging
try:
    import __builtin__ as bi
except BaseException:
    import builtins as bi


class WhoCallIdGrabber(PageGrabber):
    """
    WhoCallID sales scraper for reverse telephone lookups
    """

    def get_name(self):
        """
        Grab the users name
        """
        name = "Unknown"
        try:
            name = self.soup.find('h2', attrs={'class': 'name'})
            if name:
                name = name.text.strip()
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Name: " + bc.CEND + str(name))
        except BaseException:
            pass
        finally:
            return name

    def get_location(self):
        """
        Get the location
        """
        location = "Unknown"
        try:
            location = self.soup.find('h3', attrs={'class': 'location'})
            if location:
                location = location.text.strip()
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Location: " + bc.CEND + str(location))
        except BaseException:
            pass
        finally:
            return location

    def get_phone_type(self):
        """
        Get the phone type
        """
        phone_type = "Unknown"
        try:
            phone_type = self.soup.find("img").attrs['alt']
            if phone_type:
                phone_type = phone_type.strip()
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Phone Type: " + bc.CEND + str(phone_type))
        except BaseException:
            pass
        finally:
            return phone_type

    def get_carrier(self, phone_number):
        """
        Get the phone carrier info
        """
        carrier = ""
        try:
            self.url = "https://whocalld.com/+1{}?carrier".format(phone_number)
            self.source = self.get_source(self.url)
            self.soup = self.get_dom(self.source)
            carrier = soup.find('span', attrs={'class': 'carrier'})
        except BaseException:
            pass
        finally:
            return carrier

    def process_carrier(self, carrier):
        """
        Take the carrier info and process it
        """
        try:
            if carrier:
                carrier = carrier.text
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Carrier: " + bc.CEND + str(carrier))
            else:
                carrier = ""
        except BaseException:
            carrier = ""
        finally:
            return carrier

    def get_city(self):
        """
        Grab the city info
        """
        city = ""
        try:
            city = self.soup.find('span', attrs={'class': 'city'})
            if city:
                city = city.text
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "City: " + bc.CEND + str(city))
        except BaseException:
            pass
        finally:
            return city

    def get_state(self):
        """
        Grab the state info
        """
        state = ""
        try:
            state = self.soup.find('span', attrs={'class': 'state'})
            if state:
                state = state.text
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "State: " + bc.CEND + str(state))
        except BaseException:
            pass
        finally:
            return state

    def get_time(self):
        """
        Grab time info
        """
        time = ""
        try:
            time = self.soup.find('span', attrs={'class': 'time'})
            if time:
                time = time.text
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Time: " + bc.CEND + str(time))
        except BaseException:
            pass
        finally:
            return time

    def get_info(self, phone_number, lookup):
        """
        Request, scrape and return values found
        """
        print("[" + bc.CPRP + "?" + bc.CEND + "] " +
              bc.CCYN + "WhoCalld" + bc.CEND)
        # Get phone info
        self.url = 'https://whocalld.com/+1{}'.format(phone_number)
        self.source = self.get_source(self.url)
        self.soup = self.get_dom(self.source)
        if self.soup.body.find_all(string=re.compile(
                '.*{0}.*'.format('country')), recursive=True):
            print("  [" + bc.CRED + "X" + bc.CEND + "] " +
                  bc.CYLW + "No WhoCallID data returned\n" + bc.CEND)
            return

        name = self.get_name()
        location = self.get_location()
        phone_type = self.get_phone_type()
        carrier = self.get_carrier(phone_number)
        carrier = self.process_carrier(carrier)
        city = self.get_city()
        state = self.get_state()
        time = self.get_time()

        self.info_dict.update({
            "carrier": carrier,
            "city": city,
            "location": location,
            "name": name,
            "phone_type": phone_type,
            "state": state,
            "time": time
        })

        print()
        return self.info_dict
