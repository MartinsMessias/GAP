import os
from django.core.management.utils import get_random_secret_key

KEY = get_random_secret_key()
os.environ['KEY'] = KEY
print(os.environ['KEY'])