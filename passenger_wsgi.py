import sys
import os

# Full path to your project root
project_root = '/home/gdcplati/drink_software'

# Add project paths to sys.path
sys.path.insert(0, project_root)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'drink_software.settings'

# Start the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
