#!/usr/bin/env python
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

### GENERIC_SETUP_MARKER_START ###
__program_file__        = 'your_program.py'
__program_name__        = '%s' % __program_file__.split('.py')[0]
__scripts__             = []
__data_files__          = []
__version__             = '0.1.0'
__date__                = '2011/03/14'
__author_name__         = 'Rogério Carvalho Schneider'
__author_email__        = 'stockrt@gmail.com'
__author__              = '%s <%s>' % (__author_name__, __author_email__)
__maintainer_name__     = __author_name__
__maintainer_email__    = __author_email__
__maintainer__          = '%s <%s>' % (__maintainer_name__, __maintainer_email__)
__copyright__           = 'Copyright (C) 2011 %s' % __author_name__
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
Python utilities.
''' % __program_file__
__rpm_data__            = '''
%files
%defattr(-,root,root,-)
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
    easy_install ...
- pip:
    pip install ...
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
