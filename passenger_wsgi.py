import os, sys
import site

IMAGR_ENV_DIR = '/home/docker/imagr'

# Use site to load the site-packages directory of our virtualenv
site.addsitedir(os.path.join(IMAGR_ENV_DIR, 'lib/python2.7/site-packages'))

# Make sure we have the virtualenv and the Django app itself added to our path
sys.path.append(IMAGR_ENV_DIR)
sys.path.append(os.path.join(IMAGR_ENV_DIR, 'sal'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imagr_server.settings")
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
