# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function

import pkg_resources
import sys
import signal
import json
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
    bi.lookup = ''
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
        """
        Load all the different types
        of plugin
        """
        self.inc_plugins = plugins

        self.loaded_plugins_plugin_dict = self.load_plugins(
            self.plugins_plugin)

        self.loaded_menus_plugin_dict = self.load_plugins(
            self.menus_plugin)

        self.loaded_colors_plugin_dict = self.load_plugins(
            self.colors_plugin)

        #only supporting default menu for now
        self.loaded_menus_plugin_dict['default_menus'](self.loaded_plugins_plugin_dict).intromenu()


    def load_plugins(self, plugin):
        """
        Load the plugin and store
        object in an array
        """
        plugin_dict = {}

        for p in pkg_resources.iter_entry_points(plugin):
                plugin_dict[p.name] = p.load()
        return plugin_dict
