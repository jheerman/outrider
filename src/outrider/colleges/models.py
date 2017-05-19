# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SoftballProgram(models.Model):
	object_id = models.CharField(max_length=50, unique=True)
	school = models.CharField(max_length=50)
	nickname = models.CharField(max_length=50)
	state = models.CharField(max_length=25)
	field = models.CharField(max_length=50)
	head_coach = models.CharField(max_length=50)
	conference = models.CharField(max_length=25)
	work_series_appearances = models.CharField(max_length=20)
	titles = models.CharField(max_length=20)

	def save(self, *args, **kwargs):
		pass

	class Meta:
		managed = False
