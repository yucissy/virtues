#!/usr/bin/python

"""The base command. Superclass for all commands."""

import os

import sys

import shelve

class Base(object):
    """A base command"""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs


    def get_response(self, prompt, options):
    	""" Prints a prompt and record the response
    	"""

    	# yes/no prompt answer options
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


    def load_virtue_list(self, mode):
    	""" Loads the virtue list from virtues/data/virtue_list.json
    		Returns the file
    	"""
    	path = os.path.join(os.path.dirname(__file__), os.pardir) + '/data/virtue_list.json'
    	file = open(path, mode)
    	return file


    def load_virtue_log(self):
    	""" Loads the virtue list from virtues/data/virtue_log
    		Returns the file
    	"""
    	path = os.path.join(os.path.dirname(__file__), os.pardir) + '/data/virtue_log'
    	file = shelve.open(path, writeback=True)
    	return file

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')
