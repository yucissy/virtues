#!/usr/bin/python

"""
virtues
Usage:
  virtues init [--franklin]
  virtues list
  virtues log [--verbose | -v]
  virtues status
  virtues clear
  virtues -h | --help
  virtues --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
Examples:
  virtues init                  Create your own virtues list.
  virtues init --franklin       Create a virtues list using Benjamin Franklin's 13 virtues.
  virtues list                  See virtues list.
  virtues status                See your status report.
  virtues log                   Log your daily performance.
  virtues clear                 Clear your log.
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/yucissy/virtues
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():

    """Main CLI entrypoint"""
    import commands
    options = docopt(__doc__, version=VERSION)

    # Dynamically match the command the user is trying to run
    # with a pre-defined command class
    for k, v in options.iteritems():
        if hasattr(commands, k) and v:
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()