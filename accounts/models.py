from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    ADMIN='admin'
    USER = 'user'


    ROLES=(
        (ADMIN,"Admin"),
        (USER,"user")
    )
    role = models.CharField(max_length=20, choices=ROLES, default=USER)


    def __str__(self):
        return self.username
