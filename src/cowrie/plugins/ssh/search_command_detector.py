from cowrie.core.plugins import BasePlugin
from cowrie.plugins.ssh.utils import get_command_name_from_path


class SearchCommandDetectorPlugin(BasePlugin):
    command_list = [
        {
            "command": "grep"
        },
        {
            "command": "cat"
        },
        {
            "command": "tail"
        },
        {
            "command": "head"
        }
    ]

    def get_input(self, event):
        return event

    def process_event(self, event, *args, **kwargs):
        found_list = []
        _input = self.get_input(event)
        splitted_input = _input.split()
        splitted_input.append(get_command_name_from_path(_input))
        for input_part in splitted_input:
            if input_part in map(lambda x: x['command'], self.command_list):
                found_list.append(input_part)

        if found_list:
            self.logger.msg(eventid='cowrie.command.search_command', input=_input, found_list=found_list,
                            format='Found search commands in command "%(input)s": %(found_list)s')
