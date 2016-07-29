#!/usr/bin/python

from .base import Base

import collections

import json

import shelve

class Log(Base):
    """Prompts user for current day's virtue results and stores results in json."""

    def run(self):

    	# open the virtue log db with shelve
    	file = self.load_virtue_list('r')
    	virtue_list = json.load(file, object_pairs_hook=collections.OrderedDict)
    	log = self.load_virtue_log()

    	print 'Think back on your day...'
    	print 'Did you display the following virtues?'

    	# record the response (yes/no) for each virtue
    	for virtue in virtue_list:
    		result = self.get_response(virtue.title()+'[y/n] ', True)
    		if not log.has_key(virtue):
    			log[virtue] = []

    		if result == True:
    			log[virtue].append(1)
    		else:
    			log[virtue].append(0)

    	log.close()
    	print 'Day is recorded. Run \'virtues status\' to see your overall stats.'




    	