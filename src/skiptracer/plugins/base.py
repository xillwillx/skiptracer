"""Base Scraping Class"""
from __future__ import print_function
from __future__ import absolute_import
from lxml import etree
from bs4 import BeautifulSoup
from . import proxygrabber
from dotenv import dotenv_values

import requests
import random
import requests
import json
# monkey patch socket to use only IPv4
import socket
import pkg_resources
import builtins as bi

og = socket.getaddrinfo

def ng(*args, **kwargs):
    res = og(*args, **kwargs)
    return [r for r in res if r[0] == socket.AF_INET]


socket.getaddrinfo = ng


def random_line():
    """
    Gets random User-Agent string from local DB file
    """
    get_user_agents = pkg_resources.resource_filename('skiptracer','../../storage/user-agents.db')
    afile = open(get_user_agents)
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2):
            continue
        line = aline
    return line.strip()


class PageGrabber:
    """
    Base PageGrabber Class
    Base function to import request functionality in modules
    """

    def __init__(self):
        """
        Initialize defaults as needed
        """
        self.env = dotenv_values()
        self.info_dict = {}
        self.info_list = []
        self.ua = random_line()
        self.proxy = {}


    def get_source(self, url):
        """
        Returns source code from given URL
        """
        headers = {"User-Agent": self.ua}
        reqcom = 0
        requests.packages.urllib3.disable_warnings()
        results = ""
    
        while reqcom < 5:
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
                reqcom = 5
            except Exception as failedreq:
                if bi.webproxy:
                    bi.proxy = proxygrabber.new_proxy()
                    reqcom = reqcom + 1
                else:
                    print(failedreq)
                    reqcom = reqcom + 1
        return results.encode('ascii', 'ignore').decode("utf-8")

    def post_data(self, url, data):
        """
        Sends POST request of given DATA, URL
        """
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

    def get_dom(self, source):
        """
        Returns BeautifulSoup DOM
        """
        return BeautifulSoup(source, 'lxml')

    def get_html(self, source):
        """
        Returns BeautifulSoup DOM
        """
        return BeautifulSoup(source, 'html.parser')
