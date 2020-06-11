from cowrie.core.plugins import BasePlugin
from thefuck.shells import shell
from thefuck.output_readers import get_output
from thefuck.types import Command
from thefuck.corrector import get_corrected_commands


class MisspellDetectorPlugin(BasePlugin):
    def get_input(self, event) -> str:
        return event

    def process_event(self, event):
        _input = self.get_input(event)
        exp = shell.from_shell(_input)
        output = get_output(_input, exp)
        cmd = Command(exp, output)
        corrected_cmds = [x.script for x in get_corrected_commands(cmd)]
        if corrected_cmds:
            self.logger.msg(eventid='cowrie.command.misspell', input=_input, corrected_commands=corrected_cmds,
                            format='Misspelled command: %(input)s | Found corrections: %(corrected_commands)s')
