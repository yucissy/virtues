#!/usr/bin/python

"""The init command. Creates a list of virtues."""


from json import dumps

from .base import Base

import sys

import json

import os


class Init(Base):
    """Set up the virtue tracker by prompting the user for virtues to track"""
    """Defualt to Franklin's 13 virtues"""

    def get_response(self, prompt, options):
    	""" Print the prompt and record the response
    	"""
    	valid = {"y": True, "n": False}

    	while True:
    		sys.stdout.write(prompt)
    		choice = raw_input().lower()
    		if options == True and choice not in valid:
    			sys.stdout.write("Please respond with 'y' or 'n'.\n")
    		elif options == True:
    			return valid[choice]
    		else:
    			return choice

    def write_data(self, data, name):
    	""" Write the contents of the dict to a json file saved in 
    		virtues/data
    	"""
    	path = os.path.join(os.path.dirname(__file__), os.pardir)
    	path += '/data/virtue_list.json'
    	file = open(path, 'w+')
    	dataObj = {name: data}
    	json.dump(dataObj, file)


    def run(self):
    	""" Re-initialize the user's virtue list
    	"""
    	count = 1
    	virtues = {}

        print 'Welcome to virtue tracker!'
        print 'Creating your personalized list of virtues... ([ENTER] to end)'

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
        			for v in virtues:
        				print "%s\t%s" % (v, virtues[v])
        			self.write_data(virtues, 'virtues')
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

