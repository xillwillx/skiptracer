#
# LinkedIn Sales Module
#
import requests
from bs4 import BeautifulSoup
import logging
from base import PageGrabber
from colors import BodyColors as bc
try:
    import __builtin__ as bi
except:
    import builtins as bi


class LinkedInSalesGrabber(PageGrabber):  # LinkedIN.com sales scraper for email lookups
    def get_info(self,email):  # Requires AUTH, login and request AUTHENTICATED pages from linkedin
        client = requests.Session()  # Establish the session()
        print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "LinkedIn" + bc.CEND)
        HOMEPAGE_URL = 'https://www.linkedin.com'  # Set homepage for linkedin
        LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'  # Set login page for linkedin
        LOGOUT_URL = 'https://www.linkedin.com/m/logout'
        source = client.get(HOMEPAGE_URL).content  # Request source
        soup = self.get_dom(source)  # BS DOM
        csrf = soup.find(id="loginCsrfParam-login")['value']
        #
        # ATTENTION:: YOU MUST POPULATE THE FOLLOWING WITH YOUR REAL CREDENTIALS
        #
        # ATTENTION:: THIS WILL NOT WORK PROPRLY OTHERWISE
        #
        # session_key = email  session_password = your password
        #
        login_information = {
            'session_key':'',
            'session_password':'',
            'loginCsrfParam': csrf,
        }
        if login_information['session_key'] == '':
            if login_information['session_password'] == '':  # If no modifications of default u/p, print error, return
                print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"This module requires authentication to use it properly.\n"+bc.CEND)
                return
        try:
             client.post(LOGIN_URL, data=login_information)
             results = client.get('https://linkedin.com/sales/gmail/profile/viewByEmail/'+str(email)).text
        except Exception as failedlinkedinauth:
             print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"This module did not properly authenticate: %s"+bc.CEND) % failedlinkedinauth
        soup = self.get_dom(results)
        self.get_source(LOGOUT_URL)  # Log out of LinkedIn, kills sessionID
        try:  # Search and set from results
            profile = soup.find('a',attrs={'class': 'li-hover-under li-txt-black-85'})['href']
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Profile: "+bc.CEND+ str(profile))
        except:
            print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No LinkedIn account found.\n"+bc.CEND)
            return
        try:
            fname = soup.find('span',attrs={'id': 'li-profile-name'})['data-fname']
            lname = soup.find('span',attrs={'id': 'li-profile-name'})['data-lname']
            name = str(fname) + " " + str(lname)
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Name: "+bc.CEND+ str(fname)+" "+str(lname))
        except:
            name = ""
            pass # print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No username can be found.\n"+bc.CEND)
        try:
            company = soup.find('span',{'class': 'li-user-title-company'}).get_text()
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Company: "+bc.CEND+ str(company))
        except:
            company = ""
            pass # print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No Company can be found.\n"+bc.CEND)
        try:
            title = soup.find('div',{'class':'li-user-title'}).get_text()
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Title: "+bc.CEND+ str(title))
        except:
            title = ""
            pass #print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No Job Title can be found.\n"+bc.CEND)
        try:
            location = soup.find('div', {'class':'li-user-location'}).get_text()
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Location: "+bc.CEND+ str(location))
        except:
            location = ""
            pass #print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No Location can be found.\n"+bc.CEND)
        try:
            email = soup.find('span', {'id':'email'}).get_text()
            print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Email: "+bc.CEND+ str(email))
        except:
            email =""
            pass #print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"No Email account found.\n"+bc.CEND)
        self.info_dict.update({
            "profile": profile,
            "name": name,
            "location": location,
            "company": company,
            "title":title,
            "email":email
        })
        bi.outdata['linkedin'] = self.info_dict
        print
        return
