#!/usr/bin/python3

'''
Handles empty command lines sent to dirsite.  Generally serves as a means of
viewing the full view of command lines generated in accordance with the
configuration file.
'''

import datetime
import fnmatch
import io
import itertools
import os
import time
from pathlib import PurePath
from urllib import parse
from configparser import ConfigParser
from configparser import NoOptionError

###############################################################################
# Acquire constants from server configuration file
###############################################################################

SERVER_CFG = ConfigParser(strict=True)
SERVER_CFG.read('dirsite_files/configuration.ini')

PORT = SERVER_CFG.get('server', 'port')
RELOAD_TIME = SERVER_CFG.getint('appearance', 'reload_time')
NAVIGATE_BY_POST = SERVER_CFG.getboolean('appearance', 'navigate_by_post')

###############################################################################
# CGI script configuration file (+ persistent cfg variable)
###############################################################################

VIEWS_CFG = ConfigParser(strict=True)
VIEWS_CFG.read('dirsite_files/views.ini')
VIEWS_INI_FILE_OBJECT = io.StringIO()
VIEWS_CFG.write(VIEWS_INI_FILE_OBJECT)

TEMPLATE_SELECTION = VIEWS_CFG.get('template', 'selection')
HEAT_HOURS = VIEWS_CFG.getint('appearance', 'heat_hours')

TEST_DIRECTORY = VIEWS_CFG.get('content_paths', 'test_directory')
SAMPLE_DIRECTORY = VIEWS_CFG.get('content_paths', 'sample_directory')

FILE_FILTERS = str(VIEWS_CFG.get(TEMPLATE_SELECTION, 'filter')).split()
FILES_BANNED = str(VIEWS_CFG.get(TEMPLATE_SELECTION, 'banned')).split()
IGNORE_FILES = str(VIEWS_CFG.get(TEMPLATE_SELECTION, 'ignore_files')).split()
IGNORE_DIRS = str(VIEWS_CFG.get(TEMPLATE_SELECTION, 'ignore_dirs')).split()

###############################################################################
# Remaining constants
###############################################################################

META_REFRESH = '<META HTTP-EQUIV="refresh" CONTENT="' + str(RELOAD_TIME) + '">'
if NAVIGATE_BY_POST:
    META_REFRESH = ''

CGI_SITE = 'http://localhost:' + PORT + '/dirsite.py'
USAGE_NOTES_TITLE = 'Python Package CLI Tips (With or without DIRSITE)'
CWD = os.getcwd()

FILES_IN_PLAY = set()
for root, dirs, files in os.walk('.'):
    ignore_dir = False
    for igdir in IGNORE_DIRS:
        if igdir in dirs:
            ignore_dir = True
            dirs.remove(igdir)
    if not ignore_dir:
        for f in files:
            ignore_file = f in FILES_BANNED
            for igfile in IGNORE_FILES:
                if fnmatch.fnmatch(f, igfile):
                    ignore_file = True
                    break
            if not ignore_file:
                FILES_IN_PLAY.add(os.path.join(root, f)[2:])

###############################################################################


def cssfile(filename):
    '''Kludge to use a .css file from CGI session.'''
    result = '<style>'
    with open(filename, 'r') as file_of_css:
        result += file_of_css.read()
    return result + '</style>'

###############################################################################


def cgi_anchor(command):
    '''Create HTML anchor/input for the command.'''
    if NAVIGATE_BY_POST:
        result = '<input type="button" value = "' + command + \
                 '" onclick="commandSend({\'cl\':\'' + command + '\'})">'
    else:
        encoded = '?' + parse.urlencode({'cl': command}, quote_via=parse.quote)
        result = '<a href="' + CGI_SITE + encoded + '">' + command + '</a>'
    return result

###############################################################################


def create_color(seconds):
    '''Colors generated in an ad-hoc heat map scheme from red (Hot) to blue
    (Cold).'''
    hex_upper = '0123456789ABCDEF'

    hours = seconds // 3600
    if hours >= HEAT_HOURS:
        blue_value = 255
    else:
        blue_value = 255 * hours // HEAT_HOURS
    red_value = 255 - blue_value

    result = '#'
    result += hex_upper[red_value // 16] + hex_upper[red_value % 16]
    result += '22'    # green_value
    result += hex_upper[blue_value // 16] + hex_upper[blue_value % 16]

    return result

###############################################################################


def dir_html():
    '''Invoke table creation for non-banned directories.'''
    spanning = ''
    for row in itertools.count(1):
        try:
            key = 'dir_content_' + str(row)
            command = str(VIEWS_CFG.get(TEMPLATE_SELECTION, key))
        except NoOptionError:
            break
        key = 'dir_header_' + str(row)
        spanning += '<tr>'
        spanning += '  <th>' + VIEWS_CFG.get(TEMPLATE_SELECTION, key) + '</th>'
        command = command.format(dirtest=TEST_DIRECTORY)
        spanning += '  <td class="greentd">' + cgi_anchor(command) + '</td>'
        spanning += '</tr>'

    result = '''
            <table>
                <tr>
                    <th>Current working directory</th>
                    <td class="greentd">{cwd}</td>
                </tr>
                {full_span_commands}
            </table>
            <br>
    '''.format(cwd=CWD, full_span_commands=spanning)

    banned = [TEST_DIRECTORY, SAMPLE_DIRECTORY, 'dirsite_files']
    first_table = True
    for entry in os.scandir():
        if entry.is_dir() and entry.name not in banned:
            if first_table:
                first_table = False
            else:
                result += '<br>'
            result += files_html(entry.name)
    return result

###############################################################################


def files_html(dir_name):
    '''Create HTML table for options populated by file discovery.'''

    filtered = []
    none_banned = [f for f in os.listdir(dir_name) if f not in FILES_BANNED]
    for filt in FILE_FILTERS:
        for filename in none_banned:
            if fnmatch.fnmatch(filename, filt):
                filtered += [filename]

    result = ''
    for filename in sorted(filtered):
        result += '<tr>'
        filebase = PurePath(filename).stem
        filepath = os.path.join(dir_name, filename)
        testpath = os.path.join(TEST_DIRECTORY, 'test_' + filename)
        sample_path = os.path.join(SAMPLE_DIRECTORY, filebase + '.txt')

        FILES_IN_PLAY.remove(filepath)
        if os.path.isfile(testpath):
            FILES_IN_PLAY.remove(testpath)
        if os.path.isfile(sample_path):
            FILES_IN_PLAY.remove(sample_path)

        difftime = int(time.time() - os.stat(filepath).st_mtime)
        result += '<td style="text-align:right;font-size:0.9em;\
                       background-color:%s;white-space:nowrap;">' % \
                       create_color(difftime)
        result += '<b>%s</b>' % datetime.timedelta(seconds=difftime)
        result += '</td>'

        for column in itertools.count(1):
            try:
                key = 'file_dependency_' + str(column)
                dependency = str(VIEWS_CFG.get(TEMPLATE_SELECTION, key))
            except NoOptionError:
                break
            dependency = dependency.format(filename=filename,
                                           filepath=filepath,
                                           testpath=testpath,
                                           dirname=dir_name,
                                           sample_path=sample_path,
                                           filebase=filebase,
                                           dirtest=TEST_DIRECTORY).strip()

            if dependency != '' and not os.path.isfile(dependency):
                result += '<td class="missing"><b>Unmet Dependency:<b> ' + str(dependency) + '</td>'
            else:
                key = 'file_content_' + str(column)
                command_html = str(VIEWS_CFG.get(TEMPLATE_SELECTION, key))
                command_html = command_html.format(filename=filename,
                                                   filepath=filepath,
                                                   testpath=testpath,
                                                   dirname=dir_name,
                                                   sample_path=sample_path,
                                                   filebase=filebase,
                                                   dirtest=TEST_DIRECTORY)
                result += '<td>' + cgi_anchor(command_html) + '</td>'
        result += '</tr>'

    # Render table only when table rows have been created.
    if result:
        result = '<table>' + table_top(dir_name) + result + '</table>'

    return result

###############################################################################


def table_top(dir_name):
    '''Create HTML for table headers.'''
    top_row = '''
    <tr>
        <th colspan=100% class="greentitle">/{directory}</th>
    </tr>
    '''.format(directory=dir_name)

    file_heads = '<th style="white-space:nowrap;">Last Modified</th>'
    for column in itertools.count(1):
        try:
            header = VIEWS_CFG.get(TEMPLATE_SELECTION, \
                                   'file_header_' + str(column))
        except NoOptionError:
            break
        file_heads += '<th>' + header + '</th>'

    return top_row + '<tr>' + file_heads + '</tr>'

###############################################################################


def information_sections():
    '''Create HTML for optional portions of web page.'''
    html_results = []

    if VIEWS_CFG.getboolean('appearance', 'show_unlinked_files') and \
            len(FILES_IN_PLAY):
        unlinked_rows = ''
        for unlinked in FILES_IN_PLAY:
            unlinked_rows += '<tr><td style="border:0px"><code>{}\
                              </code></td></tr>'.format(unlinked)
        unlinked_html = '<center><table>'+ unlinked_rows + '</table></center>'
        html_results.append('''<center><h3>Files Not (Yet) Linked</h3></center>
        {unlinked_html}
        '''.format(unlinked_html=unlinked_html))

    if VIEWS_CFG.getboolean('appearance', 'show_url_encoder'):
        html_results.append('''
        <hr>
        <center><h3>General Usage URL Encoder</h3></center>
        <p>To run an arbitrary python command, modify the url to send a valid
        python invocation to the dirsite_cl.py page.  For
        assistance in creating encoded URLs, click the
        <b>URL Encode</b> button to URL encode the contents of the text box.
        Example: <code>python -m timeit -s "list(set('CLI&CGI'))"</code>.
        Note: major bug currently exists with parsing strings containing
        whitespace.  Presuming everything went well, the encoded result may be
        copied and pasted into the browser URL (I have not made this an
        automatic link because it is not tested, only demonstrated).</p>
        <input id="inputString" onfocus="javascript:clearTextField
        'encodedInputString');" onblur="javascript:clearTextField();"
        type="text" size="50">
        <button onclick="urlEncodeButton()">URL Encode</button>
        <br><br>
        <b>Encoded URL =</b>  <code>{cgi_url}<div id="encodedString"
        style="display:inline;"></div></code>
        '''.format(cgi_url=CGI_SITE + '?cl='))
        # TODO: find out if onfocus above should have a right paren

    if VIEWS_CFG.getboolean('appearance', 'show_configuration_file'):
        html_results.append('''
        <hr>
        <center><h3>
            Configuration File <code>dirsite_files/views.ini</code>
        </h3></center>
        <div style="color:#00F;">{views_ini}</div>
        Some configuration changes to consider:
        <ul>
            <li>To remove a column, delete its information from
                <code>views.ini</code> and be sure to renumber the
                other columns and decrement the <code>columns</code>
                variable.</li>
            <li>To configure heat map extent for 1 week range, change
                <b>heat_hours</b> to 168</li>
            <li>To add a column:
                <ul>
                    <li>Add the column header in a
                        <code>file_header_#</code> field.</li>
                    <li>Add the command to be executed in the
                        <code>file_content_#</code> field.  Available
                        parameters are:
                        <ul>
                            <li>{{dirname}}</li>
                            <li>{{dirtest}}</li>
                            <li>{{filepath}}</li>
                            <li>{{modulename}}</li>
                            <li>{{sample_path}}</li>
                            <li>{{testpath}}</li>
                        </ul>
                    </li>
                    <li>Add command dependency files in
                        <code>file_dependency_#</code>.  If none, the
                        attribute value must still appear in the configuration
                        file with an empty right hand side value.</li>
                    <li>Increment the <code>columns</code> value in the
                        configuration file.</li>
                </ul>
            </li>
        </ul>
        '''.format(views_ini='<pre>' +
                   VIEWS_INI_FILE_OBJECT.getvalue() + '</pre>'))

    if VIEWS_CFG.getboolean('appearance', 'show_coverage_setup'):
        html_results.append('''
        <hr>
        <center><h3><u>coverage</u> setup</h3></center>
        <p><code>coverage</code> is an external dependency available for
           installation by pip.  The prefab coverage links provided by
           DIRSITE rely upon links from the 'test' directory to the source
           directories and must be manually created by the user.  Note: no
           adult supervision was consulted in the making of this decision, or
           any other DIRSITE decision really.</p>
        <ul><u>Coverage Link Creation</u>
            <li>Windows
                <ul>
                    <li>Navigate to project's <b>test</b> directory.</li>
                    <li>Begin python session with <b>Administrator</b>
                        privileges.</li>
                    <li>Perform command <code>>>> import os</code></li>
                    <li>Perform command <code>>>> os.symlink('../module_name',
                        'module_name', target_is_directory=True)</code></li>
                    <li>End python session</li>
                </ul>
            </li>
            <li>Linux - TBD
            </li>
        </ul>
        ''')

    return ''.join(html_results)

###############################################################################

print('Content-type: text/html\n')  # CGI requirement

with open('dirsite_files/template_views.html', 'rt') as f:
    CL_HTML = f.read()

print(CL_HTML.format(
    cwd=CWD,
    basename=os.path.basename(CWD),
    meta_refresh=META_REFRESH,
    directory_tables=dir_html(),
    css=cssfile('dirsite_files/dirsite.css'),
    usage_notes_title=USAGE_NOTES_TITLE,
    sample_input=SAMPLE_DIRECTORY,
    test_dir=TEST_DIRECTORY,
    information_section=information_sections()))

###############################################################################
