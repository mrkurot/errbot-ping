from errbot import BotPlugin, botcmd
from errbot.builtins.webserver import webhook


class Ping(BotPlugin):

    """A Ping Group function for Err"""
    min_err_version = '1.6.0'  # Optional, but recommended
    #max_err_version = '3.0.0'  # Optional, but recommended

    groups = {}

    @botcmd(split_args_with="||")
    def ping_set(self, mess, args):

        group_str = args[0]
        group_tuple = group_str.split(" ", 1)
        
        if len(group_tuple) > 1:
            group, text = group_tuple
            text = group_tuple(
        else:
            del self.groups[group]
            
        self.groups[group] = text

        return "Updated group."
        
        
    @botcmd(split_args_with=None)
    def ping(self, mess, args):
        
        group = args[0]
        
        group_text = self.groups.get(group, None)
        
        if group_text != None:
            return group_text
        else:
            return "No such group"
