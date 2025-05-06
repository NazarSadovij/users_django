import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "users_django.settings")
django.setup()


from users.models import User

user1 = User(name="Богдан", email="bogdan1234@gmail.com")


user1.save()























