#######################################################################
#       whoismind scraper - returns domains associated with email     #
#######################################################################

from __future__ import print_function
from ..base import PageGrabber
from ...colors.default_colors import DefaultBodyColors as bc
import numpy as np

try:
    import __builtin__ as bi
except ImportError:
    import builtins as bi


class WhoisMindGrabber(PageGrabber):
    """
    WhoisMind scraper for registered domains by email lookups
    """

    def __init__(self):
        """
        Load up WhoisMindGrabber plugin configs
        """
        super(WhoisMindGrabber, self).__init__()


    def get_info(self, email, category):
        """
        Request and processes results, sorted unique, remove blanks
        """
        try:
            print("[" + bc.CPRP + "?" + bc.CEND + "] " +
                  bc.CCYN + "WhoisMind" + bc.CEND)
            url = 'http://www.whoismind.com/email/{}{}'.format(email, '.html')
            source = self.get_source(url)
            soup = self.get_dom(source)
            href = soup.findAll('a')

        except Exception as urlgrabfailed:
            print("  [" + bc.CRED + "X" + bc.CEND + "] " + bc.CYLW +
                  "WhoisMind failed to produce the URL" + bc.CEND)
        whoisdb = list()

        try:
            for hreftag in href:
                if hreftag.text != "" and hreftag.text in hreftag['href']:
                    domain = hreftag.text
                    print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                          bc.CRED + "Domain: " + bc.CEND + domain)
                    whoisdb.append({"domain": domain})
        except Exception as whoisfailed:
            print("  [" + bc.CRED + "X" + bc.CEND + "] " +
                  bc.CYLW + "WhoisMind returned no results" + bc.CEND)
            return
        if len(whoisdb) == 0:
            print("  [" + bc.CRED + "X" + bc.CEND + "] " +
                  bc.CYLW + "WhoisMind returned no results" + bc.CEND)
        else:
            self.info_list.append(list(np.unique(np.array(whoisdb))))
            bi.outdata['whoismind'] = self.info_list[0]
        print()
        return self.info_list
