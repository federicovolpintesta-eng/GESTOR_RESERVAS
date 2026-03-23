import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='federico').exists():
    User.objects.create_superuser('federico', 'federicovolpintesta@gmail.com', '1234')
    print("Superusuario creado en Render: federico / 1234")
else:
    print("El admin ya existe en la nube.")