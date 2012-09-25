import os
import sys

sys.stdout = sys.stderr

from site import addsitedir
addsitedir('/home/jbrooks/envs/toprank/lib/python2.7/site-packages')

from os.path import abspath, dirname, join
from django.conf import settings

sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
