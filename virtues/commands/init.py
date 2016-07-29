#!/usr/bin/python


from json import dumps

from .base import Base

from collections import OrderedDict

import sys

import json

import os


class Init(Base):
    """Set up the virtue tracker by prompting the user for virtues to track"""

    def write_data(self, data):
    	""" Write the contents of the dict to a json file saved in 
    		virtues/data
    	"""
    	file = self.load_virtue_list('w+')
    	json.dump(data, file)


    def run(self):
    	""" Re-initialize the user's virtue list
    	"""

    	# if user chooses franklin's list, copy it from virtues/data/franklin_virtue_list.json
    	if self.options['--franklin'] == True:
    		path = os.path.join(os.path.dirname(__file__), os.pardir) + '/data/franklin_virtue_list.json'

    		with open(path, 'r') as data_file:    
    			data = json.load(data_file, object_pairs_hook=OrderedDict)
    			self.write_data(data)

    		print 'Initialized virtues to franklin\'s 13 virtues.'
    		return

    	count = 1
    	virtues = OrderedDict()

        print 'Welcome to virtue tracker!'
        print 'Creating your own list of virtues... ([ENTER] to end)'

        # loop prompt until user enters blank response
        while True:

        	# create the prompt to initialize a virtue
        	prompt = 'Virtue #'+str(count)
        	if (count == 1):
        		prompt += ' (e.g. Temperance)'
        	prompt += ': '

        	response = self.get_response(prompt, False)

        	# a blank response signals the user is finished
        	if response == '':
        		response = self.get_response('Finished? [y/n] ', True)
        		if response == True:
        			print 'Saved virtues: '
        			template = "{0:15}{1}"
        			for v in virtues:
        				print template.format(v.upper(), virtues[v])
        			self.write_data(virtues)
        			break
        		continue

        	# prompt user for short description of the virtue (can be blank)
        	else:
        		virtue_name = response
        		if virtue_name in virtues:
        			print 'Virtue already exists!'
        			continue
        		virtue_description = self.get_response('Description (optional): ', False)
        		virtues[virtue_name] = virtue_description
        		count += 1

