virtues
=========

A python command-line app to track your daily virtues. Inspired by `Ben Franklin <http://www.artofmanliness.com/2008/06/01/the-virtuous-life-wrap-up/>`_.

Install
-----

After cloning the project to a directory or downloading the .zip file, run these commands in that directory to install the library (*and all
development dependencies*):

    $ python setup.py build && python setup.py install
    
    $ pip install -e .
    
Getting Started
-----
    
Create a list of virtues you'd like to track with the command:

    $ virtues init
    
You will be prompted to enter a list of virtues and their descriptions (optional). If you're unsure where to start, use the [--franklin] option to default your list to Benjamin Franklin's `13 virtues <http://www.thirteenvirtues.com/>`_.

    $ virtues init --franklin

To see your list of virtues:
    
    $ virtues list
    
Logging
-----

The program allows you to log and track your virtues. Add a new entry to your virtues log with the following command. The verbose [-v] option will print each virtue's long description:

    $ virtues log [-v]
    
To clear your log:
    
    $ virtues clear

Status Report
-----

Running this command will show you a status report for all your virtue log entries so far:

    $ virtues status
