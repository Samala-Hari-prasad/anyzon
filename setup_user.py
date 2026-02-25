import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'F10.settings')
django.setup()

from django.contrib.auth.models import User

username = 'hari'
password = 'prasad'

user, created = User.objects.get_or_create(username=username)
user.set_password(password)
user.is_staff = True
user.is_superuser = True
user.save()

if created:
    print(f"User {username} created successfully.")
else:
    print(f"User {username} password updated successfully.")
