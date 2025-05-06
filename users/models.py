from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roles = models.CharField(max_length=50, choices=[('admin','адміністратор'),('user', 'користувач')], default='user')

