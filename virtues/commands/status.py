#!/usr/bin/python

from .base import Base

import collections

import json

import shelve

from termcolor import colored

class Status(Base):
    """Prints a status report from the virtues log (virtues/data/virtue_log.db)."""

    def run(self):

    	# open the virtue log db with shelve
    	file = self.load_virtue_list('r')
    	virtue_list = json.load(file, object_pairs_hook=collections.OrderedDict)
    	log = self.load_virtue_log()

        # string template to align columns properly
        template = "{:<15s}{:>10s}  {:<15s}"

        # check for empty logs
        if not log:
            print 'Nothing logged! Run \'virtues log\' to begin logging your performance.'

    	for virtue in log:

            # calculate the % success rate for each virtue (number of 1s recorded over total days)
            # format the score as percentage rounded to whole number
            record = log[virtue]

            success_rate = (float(record.count(1)) / float(len(record)))

            # get percent score (1-100)
            percent = "{:.0%}".format(success_rate)

            # get rate rounded down to nearest digit from 0-10
            score = int(success_rate * 10)

            # print a basic visual : a line of pluses and minuses
            visual = ''

            # green pluses denote the score
            for i in range(0, score):
                visual += colored('+', 'green', None)

            # fill up the rest of the 10 spaces with red minuses
            for j in range(score, 10):
                visual += colored('-', 'red', None)
            

            print template.format(virtue.upper(), percent, visual)

    	log.close()



    	