from __future__ import print_function
from __future__ import absolute_import

from ..base import PageGrabber
from ...colors.default_colors import DefaultBodyColors as bc
from .. import proxygrabber
from time import sleep

import re
import logging
import json
import base64 as b64
import sys

try:
    import __builtin__ as bi
except BaseException:
    import builtins as bi


class AdvanceBackgroundGrabber(PageGrabber):
    """
    Grab data from Advanced Background
    site
    """
    url = ""

    def __init__(self):
        """
        Load up AdvanceBackgroundGrabber plugin configs
        """
        super(AdvanceBackgroundGrabber, self).__init__()

    def get_info(self, lookup, information):
        """
        Uniform call for framework to launch function in a way to single out the
        calls per URL
        """
        print("[" + bc.CPRP + "?" + bc.CEND + "] " +
              bc.CCYN + "AdvanceBackgroundChecks" + bc.CEND)

        self.abc_try(lookup, information)

    def check_for_captcha(self):
        """
        Check for CAPTCHA, if proxy enabled,try new proxy w/ request, else
        report to STDOUT about CAPTCHA
        """
        captcha = self.soup.find('div', attrs={'class': 'g-recaptcha'})

        if bi.webproxy and captcha is not None:
            try:
                print("  [" + bc.CRED + "X" + bc.CEND + "] " + bc.CYLW +
                      "Switching proxy, trying again...\n" + bc.CEND)
                bi.proxy = proxygrabber.new_proxy()
                self.abc_try(lookup, information)
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
        Format the phone number splitting on
        whitespace or hyphens
        """
        try:
            if str(information).split("-")[1]:
                dashphone = information
                return dashphone
        except BaseException:
            pass

        try:
            if str(information).split(" ")[1]:
                dashphone = '{}-{}-{}'.format(
                    information[0:3], information[5:8], information[9:])
                return dashphone
        except BaseException:
            pass

        try:
            # If len of data is 10 and is an integer, break and format
            # as needed for URL
            if len(information) == 10:
                dashphone = '{}-{}-{}'.format(
                    information[0:3], information[3:6], information[6:])
                return dashphone
            if len(information) != 10:
                print(
                    "  [" +
                    bc.CRED +
                    "X" +
                    bc.CEND +
                    "] " +
                    bc.CYLW +
                    "Check search string, should be 10 digits.\n" +
                    bc.CEND)
                return
        except BaseException:
            return

    def grab_phone(self, information):
        """
        Create phone number format
        """
        try:
            self.num = self.makephone(information)
            if self.num is None:
                return
            self.url = "https://www.advancedbackgroundchecks.com/{}".format(
                self.num)
        except Exception as e:
            print(
                "  [" +
                bc.CRED +
                "X" +
                bc.CEND +
                "] " +
                bc.CYLW +
                "Could not produce required URL.\n" +
                bc.CEND)
            return

    def grab_email(self, information):
        """
        Grab the targets email
        """

        if str(information).split('@')[1]:
            email = str(
                b64.b64encode(
                    information.encode('utf-8'))).split("b'")[1]
            email = email.split("'")[0]
            self.url = "https://www.advancedbackgroundchecks.com/emails/" + email

    def grab_name(self, information):
        """
        Grab the targets Name
        """
        if str(information).split(' ')[1]:
            self.url = "https://www.advancedbackgroundchecks.com/name/{}".format(
                str(information).replace(' ', '-'))

    def find_results(self, lookup):
        """
        Check if the search found any results.
        If so return them, otherwise return an
        empty string
        """
        script_html = ""

        if self.soup.find(
                'div', {'id': 'no-result-widgets'}):  # Report if there are no results to STDOUT
            print("  [" + bc.CRED + "X" + bc.CEND + "] " +
                  bc.CYLW + "No results were found.\n" + bc.CEND)
            return script_html

        checkres = self.soup.findAll("h1")

        if lookup == "phone":
            for xcheck in checkres:
                if xcheck.text in [
                        "We could not find any results based on your search criteria.  Please review your search and try again, or try our sponsors for more information.", "Top Results for " + str(self.num)]:
                    print("  [" + bc.CRED + "X" + bc.CEND + "] " +
                          bc.CYLW + "No results were found.\n" + bc.CEND)
                    return script_html

        script_html = self.soup.find_all(
            'script', type="application/ld+json")  # Scrape for JSON within DOM

        return script_html

    def grab_json_data(self, script_html):
        """
        Grab the JSON data and load it
        """
        script_html = script_html.get_text().strip()  # Format data for JSON load
        script_html = script_html.replace("\n", "")
        script_html = script_html.replace("\t", "")
        person_list = json.loads(script_html)  # Loads data as JSON
        return person_list

    def get_person_list(person_list):
        """
        Iterate through person list
        and grab results
        """
        for person in person_list:
            addrfirst = 0
            pnext = 0
            if pnext >= 1:
                print(" [" + bc.CGRN + "!" + bc.CEND + "] " +
                      bc.CRED + "Next finding: " + bc.CEND)

            self.url2 = person['@id']  # set additional 2nd level URL
            self.source2 = self.get_source(self.url2)  # request 2nd level url
            self.soup2 = self.get_dom(self.source2)  # grab 2nd level DOM
            script_html2 = self.soup2.find_all(
                'script', type="application/ld+json")  # Scrape for JSON within DOM
            print("  [" + bc.CGRN + "+" + bc.CEND + "] " + bc.CRED +
                  "Name: " + bc.CEND + str(person.get("name")))

            if person.get("birthDate"):  # Set DoB
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " + bc.CRED +
                      "D.o.B: " + bc.CEND + str(person.get("birthDate")))

            if person.get("additionalName"):  # Set additional names AKA
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Alias: " + bc.CEND)

                for xaka in person.get(
                        "additionalName"):  # For each AKA, select the name
                    print(
                        "    [" +
                        bc.CGRN +
                        "=" +
                        bc.CEND +
                        "] " +
                        bc.CRED +
                        "AKA: " +
                        bc.CEND +
                        str(xaka))

            if len(script_html2) <= 1:
                print(
                    " [" +
                    bc.CRED +
                    "X" +
                    bc.CEND +
                    "] " +
                    bc.CYLW +
                    "Unable to re-try request... Try again later...\n" +
                    bc.CEND)
                return
            else:
                script_html2 = script_html2[1]
                script_html2 = script_html2.get_text().strip()  # Format data for JSON load
                script_html2 = script_html2.replace("\n", "")
                script_html2 = script_html2.replace("\t", "")
                person_list2 = json.loads(script_html2)  # Loads dat
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Phone: " + bc.CEND)

                for tele in person_list2['telephone']:
                    print(
                        "    [" +
                        bc.CGRN +
                        "=" +
                        bc.CEND +
                        "] " +
                        bc.CRED +
                        "#: " +
                        bc.CEND +
                        str(tele))
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Email: " + bc.CEND)

                for email in person_list2['email']:
                    print("   [" + bc.CGRN + "=" + bc.CEND + "] " +
                          bc.CRED + "Addr: " + bc.CEND + str(email))

            if person.get("address"):  # Set Addresses
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Addresses.: " + bc.CEND)
                for addy in person.get(
                        "address"):  # For each address, select the information and store
                    addrfirst += 1
                    if addrfirst == 1:
                        print(
                            "    [" +
                            bc.CGRN +
                            "=" +
                            bc.CEND +
                            "] " +
                            bc.CRED +
                            "Current Address: " +
                            bc.CEND)
                    else:
                        print(
                            "    [" +
                            bc.CGRN +
                            "=" +
                            bc.CEND +
                            "] " +
                            bc.CRED +
                            "Prev. Address: " +
                            bc.CEND)
                    print("      [" +
                          bc.CGRN +
                          "-" +
                          bc.CEND +
                          "] " +
                          bc.CRED +
                          "Street: " +
                          bc.CEND +
                          str(addy.get("streetAddress")))
                    print("      [" +
                          bc.CGRN +
                          "-" +
                          bc.CEND +
                          "] " +
                          bc.CRED +
                          "City: " +
                          bc.CEND +
                          str(addy.get("addressLocality")))
                    print("      [" +
                          bc.CGRN +
                          "-" +
                          bc.CEND +
                          "] " +
                          bc.CRED +
                          "State: " +
                          bc.CEND +
                          str(addy.get("addressRegion")))
                    print("      [" +
                          bc.CGRN +
                          "-" +
                          bc.CEND +
                          "] " +
                          bc.CRED +
                          "ZipCode: " +
                          bc.CEND +
                          str(addy.get("postalCode")))
                    address_list.append({"city": addy.get("addressLocality"),
                                         "state": addy.get("addressRegion"),
                                         "zip_code": addy.get("postalCode"),
                                         "address": addy.get("streetAddress")})

            if person.get("relatedTo"):  # Set Relatives
                print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                      bc.CRED + "Related: " + bc.CEND)
                for xrelate in [item.get("name") for item in person.get(
                        "relatedTo")]:  # For each relative, select the information and store
                    print(
                        "    [" +
                        bc.CGRN +
                        "=" +
                        bc.CEND +
                        "] " +
                        bc.CRED +
                        "Known Relative: " +
                        bc.CEND +
                        str(xrelate))
            self.info_list.append({"name": person.get("name"),
                                   "birth_date": person.get("birthDate"),
                                   "additional_names": person.get("additionalName"),
                                   "telephone": person_list2['telephone'],
                                   "email": person_list2['email'],
                                   "address_list": address_list,
                                   "related_to": [item.get("name") for item in person.get("relatedTo")]})
            pnext += 1

    def abc_try(self, information, lookup):
        """
        Determins different URL constructs based on user supplied data
        """

        address_list = []
        if lookup == "phone":
            self.grab_phone(information)

        if lookup == "email":  # Make the URL for email lookup, set email True
            self.grab_email(information)

        if lookup == "name":  # Make the URL for name lookup, set email to False
            self.grab_name(information)

        self.source = self.get_source(self.url)
        self.soup = self.get_dom(self.source)

        if self.check_for_captcha() == True:

            print(("  [" + bc.CRED + "X" + bc.CEND + "] " +
                   bc.CYLW + "Goto: {}" + bc.CEND).format(self.url)
                  )

            self.iscomplete = input(
                "  [" + bc.CRED + "!" + bc.CEND + "] " + bc.CYLW +
                "Have you completed the CAPTCHA? " + bc.CEND
            )

            if str(self.iscomplete).lower() in ['no', False, 0]:
                print("  [" + bc.CRED + "X" + bc.CEND + "] " + bc.CYLW +
                      "User has not completed the CAPTCHA\n" + bc.CEND)
                return False

        script_html = self.find_results(lookup)

        if len(script_html) == 2:  # Check len on results
            # Set the desired value to iterate over
            script_html = script_html[1]
        else:
            print(
                "  [" +
                bc.CRED +
                "X" +
                bc.CEND +
                "] " +
                bc.CYLW +
                "Unable to complete request... Try again later...\n" +
                bc.CEND)
            return

        person_list = self.grab_json_data(script_html)
        self.get_person_list(person_list)

        print()
        return self.info_list
