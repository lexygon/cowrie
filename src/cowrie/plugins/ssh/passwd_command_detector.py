from cowrie.core.plugins import BasePlugin
from cowrie.plugins.ssh.utils import get_command_name_from_path


class PasswdCommandDetectorPlugin(BasePlugin):
    def get_input(self, event):
        return event

    def process_event(self, event):
        _input = self.get_input(event)
        splitted_input = _input.split()
        splitted_input.append(get_command_name_from_path(_input))
        if 'passwd' in splitted_input:
            self.logger.msg(eventid='cowrie.command.passwd_command_entered', input=_input,
                            format='"passwd" command detected on input "%(input)s".')
