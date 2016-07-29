#!/usr/bin/python

from .base import Base

import collections

import json

import shelve

class Status(Base):
    """Prints a status report from the virtues log (virtues/data/virtue_log.db)."""

    def run(self):

    	# open the virtue log db with shelve
    	file = self.load_virtue_list('r')
    	virtue_list = json.load(file, object_pairs_hook=collections.OrderedDict)
    	log = self.load_virtue_log()

    	for virtue in log:
            print virtue
            print log[virtue]

    	log.close()



    	