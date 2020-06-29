from .colors.default_colors import DefaultBodyColors as bc


class Banner():
    """
    Display the SkipTracer banner
    using the BodyColors lib
    to set text color.
    """

    def banner(self):
        """
        Print the banner
        out to the screen
        """
        print("")
        print("\t\t.▄▄ · ▄ •▄ ▪   ▄▄▄·▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄▄▄ .▄▄▄  ")
        print("\t\t▐█ ▀. █▌▄▌▪██ ▐█ ▄█•██  ▀▄ █·▐█ ▀█ ▐█ ▌▪▀▄.▀·▀▄ █·")
        print("\t\t▄▀▀▀█▄▐▀▀▄·▐█· ██▀· ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▪▄▐▀▀▄ ")
        print("\t\t▐█▄▪▐█▐█.█▌▐█▌▐█▪·• ▐█▌·▐█•█▌▐█ ▪▐▌▐███▌▐█▄▄▌▐█•█▌")
        print(
            ("\t\t       {},.-~*´¨¯¨`*·~-.¸{}-({}by{})-{},.-~*´¨¯¨`*·~-.¸{} \n").format(
                bc.CRED,
                bc.CYLW,
                bc.CCYN,
                bc.CYLW,
                bc.CRED,
                bc.CEND))
        print(
            ("\t\t\t      {}▀ █ █ █▀▄▀█ {}█▀▀█ {}█▀▀▄ {}").format(
                bc.CBLU,
                bc.CRED,
                bc.CBLU,
                bc.CEND))
        print(
            ("\t\t\t      {}█ █ █ █ ▀ █ {}█  █ {}█▀▀▄{}").format(
                bc.CBLU,
                bc.CRED,
                bc.CBLU,
                bc.CEND))
        print(
            ("\t\t\t      {}▀ ▀ ▀ ▀   ▀ {}▀▀▀▀ {}▀▀▀ {}").format(
                bc.CBLU,
                bc.CRED,
                bc.CBLU,
                bc.CEND))
        print(("\t\t\t      {}  https://illmob.org {}\n").format(bc.CYLW, bc.CEND))
