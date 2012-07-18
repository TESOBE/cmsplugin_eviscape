from cms.models.pluginmodel import CMSPlugin

from django.db import models


class EviscapeInstance(CMSPlugin):
    server = models.CharField(max_length=100, default='api.eviscape.com')
    nod_id = models.PositiveIntegerField()
    evis_type = models.CharField(max_length=20, default='blog', blank=True)
    limit = models.PositiveIntegerField(default=5)
    title = models.CharField(max_length=30, default='Blog', blank=True)
