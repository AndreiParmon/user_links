from django.db import models
from links.models import Link


class Collection(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    links = models.ManyToManyField(Link)

    class Meta:
        app_label = 'users_collections'
