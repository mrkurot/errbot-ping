from errbot import BotPlugin, botcmd
from errbot.builtins.webserver import webhook


class Ping(BotPlugin):

    """A Ping Group function for Err"""
    min_err_version = '1.6.0'  # Optional, but recommended
    #max_err_version = '3.0.0'  # Optional, but recommended

    def activate(self):
        super(Xup, self).activate()

        if not hasattr(self, 'groups'):
            self['groups'] = {}

    @botcmd(split_args_with="||")
    def ping_set(self, mess, args):
        """Create/Update a group."""
        
        group_str = args[0]
        group_tuple = group_str.split(" ", 1)
        
        if len(group_tuple) > 1:
            group, text = group_tuple
            group = group.lower()
            
            old_value = self.groups.get(group)
            self.groups[group] = text
            if old_value:
                return "Updated group '%', previous value was: %s" % (group, old_value,)
            else:
                return "Created group '%s'." % (group,)
        else:
            group = group_tuple[0]
            group = group.lower()
            if group in self.groups:
                del self.groups[group]
                return "Deleted group %s" % group
        
        
        
        
    @botcmd(split_args_with=None)
    def ping(self, mess, args):
        """Ping a specified group"""
        
        group = args[0]
        group = group.lower()
        
        group_text = self.groups.get(group, None)
        
        if group_text != None:
            return group_text
        else:
            return "No such group, valid groups are: %s" % (", ".join(sorted(self.groups.keys())),)
            
    @botcmd(split_args_with=None)
    def ping_groups(self, mess, args):
        """Show the groups that can be pinged"""
        
        groups = self.groups.keys()
        
        return ", ".join(sorted(groups))
