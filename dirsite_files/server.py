'''
DIRSITE CGI server script.
'''

import os
from configparser import ConfigParser

DIRSITE_INI = ConfigParser()
DIRSITE_INI.read('dirsite_files/configuration.ini')

FIRST_PAGE = DIRSITE_INI.get('appearance', 'FIRST_PAGE')
README_FILENAME = 'dirsite_files' + os.sep + 'readme.html'

###############################################################################


def create_read_me_file(port_number):
    '''Create the readme file for the server session using configuration
    values extracted from configuration files.'''

    import io

    command_line = 'http://localhost:' + str(port_number) + '/dirsite.py?cl='

    dirsite_ini_object = io.StringIO()
    DIRSITE_INI.write(dirsite_ini_object)

    views_ini_object = io.StringIO()
    views_ini = ConfigParser()
    views_ini.read('dirsite_files/views.ini')
    views_ini.write(views_ini_object)

    plain_dir = command_line + 'dir && more ' + README_FILENAME
    coded_dir = command_line + 'dir%20%26%26%20more%20' + README_FILENAME

    with open('dirsite_files/template_readme.html', 'rt') as readme_file:
        readme_html = readme_file.read()

    readme_html = readme_html.format(
        cwd=os.getcwd(),
        readme_cgi=command_line + 'more ' + README_FILENAME,
        dir_readme_cgi=plain_dir,
        encoded_dir_readme_cgi=coded_dir,
        command_line=command_line,
        views_ini='<pre>' + views_ini_object.getvalue() + '</pre>',
        dirsite_ini='<pre>' + dirsite_ini_object.getvalue() + '</pre>')

    with open(README_FILENAME, 'w') as readme_file:
        readme_file.write(readme_html)

###############################################################################


def start(port_number):
    '''Start server running at port_number.  If configuration file value
    FIRST_PAGE is an actual file then the server will automatically serve that
    page, otherwise, the server will sleep for a second and then serve the
    page assumed to be a CGI script.'''

    from http.server import HTTPServer, CGIHTTPRequestHandler
    import cgitb
    import subprocess
    import webbrowser

    create_read_me_file(port_number)

    ###########################################################################
    # Browse to FIRST_PAGE.  Unscalable past 1 due to likely port # collision.
    ###########################################################################

    if os.path.isfile(FIRST_PAGE):
        webbrowser.open('file://' + os.path.realpath(FIRST_PAGE))
    else:
        # Delayed browse of page served by this script
        webcommand = 'sleep 1 && python -m webbrowser "http://localhost:'
        webcommand += str(port_number) + '/' + FIRST_PAGE + '"'
        proc = subprocess.Popen(webcommand, shell=True)
        print('Delayed browse command pid =', str(proc.pid))

    cgi_handler = CGIHTTPRequestHandler
    cgi_handler.cgi_directories = ['/']

    cgitb.enable()

    # TODO: detect/prevent reuse of port_number in case of 2 dirsites...
    httpd = HTTPServer(("", port_number), cgi_handler)
    print("Serving at port", port_number)
    httpd.serve_forever()

###############################################################################
