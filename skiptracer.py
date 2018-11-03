# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
from plugins.menus import menus
from plugins.banner import Logo

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

bi.search_string = None
bi.lookup = None
bi.output = None
bi.outdata = dict()
bi.webproxy = None
bi.proxy = None
bi.debug = False

Logo().banner()


if __name__ == "__main__":  # If true, run main function of framework
 try:
  if str(bi.output).lower() == "y":
   bi.filename = raw_input("[Please provide the filename for output? (somefile.txt|somefile.json)]: ")
   def writeout():
    import json
    try:
     pg.write_file(json.dumps(bi.outdata), bi.filename)
     print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+" Output written to disk: ./%s\n"+bc.CEND) % bi.filename)
    except Exception as nowriteJSON:
     if bi.debug:
      print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND) % nowriteJSON)
     else:
      print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND)
  menus().intromenu()
 except Exception as failedmenu:
  print("Failed menu: %s" % (failedmenu))
  pass
