
from django.db import models


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    questions_count = models.IntegerField()

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file_url = models.URLField()

    def __str__(self):
        return self.title