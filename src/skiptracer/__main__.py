from .skiptracer import SkipTracer
from .banner import Banner

def main():
    """
    Start skip tracer
    """
    plugins = plugin_processor('skiptracer.plugins', 'all')
    banner = Banner()
    banner.banner()
    skiptracer = SkipTracer(plugins)


def plugin_processor(cat, plugins):
    """
    Return a list of plugins
    to use
    """
    plugins_to_use = {}
    plugins_to_use[cat] = plugins.split(',')
    return plugins_to_use


if __name__ == "__main__":
    main()
