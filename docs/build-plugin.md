# How to build a plugin guide


The following document provides a guide to building a plugin.


Skiptracer uses a plugin architecture.

Plugins are added to the following dir:

```
src/skiptracer/plugins/
```

Plugins should be added in a folder under here with their plugin name and
should contain a __main__.py and __init__.py


The following demonstrates the basics of the __init__.py file:

```

from ..base import PageGrabber
from ...colors.default_colors import DefaultBodyColors as bc
from .. import proxygrabber


<include any other imports here>

import builtins as bi


class MyClassGrabber(PageGrabber):
    """ Give your class a name """


    def get_info(self, <pass in params>, category):
        """
        Each class needs this method.
        Pass in any params you need to process
        e.g. email, name etc.
        """

        return

```



Once added, to register your plugin, add it to the setup.py under the
skiptracer.plugins section under entry_points.

For example:

```
'skiptracer.plugins': [
    'myplugin = skiptracer.plugins.myplugin:MyClassGrabber',
    ...
    ]
```


If your plugin requires parameters, please add these to the setup.cfg. For
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

These values can then be set either through the commandline or via the .env file.

## Plugin Menu Configuration

As noted in the main readme, the menus in Skiptracer are configurable and handled by the setup.cfg file
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

It's that simple.

