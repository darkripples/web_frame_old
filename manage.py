#!/usr/bin/env python
import os
import sys

ROOT = os.path.abspath( os.path.join( os.path.split( __file__ )[0] , '..' ) )
sys.path.append( ROOT )

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dr_blog.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
