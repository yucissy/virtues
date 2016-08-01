virtues
=========

A python command-line app to track your daily virtues. Inspired by `Ben Franklin <http://www.artofmanliness.com/2008/06/01/the-virtuous-life-wrap-up/>`_.

Usage
-----

After cloning the project, run these commands to install the library (*and all
development dependencies*):

    $ python setup.py build && python setup.py install
    
    $ pip install -e .
    
First things first: Create a list of virtues you'd like to track for yourself. Run the command

    $ virtues init
    
You will be prompted to enter a list of virtues and their descriptions (optional). If you're unsure where to start, running this command will let you use Benjamin Franklin's `13 virtues <http://www.thirteenvirtues.com/>`_.

    $ virtues init --franklin
