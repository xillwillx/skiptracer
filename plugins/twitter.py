from plugins.base import PageGrabber
from colors import BodyColors as bc
try:
    import __builtin__ as bi
except:
    import builtins as bi
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options


class TwitterGrabber(PageGrabber):
 def get_info(self, screenname):
  print screenname
  print("["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "Twitter" + bc.CEND)
  options = Options()
  print "Set options"
  try:
   options.add_argument('--headless')
   b=Firefox(executable_path='/usr/bin/geckodriver',firefox_options=options)
   wait = WebDriverWait(b, timeout=5)
   b.get('https://twitter.com/{}'.format(screenname))
  except Exception as e:
   print e
  print "Sent request"
  try:
   h = b.page_source
   soup = bs(h,'lxml')
  except Exception as e:
   print e
  print "got soup"
  validname = str(soup.h1).split()[-2].split('/')[1].split('"')[0]
  avatar=str(soup.findAll('img', {'class','avatar','js-action-profile-avatar'})[3]['src'])
  profnav = soup.find_all('span',{'class','ProfileNav-value'})
  try:
   if len(profnav) >= 5:
    datal = list()
    print "making list"
    for x in profnav[0:len(profnav)-1:]:
     datal.append(" ".join(str(x).replace("\n"," ").split()).split('"')[3])
  except:
   print "Failed to get profnav"
  print datal
  tcount,fgcount, fscount, likes = datal[:4]
  page = int(tcount) / 20 + 1
  print tcount
  print page
  print fgcount
  print fscount
  print likes
  try:
   for i in range(1,page):
    b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
  except Exception as e:
   print e
  try:
   h = b.page_source
   soup = bs(h,'html')
  except Exception as e:
   print e
  print "Get 2nd helping"
  datelist = list()
  timelist = list()
  for d in soup.findAll('li', {'class','js-stream-item'}):
   print "  [+]", "-" *80
   if 'Retweeted' in d.p.text:
    print(" ["+bc.CGRN+"!"+bc.CEND+"] "+bc.CRED+"Retweet: "+bc.CEND)
    pass
   if str(d.span).split()[3] == 'Icon--pinned':
    print(" ["+bc.CGRN+"!"+bc.CEND+"] "+bc.CRED+"Pinned: "+bc.CEND)
    pass
   try:
    tlist = d.findAll('a')
    dt = tlist[1]['title']
   except Exception as e:
    #print "tlist Fail: %s" % e
    #print tlist
    dt = tlist[2]['title']
    pass
   datelist.append(dt)
   print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Date/Time: "+bc.CEND+ str(dt))
   try:
    timestamp = str(tlist[1]).split()[-3].split('"')[1]
   except Exception as e:
    timestamp = str(tlist[2]).split()[-3].split('"')[1]
    pass
   timelist.append(timestamp)
   print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Timestamp: "+bc.CEND+str(timestamp))
   try:
    posttitle = str(d.p.a['title'])
    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Title: "+bc.CEND+str(posttitle))
   except Exception as e:
    pass
   try:
    postdata = d.p.text
    print("  ["+bc.CGRN+"+"+bc.CEND+"] "+bc.CRED+"Content: "+bc.CEND + postdata)
   except Exception as e:
    print "Post data failed: %s" % e
    pass
