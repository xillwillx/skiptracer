from __future__ import print_function
from __future__ import absolute_import
from ..base import PageGrabber
from ...colors.default_colors import DefaultBodyColors as bc
from .. import proxygrabber

import logging
import json
import ast
import cfscrape
try:
    import __builtin__ as bi
except BaseException:
    import builtins as bi


class HaveIBeenPwwnedGrabber(PageGrabber):
    """
    HackedEmails.com scraper for email compromise lookups
    """

    def get_info(self, email, category):
        """
        Uniform call for framework
        """
        print("[" + bc.CPRP + "?" + bc.CEND + "] " +
              bc.CCYN + "HaveIbeenPwned" + bc.CEND)
        self.count = 0
        self.resurl = 0
        self.trymore(email)

    def trymore(self, email):
        """
        Actual logic for lookup and re-try
        """
        while self.resurl == 0:

            self.count += 1
            url = 'https://haveibeenpwned.com/api/v3/breachedaccount/{}'.format(
                email)

            scraper = cfscrape.create_scraper()
            headers = {
                'user-agent': self.ua,
                'hibp-api-key': self.env['HAVEIBEENPWNED_API_KEY']
            }
            self.source = scraper.get(url, headers=headers).content
            self.source = str(
                self.source).replace(
                "true",
                "True").replace(
                "false",
                "False")

            self.source = ast.literal_eval(self.source)  # cast string to bytes
            self.source = self.source.decode('utf8')  # decode string
            self.source = ast.literal_eval(self.source)  # cast string to dict

            self.resurl = 1
            for dataset in self.source:
                self.result = dataset

                if self.result:
                    self.breach = self.result['BreachDate']
                    self.domain = self.result['Domain']
                    self.title = self.result['Title']
                    self.exposes = self.result['DataClasses']
                    self.info_dict.update(
                        {
                            "BreachDate": self.breach,
                            "Domain": self.domain,
                            "Title": self.title,
                            "DataExposed": self.exposes})
                    print(
                        "  [" +
                        bc.CGRN +
                        "+" +
                        bc.CEND +
                        "] " +
                        bc.CRED +
                        "Dump Name: " +
                        bc.CEND +
                        self.title)
                    print(
                        "    [" +
                        bc.CGRN +
                        "=" +
                        bc.CEND +
                        "] " +
                        bc.CRED +
                        "Domain: " +
                        bc.CEND +
                        self.domain)
                    print(
                        "    [" +
                        bc.CGRN +
                        "=" +
                        bc.CEND +
                        "] " +
                        bc.CRED +
                        "Breach: " +
                        bc.CEND +
                        self.breach)
                    print(
                        "    [" +
                        bc.CGRN +
                        "=" +
                        bc.CEND +
                        "] " +
                        bc.CRED +
                        "Exposes: " +
                        bc.CEND)
                    for xpos in self.exposes:
                        print(
                            "      [" +
                            bc.CGRN +
                            "-" +
                            bc.CEND +
                            "] " +
                            bc.CRED +
                            "DataSet: " +
                            bc.CEND +
                            xpos)
                else:
                    print(
                        "  [" +
                        bc.CRED +
                        "X" +
                        bc.CEND +
                        "] " +
                        bc.CYLW +
                        "No results were found.\n" +
                        bc.CEND)

            print()
            return self.info_dict
