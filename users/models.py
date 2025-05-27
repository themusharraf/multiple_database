from django.db import models


class CustomUser(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True)


    def __str__(self):
        return self.full_name

    class Meta:
        app_label = "users"
