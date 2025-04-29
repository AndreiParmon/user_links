from django.db import models


class Link(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(unique=True)
    image = models.URLField(blank=True, null=True)
    link_type = models.CharField(
        max_length=50,
        choices=[
            ('website', 'Website'),
            ('book', 'Book'),
            ('article', 'Article'),
            ('music', 'Music'),
            ('video', 'Video'),
        ],
        default='website',
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'links'

    def __str__(self):
        return self.title
