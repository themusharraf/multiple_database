from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=225)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        app_label = "books"
