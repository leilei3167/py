"""
WSGI config for student_sys project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 默认开发环境
profile = os.environ.get("profile", "develop")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_sys.settings.%s" % profile)

application = get_wsgi_application()
