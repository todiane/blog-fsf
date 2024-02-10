"""
WSGI config for todianedev project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todianedev.settings')

# Get the Django application
application = get_wsgi_application()

# Wrap the Django application with Whitenoise
application = WhiteNoise(application)

# Set the root directory for collecting static files
application.add_files(os.path.join(os.path.dirname(__file__), "todianedev/static"))

