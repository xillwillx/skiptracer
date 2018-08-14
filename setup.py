from setuptools import setup, find_packages
from setuptools.command.install import install
import io

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.md')

setup(
    name='skiptracer',
    version='3.0.0',
    description='OSINT python webscaping framework',
    long_description=long_description,
    maintainer='xillwillx',
    license='Apache 2.0',
    url='https://github.com/xillwillx/skiptracer',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    entry_points={
        'console_script': [
            'skiptracer = skiptracer.__main__:main'
        ],
        'skiptracer.plugins': [
            'fouroneone_info = skiptracer.plugins.fouroneone_info:FourOneOneGrabber',
            'haveibeenpwned = skiptracer.plugins.haveibeenpwned:HaveIBeenPwwnedGrabber',
            'knowem = skiptracer.plugins.knowem:KnowemGrabber',
            'linkedin = skiptracer.plugins.linkedin:LinkedInSalesGrabber',
            'myspace = skiptracer.plugins.myspace:MySpaceGrabber',
            'namechk2 = skiptracer.plugins.namechk2:NameChkGrabber',
            'plate = skiptracer.plugins.plate:VinGrabber',
            'tinder = skiptracer.plugins.tinder:TinderGrabber',
            'true_people = skiptracer.plugins.true_people:TruePeopleGrabber',
            'truthfinder = skiptracer.plugins.truthfinder:TruthFinderGrabber',
            'twitter = skiptracer.plugins.twitter:TwitterGrabber',
            'who_call_id = skiptracer.plugins.who_call_id:WhoCallIdGrabber',
            'whoismind = skiptracer.plugins.whoismind:WhoisMindGrabber'
        ],
        'skiptracer.menus': [
            'default_menus = skiptracer.menus.default_menus:DefaultMenus'
        ],
        'skiptracer.colors': [
            'default_colors = skiptracer.colors.default_colors:DefaultBodyColors'
        ]
    },
    install_requires=[
        'bs4',
        'lxml',
        'requests',
        'ipdb',
        'pprint',
        'click',
        'cfscrape',
        'numpy',
        'simplejson',
        'tqdm',
        'selenium'
    ]
)
