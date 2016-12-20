"""
WSGI config for wsudorauth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/opt/wsudorauth')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wsudorauth.settings")

application = get_wsgi_application()
