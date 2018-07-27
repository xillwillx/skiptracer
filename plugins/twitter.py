#
# Twitter Scraper: Requires users to install additional non standard libraries
#
from plugins.base import PageGrabber
from colors import BodyColors as bc
try:
    import __builtin__ as bi
except:
    import builtins as bi
import time
try:
 from bs4 import BeautifulSoup as bs
except Exception as e:
 print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Failed at importing BeautifulSoup from bs4: {}\n"+bc.CEND).format(e)
try:
 from selenium.webdriver import Firefox
 from selenium.webdriver.common.by import By
 from selenium.webdriver.common.keys import Keys
 from selenium.webdriver.support.ui import Select
 from selenium.webdriver.support.ui import WebDriverWait
 from selenium.webdriver.firefox.options import Options
except Exception as e:
 print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Failed at importing selenium requirements: {}\n"+bc.CEND).format(e)
try:
 from tqdm import tqdm
except Exception as e:
 print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Failed at importing tqdm from tdqm: {}\n"+bc.CEND).format(e)
import os

class TwitterGrabber(PageGrabber):
 def get_info(self, screenname):
  print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "Twitter" + bc.CEND)
  print(" ["+bc.CGRN+"!"+bc.CEND+"] "+bc.CRED+"Module takes some time to load, please wait!"+bc.CEND)
  options = Options()
  try:
   options.add_argument('--headless')
   b=Firefox(executable_path='/usr/bin/geckodriver',firefox_options=options)
   wait = WebDriverWait(b, timeout=5)
   b.get('https://twitter.com/{}'.format(screenname))
  except Exception as e:
   print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Failed at making the initial request: {}\n"+bc.CEND).format(e)
  try:
   soup = bs(b.page_source,'lxml')
  except Exception as e:
   print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Unable to make initial soup: {}\n"+bc.CEND).format(e)
  validname = str(soup.h1).split()[-2].split('/')[1].split('"')[0]
  avatar = str(soup.findAll('img', {'class','avatar','js-action-profile-avatar'})[3]['src'])
  profnav = soup.find_all('span',{'class','ProfileNav-value'})
  try:
   if len(profnav) >= 5:
    datal = list()
    for x in profnav[0:len(profnav)-1:]:
     datal.append(" ".join(str(x).replace("\n"," ").split()).split('"')[3])
  except Exception as e:
   print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Failed at making the datalist: {}\n"+bc.CEND).format(e)
  tcount,fgcount, fscount, likes = datal[:4]
  page = int(tcount) / 20 + 1
  nap = 1
  estt = page*nap/60
  try:
   scrapeall = raw_input(" [!] Do you want to capture all tweets ?\n [!] Estimated time to complete: "+str(estt)+"m (Y/n) ")
   if scrapeall.lower() in [1,'y','true','on']:
    for i in tqdm(range(1,page)):
     b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     time.sleep(nap)
  except Exception as e:
   print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Failed at scrolling site: {}\n"+bc.CEND).format(e)
  try:
   h = b.page_source
   soup = bs(h,'lxml')
  except Exception as e:
   print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Can not make soup, phase 2: {}\n"+bc.CEND).format(e)
  datelist = list()
  timelist = list()
  for d in soup.findAll('li', {'class','js-stream-item'}):
   print "\n  [+]", "-" *80
   if 'Retweeted' in d.p.text:
    print(" ["+bc.CGRN+"!"+bc.CEND+"] "+bc.CRED+"Retweet: "+bc.CEND)
   if str(d.span).split()[3] == 'Icon--pinned':
    print(" ["+bc.CGRN+"!"+bc.CEND+"] "+bc.CRED+"Pinned: "+bc.CEND)
   try:
    tlist = d.findAll('a')
    dt = tlist[1]['title']
   except Exception as e:
    try:
     dt = tlist[2]['title']
    except Exception as e:
     print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Unable to find datetime: {}\n"+bc.CEND).format(e)
     pass
   datelist.append(dt)
   print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Date/Time: "+bc.CEND+ str(dt))
   try:
    timestamp = str(tlist[1]).split()[-3].split('"')[1]
    if len(timestamp) < 10:
     timestamp = str(tlist[2]).split()[-3].split('"')[1]
    if len(timestamp) < 10:
     timestamp = "Conversation Extension"
   except Exception as e:
    print e
    pass
   if timestamp:
    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Timestamp: "+bc.CEND+str(timestamp))
   try:
    posttitle = str(d.p.a['title'])
    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Title: "+bc.CEND+str(posttitle))
   except Exception as e:
    pass
   try:
    postdata = d.p.text
    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Content:\n"+bc.CEND)
    print postdata
   except Exception as e:
    print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Unable to find content: {}\n"+bc.CEND).format(e)
    pass
  try:
   for xproc in os.popen('ps -A xf | grep -v grep | grep "/usr/bin/firefox -marionette --headless -profile /" | cut -d " " -f2'):
    os.popen('kill -9 '+str(xproc))
  except Exception as e:
   print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Unable to kill Firefox headless: {}\n"+bc.CEND).format(e)
