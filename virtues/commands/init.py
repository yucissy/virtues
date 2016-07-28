#!/usr/bin/python

"""The init command."""


from json import dumps

from .base import Base


class Init(Base):
    """Set up the virtue tracker by prompting the user for virtues to track"""
    """Defualt to Franklin's 13 virtues"""

    def run(self):
        print 'Hello, world!'
        print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
