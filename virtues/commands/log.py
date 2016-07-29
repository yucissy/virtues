#!/usr/bin/python

from .base import Base

import collections

import json


class Log(Base):
    """Prompts user for current day's virtue results and stores results in json."""

    def run(self):
    	file = load_virtue_list('r')
    	virtue_list = json.load(file, object_pairs_hook=collections.OrderedDict)

    	while True:


    	