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
    
Create a list of virtues you'd like to track with the command

    $ virtues init
    
You will be prompted to enter a list of virtues and their descriptions (optional). If you're unsure where to start, running this command will default your list to Benjamin Franklin's `13 virtues <http://www.thirteenvirtues.com/>`_.

    $ virtues init --franklin

To see your list of virtues
    
    $ virtues show
