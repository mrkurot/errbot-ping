from errbot import BotPlugin, botcmd
from errbot.builtins.webserver import webhook


class SVSL(BotPlugin):

    """A PingSVSL function for Err"""
    min_err_version = '1.6.0'  # Optional, but recommended
    #max_err_version = '2.0.0'  # Optional, but recommended

    @botcmd(split_args_with=None)
    def svsl(self, mess, args):

        return "cephei_kells: ephecina: grumps_mcgee: Hibbie: lakz: lakz-work: rina_kondur: shock_fist: sp33dyk3: Spring HeeledJack: dante_lobos: shutupandshave: Koshka narkotikov: tuxedo_catfish:"
