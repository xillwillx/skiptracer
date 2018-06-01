"""Base Scraping Class"""
import requests
import random
import requests
from lxml import etree
from bs4 import BeautifulSoup
import proxygrabber
try:
    import __builtin__ as bi
except Exception as e:
    import builtins as bi
    print e
import json

def random_line():  # Gets random User-Agent string from local DB file
    afile = open("storage/user-agents.db")
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2):
            continue
        line = aline
    return line.strip()

class PageGrabber:  # base function to import request functionality in modules
    """Base PageGrabber Class"""
    def __init__(self):  # Initialize defaults as needed
        self.info_dict = {}
        self.info_list = []
        self.ua = random_line()
        if bi.proxy != '':
            proxy = str(bi.proxy).split(":")[1].strip()
            xproto = str(bi.proxy).split(":")[0].strip()
            self.proxy = {str(xproto): str(proxy).strip()}
        else:
            self.proxy = {}
    def get_source(self, url):  # Returns source code from given URL
        headers = {"User-Agent": self.ua}
        reqcom = 0
        requests.packages.urllib3.disable_warnings()
        while reqcom == 0:
            try:
                if bi.proxy != '':
                    proxy = str(bi.proxy).split(":")[1].strip()
                    xproto = str(bi.proxy).split(":")[0].strip()
                    self.proxy = {str(xproto): str(proxy).strip()}
                    results = requests.get(
                                url,
                                headers=headers,
                                proxies=self.proxy,
                                timeout=10,
                                verify=False,
                                allow_redirects=True
                                ).text
                else:
                    results = requests.get(
				url,
				headers=headers,
				timeout=10,
				verify=False,
				allow_redirects=True
				).text
                reqcom = 1
            except Exception as failedreq:
                if bi.webproxy:
    	            bi.proxy = proxygrabber.new_proxy()
        return results.encode('ascii', 'ignore').decode("utf-8")
    def post_data(self, url, data):  # Sends POST request of given DATA, URL
        headers = {"User-Agent": self.ua}
        reqcom = 0
        requests.packages.urllib3.disable_warnings()
        while reqcom == 0:
            try:
                results = requests.post(
                                url,
                                headers=headers,
                                proxies=self.proxy,
                                timeout=10,
                                verify=False,
                                allow_redirects=True,
                                data=postdata
                                ).text
                reqcom = 1
                return results.encode('ascii', 'ignore').decode("utf-8")
            except Exception as failedreq:
                if bi.webproxy:
                    bi.proxy = proxygrabber.new_proxy()
        return
    def get_dom(self, source):  # Returns BeautifulSoup DOM
        return BeautifulSoup(source, 'lxml')
    def get_html(self, source):  # Returns BeautifulSoup DOM
        return BeautifulSoup(source, 'html.parser')
