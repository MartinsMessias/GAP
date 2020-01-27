import os
from django.core.management.utils import get_random_secret_key


try:
    print(os.environ['KEY'])
except KeyError:
    KEY = get_random_secret_key()
    os.environ['KEY'] = KEY
