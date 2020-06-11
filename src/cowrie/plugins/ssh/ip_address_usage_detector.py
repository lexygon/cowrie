from cowrie.core.plugins import BasePlugin
import re


class IPAddressUsageDetectorPlugin(BasePlugin):
    IP_ADDDRESS_REGEX = r'(?:^|\b(?<!\.))(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])'

    def get_input(self, event):
        return event

    def process_event(self, event):
        _input = self.get_input(event)
        ip_addresses = re.findall(self.IP_ADDDRESS_REGEX, _input)
        if ip_addresses:
            self.logger.msg(eventid='cowrie.command.ip_address_entered', input=_input, ip_addresses=ip_addresses,
                            format='IP addresses detected on input "%(input)s". Addresses: %(ip_addresses)')
