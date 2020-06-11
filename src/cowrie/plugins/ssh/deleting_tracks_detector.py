from cowrie.core.plugins import BasePlugin
from cowrie.plugins.ssh.utils import get_command_name_from_path


class DeletingTracksDetectorPlugin(BasePlugin):
    risky_directories = [
        '/var/log',
        'bash_history'
    ]

    def get_input(self, event):
        return event

    def process_event(self, event, *args, **kwargs):
        deleted_directories = []
        _input = self.get_input(event)
        splitted_input = _input.split()
        splitted_input.append(get_command_name_from_path(_input))

        if self.deletion_exists(splitted_input):
            for directory in self.risky_directories:
                if directory in _input:
                    deleted_directories.append(directory)

        if deleted_directories:
            self.logger.msg(eventid='cowrie.command.deleting_track', input=_input, found_list=deleted_directories,
                            format='Found deleting track commands in command "%(input)s": %(found_directories)s')

    def deletion_exists(self, splitted_input):
        if 'rm' in splitted_input:
            return True

        return False
