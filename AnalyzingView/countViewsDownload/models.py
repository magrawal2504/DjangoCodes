from django.db import models
import django


# Create your models here.
class Hit(models.Model):

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    action = models.CharField(max_length=2, choices=ACTIONS)


class Publication(models.Model):
    title = models.CharField(max_length=200)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    user = models.ForeignKey('UserAgent', on_delete=models.CASCADE)


class Journal(models.Model):
    headline = models.CharField(max_length=200)


class UserAgent(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
