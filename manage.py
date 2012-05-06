#!/usr/bin/env python

# platform specific library loading
import sys
import platform
if platform.uname()[1] == 'dude.local':
    sys.path.append('/Users/michael/code/songbird-django/code/libraries/lib/python/')

# do not change anything below here mhg
# ////////////////////////////////////////////////////

from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

if __name__ == "__main__":
    execute_manager(settings)
