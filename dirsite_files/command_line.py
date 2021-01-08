#!/usr/bin/python3

'''
DIRSITE Command Line handler.
'''

import cgi
import datetime
import os
import platform
import subprocess
from urllib import parse
from configparser import ConfigParser

DIRSITE_INI = ConfigParser()
DIRSITE_INI.read('dirsite_files/configuration.ini')

NAVIGATE_BY_POST = DIRSITE_INI.getboolean('appearance', 'navigate_by_post')

CWD = os.getcwd()

results = []
legends = []
invoked_module = ''

###############################################################################


def cssfile(filename):
    '''Kludge to use a .css file from CGI session.'''
    result = '<style>'
    with open(filename, 'r') as file_of_css:
        result += file_of_css.read()
    return result + '</style>'

###############################################################################


def cl_window_title():
    ''''Module'arize window title.'''

    if invoked_module == 'unittest':
        if 'FAILED' in results[-1]:
            title_string = 'FAILED'
            number_failed = results[0].count('AssertionError')
            if number_failed:
                title_string += ' ' + str(number_failed)
        elif 'Ran 0 tests' in results[-1]:
            title_string = 'MISSING tests'
        else:
            title_string = 'PASSED ALL'
    elif invoked_module:
        title_string = invoked_module
    else:
        title_string = "DIRSITE"
    return title_string

###############################################################################


def command_results(commands, outputs):
    '''Create html rows of commands and output.'''

    result_html = ''
    count_commands = (len(commands) > 1)
    counted = 0
    for leg, res in zip(commands, outputs):
        command = ''
        if count_commands:
            counted += 1
            command += '<th style="white-space:nowrap;">Command ' + \
                str(counted) + '</th>'
            output = '<th>Output ' + str(counted) + '</th>'
        else:
            command += '<th>Command</th>'
            output = '<th>Output</th>'
        command += '<td class="greentd" style="color:#28D">' + leg + '</td>'

        output += '<td class="greentd">'
        output += '    <pre><table class="greentext">'
        for outline in res.splitlines(True):
            if outline == '\n':
                spaced = '<br>'
            else:
                spaced = ''
                for glyph in outline:
                    if glyph == ' ':
                        spaced += '&nbsp;'
                    else:
                        spaced += glyph
            output += '<tr><td style="padding:0px;">' + spaced + '</td></tr>'
        output += '    </table></pre>'
        output += '</td>'

        result_html += '<tr>' + command + '</tr><tr>' + output + '</tr>'

    return result_html

###############################################################################

CLI_INPUT = cgi.FieldStorage().getvalue('cl')

if CLI_INPUT:
    META_REFRESH = '<META HTTP-EQUIV="refresh" CONTENT="{}">'.format(
        DIRSITE_INI.get('appearance', 'reload_time'))
    CLI_PLATFORM = '{} ({} {})'.format(
        platform.node(),
        platform.system(),
        platform.version())

    SCRIPT = parse.unquote(CLI_INPUT)
    COMMANDS = SCRIPT.split('&&')

    for cmd in COMMANDS:
        parts = cmd.split()
        invoked_module = ''
        if '-m' in parts:
            i = parts.index('-m') + 1
            if i < len(parts):
                invoked_module = parts[i]  # window title assignment
        if invoked_module == '':
            invoked_module = parts[0]

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        # TODO: test having a subprocess timed exit here...
        (out, err) = proc.communicate()
        # TODO: decode windows extended ascii output for 'tree' command
        results.append(str(out, 'utf-8') + str(err, 'utf-8'))
        encoded = []
        for r in results:
            line = r.replace('<', '&lt;')  # Prevent '<DIR>' parsing as HTML
            line = line.replace('>', '&gt;')
            line = line.replace('\r', ' ')  # Is there another way?
            encoded.append(line)
        results = encoded
        legends.append(cmd)
        # TODO: Stop looping after error is reported from command execution

    with open('dirsite_files/template_cl.html', 'rt') as f:
        TABULATED_HTML = f.read()
    print('Content-type: text/html; charset=utf-8\n')  # CGI requirement
    print(TABULATED_HTML.format(
        cwd=CWD,
        meta_refresh=META_REFRESH,
        user_login=os.getlogin(),
        user_platform=CLI_PLATFORM,
        css=cssfile('dirsite_files/dirsite.css'),
        window_title=cl_window_title(),
        output=command_results(legends, results),
        date_time=datetime.datetime.today().ctime()))
else:
    # TODO: list templates from views.ini and allow choice from here?
    from dirsite_files import views

###############################################################################
