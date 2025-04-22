#!/usr/bin/env python3
"""
Helper script to ensure correct Python path when running Django
"""

import os
import sys
import subprocess

# Add the parent directory to sys.path
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, parent_dir)

# Run Django's runserver command
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gamerevs.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions.
        try:
            import django
        except ImportError:
            raise ImportError("Couldn't import Django. Are you sure it's installed?")
        raise
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
