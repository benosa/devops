#!/usr/bin/python

import re

from ansible.errors import (
    AnsibleFilterTypeError,
    AnsibleFilterError
)

def format_mac_filter(input_str):
    if not isinstance(input_str, str):
        raise AnsibleFilterTypeError("String type is expected, "
                                     "got type %s instead" % type(input_str))
    if re.match("^([a-fA-F0-9]){12}$", input_str) is None:
        raise AnsibleFilterError("Not valid string, valid string is can include a-fA-F0-9 character")
    
    return ":".join(re.findall(r'[a-fA-F0-9]{2}', str(input_str).lower()))


class FilterModule(object):
    def filters(self):
        return {
            'format_mac_filter': format_mac_filter
        }
