from bs4 import BeautifulSoup
from ..base import PageGrabber
from ...colors.default_colors import DefaultBodyColors as bc
import requests
import configparser
import pkg_resources


class LinkedInSalesGrabber(PageGrabber):
    """
    LinkedIn.com sales scraper for email lookups
    """

    config = []
    soup = ""
    client = {}
    homepageurl = ""
    loginurl = ""
    logouturl = ""
    viewbyemail = ""
    login_information = {
            'session_key': '',
            'session_password': '',
            'loginCsrfParam': '',
    }


    def __init__(self):
        """
        Load up LinkedIn plugin configs
        """
        super(LinkedInSalesGrabber, self).__init__()
        self.config = configparser.ConfigParser()
        get_plugin_cats = pkg_resources.resource_filename('skiptracer','../../setup.cfg')
        self.config.read(get_plugin_cats)
        self.homepageurl = self.config['plugin.linkedin']['homepageurl']
        self.loginurl = self.config['plugin.linkedin']['loginurl']
        self.logouturl = self.config['plugin.linkedin']['logouturl']
        self.viewbyemail = self.config['plugin.linkedin']['viewbyemail']
        self.login_information['session_key'] = self.config['plugin.linkedin']['sessionkey']
        self.login_information['session_password'] = self.config['plugin.linkedin']['sessionpassword']
        self.client = requests.Session()  # Establish the session()
        source = self.client.get(self.homepageurl).content  # Request source
        self.soup = self.get_dom(source)  # BS DOM



    def grab_data(self, el, attr, attrval, title, gettext):
        """
        Pass to this function the following:
        el = element to find e.g. div
        attr = attribute to find e.g. class or id
        attrval = attribute value to find e.g. li-profile-name
        title = Title to display is results e.g. Name, Phone
        """

        try:
            if gettext == False:
                val = self. grab_data_attr()
            else:
                val = self.grab_data_text(el, attr, attrval, gettext)

            print("  [" + bc.CGRN + "+" + bc.CEND + "] " +
                  bc.CRED + title +": " + bc.CEND + str(company))
        except BaseException:
            val = ""
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No "+title+" can be found.\n"+bc.CEND)
            pass
        return val


    def grab_data_text(self, el, attr, attrval):
        """
        Pass to this function the following:
        el = element to find e.g. div
        attr = attribute to find e.g. class or id
        attrval = attribute value to find e.g. li-profile-name
        """

        return self.soup.find(el,{attr: attrval}).get_text()


    def grab_data_attr(self, el, attr, attrval, title):
        """
        Pass to this function the following:
        el = element to find e.g. div
        attr = attribute to find e.g. class or id
        attrval = attribute value to find e.g. li-profile-name
        getext = attribute text to grab e.g. href
        """

        return self.soup.find(el, attrs={attr: attrval})[gettext]


    def grab_name(self):
        """
        Grabs a first + last name from LinkedIn DOM
        and constructs a single name string
        """

        try:
            fname = self.grab_data('span','id','li-profile-name','First name','data-fname')
            lname = self.grab_data('span','id','li-profile-name','Last name','data-lname')
            name = str(fname) + " " + str(lname)
            print("  [" + bc.CGRN + "+" + bc.CEND + "] " + bc.CRED +
                  "Name: " + bc.CEND + str(fname) + " " + str(lname))
        except BaseException:
            name = ""
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No username can be found.\n"+bc.CEND)
        return name


    def grab_csrf(self):
        """
        Grab CSRF token
        """

        csrf = self.soup.find(id="loginCsrfParam-login")['value']
        self.login_information['loginCsrfParam'] = csrf


    def get_info(self, email, category):
        """
        Requires AUTH, login and request AUTHENTICATED pages from linkedin
        """

        print("[" + bc.CPRP + "?" + bc.CEND + "] " + bc.CCYN + "LinkedIn" + bc.CEND)
        self.grab_csrf()

        if self.login_information['session_key'] == '':
            # If no modifications of default u/p, print error, return
            if login_information['session_password'] == '':
                print(
                    "  [" +
                    bc.CRED +
                    "X" +
                    bc.CEND +
                    "] " +
                    bc.CYLW +
                    "This module requires authentication to use it properly.\n" +
                    bc.CEND)
                return

        results = "None"
        try:
            self.client.post(self.loginurl, data=self.login_information)
            results = client.get(self.viewbyemail + str(email)).text
        except Exception as failedlinkedinauth:
            print(("  [" +
                   bc.CRED +
                   "X" +
                   bc.CEND +
                   "] " +
                   bc.CYLW +
                   "This module did not properly authenticate: %s" +
                   bc.CEND) %
                  failedlinkedinauth)

        self.soup = self.get_dom(results)
        self.get_source(self.logouturl)  # Log out of LinkedIn, kills sessionID
        profile = self.grab_data('a', 'class', 'li-hover-under li-txt-black-85',
                       'Profile', 'href')
        name = self.grab_name()
        location = self.grab_data('div', 'class', 'li-user-location',
                       'Location', False)
        company = self.grab_data('span', 'class', 'li-user-title-company',
                       'Company', False)
        title = self.grab_data('div', 'class', 'li-user-title',
                       'Job Title', False)
        email = self.grab_data('span', 'id', 'email', 'Email', False)

        self.info_dict.update({
            "profile": profile,
            "name": name,
            "location": location,
            "company": company,
            "title": title,
            "email": email
        })

        print()
        return self.info_dict
