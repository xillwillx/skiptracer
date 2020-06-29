try:
    import __builtin__ as bi
except BaseException:
    import builtins as bi


class DataSaver()

 bi.outdata = dict()
  bi.output = ''

   def __init__():
        bi.webproxy = input("[Do we wish to enable proxy support? (Y/n)]: ")
        bi.output = input(
            "[Do we wish to save returned data to disk? (Y/n)]: ")
        if str(bi.output).lower() == "y":
            bi.filename = input(
                "[Please provide the filename for output? (somefile.txt|somefile.json)]: ")
        self.writeout()

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
