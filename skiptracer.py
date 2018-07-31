# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
from plugins.menus import menus
from plugins.colors import BodyColors as bc

import sys
import signal
import json
import plugins.proxygrabber as pg
import ast
try:
    import __builtin__ as bi
except:
    import builtins as bi

class SkipTracer:

    bi.search_string = ''
    bi.lookup = ''
    bi.outdata = dict()
    bi.webproxy = ""
    bi.proxy = ""
    bi.debug = False

    def signal_handler(self, signal, frame):
        """
        Signal handler method
        """
        print("")
        sys.exit(0)

    def banner(self):
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

    def writeout(self):
        """
        Display output text
        """
        try:
            pg.write_file(json.dumps(bi.outdata), bi.filename)
            print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+" Output written to disk: ./%s\n"+bc.CEND) % bi.filename)
        except Exception as nowriteJSON:
            if bi.debug:
                print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND) % nowriteJSON)
            else:
                print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND)

    def __init__(self):
        """
        Start by displaying the banner
        """
        self.banner()
        signal.signal(signal.SIGINT, self.signal_handler)
        try:
            bi.webproxy = raw_input("[Do we wish to enable proxy support? (Y/n)]: ")
            bi.output = raw_input("[Do we wish to save returned data to disk? (Y/n)]: ")
            if str(bi.output).lower() == "y":
                bi.filename = raw_input("[Please provide the filename for output? (somefile.txt|somefile.json)]: ")

            menus().intromenu()
            try:
               self.writout()
            except:
               pass
        except:
            pass


if __name__ == "__main__":  # If true, run main function of framework
    skiptracer = SkipTracer()
