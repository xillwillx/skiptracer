## Skiptracer - OSINT scraping framework
![python](https://img.shields.io/badge/python-3.6-green.svg) ![version](https://img.shields.io/badge/version-3.0.0-brightgreen.svg) ![licence](https://img.shields.io/badge/license-GPLv3-lightgrey.svg)

![screen](https://i.imgur.com/gG0KZ0F.png)

Initial attack vectors for recon usually involve utilizing pay-for-data/API (Recon-NG), or paying to utilize transforms (Maltego) to get data mining results. Skiptracer utilizes some basic python webscraping (BeautifulSoup) of PII paywall sites to compile passive information on a target on a ramen noodle budget.


Background:
-----------
The following recording from DEFCON 26 Recon Village provides background on Skiptracer

[![defconreconvillageyoutube](https://www.youtube.com/watch?v=3mEOkwrxfsU)](https://www.youtube.com/watch?v=3mEOkwrxfsU)


Installation
----
```
$ git clone https://github.com/xillwillx/skiptracer.git skiptracer
```
__Install requirements__
```
$ pip3 install -e skiptracer
```
__Run__
```
$ python3 -m skiptracer
```

Usage
----
Full details on how to use Skiptracer are on the wiki located [here](https://github.com/xillwillx/skiptracer/wiki)


### Extending and configuring Skiptracer

The following section describes how to configure and extend
Skiptracer's functionality using plugins and .cfg files.

Plugins
-------

Skiptracer uses a plugin architecture.

Plugins are added to the following dir:

```
src/skiptracer/plugins/
```

Plugins should be added in a folder under here with their plugin name and
should contain a __main__.py and __init__.py

Once added, to register them, please add them to the setup.py under the
skiptracer.plugins section under entry_points.

For example:

```
'skiptracer.plugins': [
    'myplugin = skiptracer.plugins.myplugin:MyNewSiteGrabber',
    ...
    ]
```


Plugin Menu Configuration
-------------------------
The menus in Skiptracer are configurable and handled by the setup.cfg file
located in the package/source code.

When adding a new plugin, you will need to update the setup.cfg to config
which menus the plugin will be displayed under. A plugin can appear under 1:n
menus.

For example if your plugin supports both email and phone based scraping features
then it can be added to both menus.

To do this, simply edit the setup.cfg and add the plugin name, title and description to
the menu you wish it to appear under, for example:

```
[menu.email]
myplugin = ["My Plugin","Check if user exposes information through some site"]
```

If your plugin requires parameters, please add these to the setup.cfg too. For
example:

```
[plugin.myplugin]
homepageurl = https://www.example.com
loginurl = https://www.example.com/uas/login-submit
logouturl = https://www.example.com/m/logout
viewbyemail = https://example.com/sales/gmail/profile/viewByEmail/
sessionkey = ""
sessionpassword = ""
```
