# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
import click
# [Experimental]
from plugins.twitter import TwitterGrabber
# [Experimental]
from plugins.fouroneone_info import FourOneOneGrabber
from plugins.who_call_id import WhoCallIdGrabber
from plugins.advance_background_checks import AdvanceBackgroundGrabber
from plugins.myspace import MySpaceGrabber
from plugins.whoismind import WhoisMindGrabber
from plugins.linkedin import LinkedInSalesGrabber
from plugins.true_people import TruePeopleGrabber
from plugins.truthfinder import TruthFinderGrabber
from plugins.haveibeenpwned import HaveIBeenPwwnedGrabber
from plugins.hackedemails import HackedEmailGrabber
from plugins.namechk2 import NameChkGrabber
from plugins.plate import VinGrabber
from plugins.knowem import KnowemGrabber
from plugins.tinder import TinderGrabber
import plugins.proxygrabber as pg
try:
    import __builtin__ as bi
except:
    import builtins as bi
import ast
from plugins.colors import BodyColors as bc
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

@click.command()  # Gets arguments supplied at CLI STDIN
@click.option('--lookup', '-l', prompt=True,type=click.Choice(['email', 'phone', 'name', 'sn', 'plate']), help='Lookup type to perform:\n\t[\'email\',\'phone\',\'name\',\'sn\',\'plate\']')
@click.option('--search_string', '-s', prompt=True, help='Search string for lookup type:\n\t[\'user@domain.tld\',\'123-456-7890\',\'bill gates\',\'hacker1\']')
@click.option('--output', '-o', default='', help='Output results to given filename')
@click.option('--webproxy', '-p' ,default=False, is_flag=True, help='Enable web proxied request, edit proxy.txt')
@click.option("--debug", "-d", default=False, is_flag=True, help="enables debugging feature")

def main(lookup, search_string, output, webproxy,debug):
    """Main logic of the application, interfacing with supplied user arguments"""
    banner()  # Display app banner function
    try:
        if debug:
            bi.debug = debug
        if webproxy:
            bi.webproxy = webproxy  # Test to see if web proxy argument was supplied, set builtin with value
    except:
        pass
    if bi.webproxy:  # If true, call proxygrabber.new_proxy(), set new proxy address to bi.proxy, else set to ""
        print ("\t  ["+bc.CRED+"::ATTENTION::"+bc.CEND+"]"+bc.CYLW+" Proxied requests are unreliable "+bc.CEND+"["+bc.CRED+"::ATTENTION::"+bc.CEND+"]")
        bi.proxy = pg.new_proxy()
    if lookup == "phone":  # If true, run phone modules
        try:
            print()
            TruePeopleGrabber().get_info(lookup,search_string)
            WhoCallIdGrabber().get_info(search_string)
            FourOneOneGrabber().get_info(search_string)
            AdvanceBackgroundGrabber().get_info(lookup,search_string)
        except Exception as phonefail:
            if bi.debug: print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Phone lookups failed %s\n"+bc.CEND) % phonefail)
            else:
                print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Phone lookups failed\n"+bc.CEND)

    if lookup == "email":  # If true, run email modules
        try:
            print()
            HackedEmailGrabber().get_info(search_string)
            LinkedInSalesGrabber().get_info(search_string)
            MySpaceGrabber().get_info(search_string)
            HaveIBeenPwwnedGrabber().get_info(search_string)
            WhoisMindGrabber().get_info(search_string)
            AdvanceBackgroundGrabber().get_info(lookup,search_string)
        except Exception as emailfail:
            if bi.debug: print ("Test")  # print(("  ["+bc.CRED+"DEBUG"+bc.CEND+"] "+bc.CYLW+"Email lookups failed %s\n"+bc.CEND) % emailfail)
            else:
                print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Email lookups failed\n"+bc.CEND)

    if lookup == "name":  # If true, run name modules
        try:
            print()
            TruthFinderGrabber().get_info(lookup,search_string)
            TruePeopleGrabber().get_info(lookup,search_string)
            AdvanceBackgroundGrabber().get_info(lookup,search_string)
        except Exception as namefail:
            if bi.debug: print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Name lookups failed %s\n"+bc.CEND) % namefail)
            else:
                print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Name lookups failed %s\n"+bc.CEND)

    if lookup == "sn":  # If true, run screename modules
        print()
        try:
            TwitterGrabber().get_info(search_string)
            KnowemGrabber().get_info(search_string)
            NameChkGrabber().get_info(search_string)
            TinderGrabber().get_info(search_string)
        except Exception as snfail:
            if bi.debug: print(("  ["+bc.CRED+"DEBUG"+bc.CEND+"] "+bc.CYLW+"Screenname lookups failed %s\n"+bc.CEND) % snfail)
            else:
                print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Screenname lookups failed\n"+bc.CEND)
    if lookup == "plate":  # If true, run plate modules
        try:
            print()
            VinGrabber().get_info(search_string)
        except Exception as platefail:
            if bi.debug: print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Plate lookups failed %s\n"+bc.CEND) % platefail)
            else:
                print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Plate lookups failed %s\n"+bc.CEND)
    else:  # Still in the works
        "Still working on rest"
    if output:  # If true, import JSON, dump data, write bi.outdata to given file name -o FILENAME
        import json
        try:
            pg.write_file(json.dumps(bi.outdata), output)
            print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+" Output written to disk: ./%s\n"+bc.CEND) % output)
        except Exception as nowriteJSON:
            print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND) % nowriteJSON)
            if bi.debug: print(("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND) % nowriteJSON)
            else:
                print("  ["+bc.CRED+"X"+bc.CEND+"] "+bc.CYLW+"Output failed to write to disk %s\n"+bc.CEND)
if __name__ == "__main__":  # If true, run main function of framework
    main()

