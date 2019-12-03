from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class QueryModel(models.Model):

	location = models.CharField(max_length=150, verbose_name='Konum Bilgisi')
	venue = models.CharField(max_length=150, verbose_name='Mekan Türü')
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	limit = models.CharField(max_length=40, verbose_name='Listelenecek Limit.')

	def __str__(self):
		return '%s  %s %s' % (self.location, self.venue, self.limit)


