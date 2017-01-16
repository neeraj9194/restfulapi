from __future__ import unicode_literals

from django.db import models

# Create your models here.

LANGUAGE_CHOICES = (
    ('Eng', 'English'),
    ('Hin', 'Hindi'),
)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)

    def __str__(self):
        return self.title
