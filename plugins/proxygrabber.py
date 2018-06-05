from __future__ import print_function
from __future__ import absolute_import
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
import os, random, time, random
from .colors import BodyColors as bc
try:
    import __builtin__ as bi
except:
    import builtins as bi

#props to scrapehero for proxy cycler
storage_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, 'storage'))
output_file = "%s%sproxies.txt"% (storage_dir,os.sep)

def remove_proxy(fn,remline):  # Removes a bad proxy from proxies.txt
    f = open(fn,"r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != str(remline):
            f.write(i)
    f.truncate()
    f.close()

def write_file(d, fn):  # used to write out files to disk
    t = open(fn, "a")
    t.write(d)
    t.close()
    t = None

def get_proxies():  # Initial request to generate proxy list
    print("\n["+bc.CPRP+"?"+bc.CEND+"] "+bc.CCYN + "Proxy List Generator" + bc.CEND)
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[::]:
        if i.xpath('.//td[5][contains(text(),"elite proxy")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Testing proxies, please wait till complete..."+bc.CEND)
    return proxies

def new_proxy():  # Select random proxy form list, if no list, generate a new one and test them for connectivity (living)
    cwd = os.getcwd()
    try:
        now = time.time()
        if os.stat(str(cwd)+'/storage/proxies.txt').st_mtime < now - 7 * 86000:
            os.remove(str(cwd)+'/storage/proxies.txt')
        with open(str(cwd)+'/storage/proxies.txt','r') as proxies:
            bi.proxy = str(random.choice(proxies.readlines())).strip()
            proxy = bi.proxy
        print ("\t  ["+bc.CRED+"::ATTENTION::"+bc.CEND+"]"+bc.CYLW+" Proxy: "+bi.proxy+bc.CEND+" ["+bc.CRED+"::ATTENTION::"+bc.CEND+"]")
        return proxy
    except Exception as noproxyfile:  # Start generating the proxy list
        proxies = get_proxies()  # Call to grab results, returns a list
        proxy_pool = cycle(proxies)  # Shuffle list
        url = 'https://api.ipify.org?format=json'
        for i in range(1,11):  # Choose random 10 proxies and test from pool
            proxy = random.choice(list(proxies))
            for xproto in ['http','https']:
                try:
                    print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Testing %s proxy: %s"+bc.CEND) % (str(xproto).strip(),str(proxy).strip()))
                    response = requests.get(url,proxies={xproto : proxy}, timeout=2)
                    if response:
                        write_file(str(xproto)+"://"+str(proxy) + "\n", output_file)
                except:
                    pass
        print ("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Finished testing proxies, continue.\n"+bc.CEND)
        bi.proxy = new_proxy()
    return bi.proxy
