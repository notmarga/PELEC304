from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username
