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
