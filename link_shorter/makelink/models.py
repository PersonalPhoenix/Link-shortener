from django.db import models


class Link(models.Model):

    url = models.CharField(max_length = 10000, null = False)
    uuid = models.CharField(max_length = 6,
                            unique = True,
                            null = False)