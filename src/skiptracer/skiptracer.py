# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
#from .plugins.menus import menus
#from .plugins.colors import BodyColors as bc
import pkg_resources
import sys
import signal
import json
#import plugins.proxygrabber as pg
import ast

try:
    import __builtin__ as bi
except BaseException:
    import builtins as bi


class SkipTracer:
    """
    Kick off the SkipTracer
    program
    """
    bi.search_string = ''
    bi.output = ''
    bi.lookup = ''
    bi.outdata = dict()
    bi.webproxy = ""
    bi.proxy = ""
    bi.debug = False

    inc_plugins = {}
    plugins_plugin = "skiptracer.plugins"
    menus_plugin = "skiptracer.menus"
    colors_plugin = "skiptracer.colors"
    loaded_plugins_plugin_dict = {}
    loaded_menus_plugin_dict = {}
    loaded_colors_plugin_dict = {}

    def __init__(self, plugins):
        #signal.signal(signal.SIGINT, self.signal_handler)
        self.inc_plugins = plugins
        self.loaded_plugins_plugin_dict = self.load_plugins(
            self.plugins_plugin)
        self.loaded_menus_plugin_dict = self.load_plugins(
            self.menus_plugin)
        self.loaded_colors_plugin_dict = self.load_plugins(
            self.colors_plugin)


        self.loaded_menus_plugin_dict[0].intromenu()
        #bi.webproxy = input("[Do we wish to enable proxy support? (Y/n)]: ")
        #bi.output = input(
        #    "[Do we wish to save returned data to disk? (Y/n)]: ")
        #if str(bi.output).lower() == "y":
        #    bi.filename = input(
        #        "[Please provide the filename for output? (somefile.txt|somefile.json)]: ")

        #menus().intromenu()
        #self.writeout()


    def load_plugins(self, plugin):
        """
        Load the plugin and store
        object in an array
        """
        plugin_dict = {}

        for p in pkg_resources.iter_entry_points(plugin):
                plugin_dict[p.name] = p.load()
        return plugin_dict



    def signal_handler(self, signal, frame):
        """
        Signal handler method
        """
        print("")
        sys.exit(0)


    def writeout(self):
        """
        Display output text
        """
        try:
            pg.write_file(json.dumps(bi.outdata), bi.filename)
            print(("  [" + bc.CRED + "X" + bc.CEND + "] " + bc.CYLW +
                   " Output written to disk: ./%s\n" + bc.CEND) % bi.filename)
        except Exception as nowriteJSON:
            if bi.debug:
                print(("  [" +
                       bc.CRED +
                       "X" +
                       bc.CEND +
                       "] " +
                       bc.CYLW +
                       "Output failed to write to disk %s\n" +
                       bc.CEND) %
                      nowriteJSON)
            else:
                print("  [" + bc.CRED + "X" + bc.CEND + "] " + bc.CYLW +
                      "Output failed to write to disk %s\n" + bc.CEND)
