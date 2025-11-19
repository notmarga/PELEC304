"""
ASGI config for PELEC304_FINALS_QUIZZES project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PELEC304_FINALS_QUIZZES.settings')

application = get_asgi_application()
