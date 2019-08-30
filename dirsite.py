#!/usr/bin/python3

'''
DIRSITE top level CGI script.  Forks to create server if not already running.
Current implementation likely does not scale beyond 1 directory.
'''

import os

# Test if server is already running.
if 'REQUEST_METHOD' in os.environ:
    from dirsite_files import command_line
else:
    import argparse
    from configparser import ConfigParser
    from dirsite_files import server

    DIRSITE_INI = ConfigParser()
    DIRSITE_INI.read('dirsite_files/configuration.ini')
    PORT = DIRSITE_INI.getint('server', 'port')

    PARSER = argparse.ArgumentParser(description='Start DIRSITE server.')
    PARSER.add_argument('--port', default=PORT, type=int,
                        help='server on this port')
    ARGS = PARSER.parse_args()

    if ARGS.port != PORT:
        DIRSITE_INI.set('server', 'port', str(ARGS.port))
        with open('dirsite_files/configuration.ini', 'w') as config_file:
            DIRSITE_INI.write(config_file)

    server.start(ARGS.port)
