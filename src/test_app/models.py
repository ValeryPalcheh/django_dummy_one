from django.db import models

# Create your models here.
# ORM -
# Directory
# name | description

class Directory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
