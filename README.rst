virtues
=========

A python command-line app to track your daily virtues. Inspired by `Ben Franklin <http://www.artofmanliness.com/2008/06/01/the-virtuous-life-wrap-up/>`_.

Install
-----

After cloning the project to a directory, run these commands in that directory to install the library (*and all
development dependencies*):

    $ python setup.py build && python setup.py install
    
    $ pip install -e .
    
Getting Started
-----
    
Create a list of virtues you'd like to track with the command:

    $ virtues init
    
You will be prompted to enter a list of virtues and their descriptions (optional). If you're unsure where to start, running with the [--franklin] option will default your list to Benjamin Franklin's `13 virtues <http://www.thirteenvirtues.com/>`_.

    $ virtues init --franklin

To see your list of virtues:
    
    $ virtues list
    
Logging
-----

At the end of each day, log your performance with the following command. The verbose [-v] option will prompt you with each virtue's long description:

    $ virtues log [-v]

Status Report
-----

Running this command will show you a status report for all your days so far:

    $ virtues status
