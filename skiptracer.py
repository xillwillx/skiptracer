# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
import plugins.proxygrabber as pg
from plugins.menus import menus
import sys
import signal
try:
    import __builtin__ as bi
except:
    import builtins as bi
import ast
from plugins.colors import BodyColors as bc
def signal_handler(signal, frame):
 print("")
 sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
bi.search_string = ''
bi.lookup = ''
bi.outdata = dict()
bi.webproxy = ""
bi.proxy = ""
bi.debug = False
def banner():
    print ("")
    print ("\t\t.▄▄ · ▄ •▄ ▪   ▄▄▄·▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄▄▄ .▄▄▄  ")
    print ("\t\t▐█ ▀. █▌▄▌▪██ ▐█ ▄█•██  ▀▄ █·▐█ ▀█ ▐█ ▌▪▀▄.▀·▀▄ █·")
    print ("\t\t▄▀▀▀█▄▐▀▀▄·▐█· ██▀· ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▪▄▐▀▀▄ ")
    print ("\t\t▐█▄▪▐█▐█.█▌▐█▌▐█▪·• ▐█▌·▐█•█▌▐█ ▪▐▌▐███▌▐█▄▄▌▐█•█▌")
    print(("\t\t       {},.-~*´¨¯¨`*·~-.¸{}-({}by{})-{},.-~*´¨¯¨`*·~-.¸{} \n").format(bc.CRED,bc.CYLW,bc.CCYN,bc.CYLW,bc.CRED,bc.CEND))
    print(("\t\t\t      {}▀ █ █ █▀▄▀█ {}█▀▀█ {}█▀▀▄ {}").format(bc.CBLU,bc.CRED,bc.CBLU,bc.CEND))
    print(("\t\t\t      {}█ █ █ █ ▀ █ {}█  █ {}█▀▀▄{}").format(bc.CBLU,bc.CRED,bc.CBLU,bc.CEND))
    print(("\t\t\t      {}▀ ▀ ▀ ▀   ▀ {}▀▀▀▀ {}▀▀▀ {}").format(bc.CBLU,bc.CRED,bc.CBLU,bc.CEND))
    print(("\t\t\t      {}  https://illmob.org {}\n").format(bc.CYLW,bc.CEND))

banner()

def writeout():
 if str(bi.output).lower() == "y":  # If true, import JSON, dump data, write bi.outdata to given file name -o FILENAME
  import json
  try:
   pg.write_file(json.dumps(bi.outdata), bi.filename)
   print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+" Output written to disk: ./%s\n"+bc.CEND) % bi.filename)
  except Exception as nowriteJSON:
   if bi.debug: 
    print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND) % nowriteJSON)
   else:
    print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND)

if __name__ == "__main__":  # If true, run main function of framework
 try:
  bi.webproxy = raw_input("[Do we wish to enable proxy support? (Y/n)]: ")
  bi.output = raw_input("[Do we wish to save returned data to disk? (Y/n)]: ")
  if str(bi.output).lower() == "y":
   bi.filename = raw_input("[Please provide the filename for output? (somefile.txt|somefile.json)]: ")
 except:
   pass
 menus().intromenu()
 writout()

