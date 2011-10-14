#!/usr/bin/env python
# coding: utf-8

# Copyright (C) 2009-2011 Rogério Carvalho Schneider <stockrt@gmail.com>
#
# This file is part of generic_setup.
#
# generic_setup is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# generic_setup is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with generic_setup.  If not, see <http://www.gnu.org/licenses/>.
#
#
# change_me.py
#
# Created:  Jun 22, 2009
# Author:   Rogério Carvalho Schneider <stockrt@gmail.com>

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

### GENERIC_SETUP_MARKER_START ###
# Readme
import os
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
if os.path.isfile(os.path.join(PROJECT_DIR, 'README.txt')):
    README_FILE =  os.path.join(PROJECT_DIR, 'README.txt')
else:
    README_FILE =  os.path.join(PROJECT_DIR, '../README.txt')

__program_file__        = 'change_me.py'
__program_name__        = '%s' % __program_file__.split('.py')[0]
__scripts__             = []
__data_files__          = []
#__data_files__          = [('/usr/local/%s/conf' % __program_name__, ['%s.conf' % __program_name__]),
#                           ('/usr/local/%s/bin' % __program_name__, [__program_file__]),
#                           ('/usr/local/%s' % __program_name__, ['README.txt']),
#                           ('/var/spool/%s' % __program_name__, []),
#]
#__data_files__          = [('/usr/local/%s/conf' % __program_name__, ['%s/%s.conf' % (__program_name__, __program_name__)]),
#                           ('/usr/local/%s/bin' % __program_name__, ['%s/%s' % (__program_name__, __program_file__)]),
#                           ('/usr/local/%s' % __program_name__, ['README.txt']),
#                           ('/var/spool/%s' % __program_name__, []),
#]
__data_files__          = []
__version__             = '0.1.1'
__date__                = '2011/09/28'
__author_name__         = 'Rogério Carvalho Schneider'
__author_email__        = 'stockrt@gmail.com'
__author__              = '%s <%s>' % (__author_name__, __author_email__)
__maintainer_name__     = __author_name__
__maintainer_email__    = __author_email__
__maintainer__          = '%s <%s>' % (__maintainer_name__, __maintainer_email__)
__copyright__           = 'Copyright (C) 2009-2011 %s' % __author_name__
__license__             = 'GPLv3'
__url__                 = 'http://stockrt.github.com'
__download_url__        = __url__
__py_modules__          = [__program_name__]
__platforms__           = ['any']
__keywords__            = 'python utilities functions'
__classifiers__         = [
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Utilities',
]
__description__         = 'Python utilities.'
__long_description__    = '''%s
%s
''' % (__program_file__, open(README_FILE).read())
__rpm_data__            = '''
%post
echo
echo 'Some message to your users'
echo

%files
%defattr(-,root,root,-)
#%dir /var/spool/%{name}
#%config(noreplace) /usr/local/%{name}/conf/%{name}.conf
#/usr/local/%{name}/bin/%{name}.py
'''
### GENERIC_SETUP_MARKER_END ###

### IMPORTS_START ###
try:
    import translate
    import re
    import os
except ImportError, why:
    print
    print 'Error loading module: [%s]' % why
    print '''
You need to install some extra modules in order to run this program:
- easy_install
    wget http://peak.telecommunity.com/dist/ez_setup.py
    python ez_setup.py
    easy_install (see import error above)
- pip:
    pip install (see import error above)
'''
    sys.exit(1)
### IMPORTS_END ###

### DEFINES_START ###
### DEFINES_END ###

##########
## MAIN ##
##########
def main():
    print '''
Sample program.
    '''

if __name__ == '__main__':
    main()
