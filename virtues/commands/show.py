#!/usr/bin/python

from .base import Base

import collections

import json

import os


class Show(Base):
    """Print the user's virtue list to stdout"""

    def run(self):
        file = self.load_virtue_list('r')
        virtue_list = json.load(file, object_pairs_hook=collections.OrderedDict)
        
        # align the columns properly
        template = "{0:15}{1}"

        for virtue in virtue_list:
            print template.format(virtue.upper(), virtue_list[virtue])
    	