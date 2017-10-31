# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Agar(models.Model):
	agar_id = models.IntegerField(primary_key=True)
	media = models.CharField(max_length=100)
	temp = models.CharField(max_length=20)
	ctx = models.BooleanField()
	def __str__(self):
		return str(self.agar_id) + " " + self.media + " " + self.temp + " " + str(int(self.ctx))

class Site(models.Model):
	site_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return str(self.site_id) + " " + self.name

class Run(models.Model):
	run_id = models.IntegerField(primary_key=True)
	date = models.DateField()
	time = models.TimeField()
	conditions = models.TextField()
	initials = models.CharField(max_length=20)
	def __str__(self):
		return str(self.run_id) + " " + str(self.date) + " " + str(self.time) + " [conditions]" + self.initials

class Swabber(models.Model):
	# run_id = models.IntegerField(primary_key=True)
	run_id = models.ForeignKey(Run, db_column="run_id", on_delete=models.CASCADE, primary_key=True)
	swabber = models.CharField(max_length=20)
	def __str__(self):
		return str(self.run_id.run_id) + " " + self.swabber

class Plate(models.Model):
	plate_id = models.IntegerField(primary_key=True)
	run_id = models.ForeignKey('Run', db_column="run_id", on_delete=models.CASCADE)
	site_id = models.ForeignKey('Site', db_column="site_id", on_delete=models.CASCADE)
	agar_id = models.ForeignKey('Agar', db_column="agar_id", on_delete=models.CASCADE)
	cfu = models.IntegerField()
	def __str__(self):
		return str(self.plate_id) + " " + str(self.run_id.run_id) + " " + str(self.site_id.site_id) + " " + str(self.agar_id.agar_id) + " " + str(self.cfu)

class Isolate(models.Model):
	iso_id = models.IntegerField(primary_key=True)
	plate_id = models.ForeignKey(Plate, db_column="plate_id", on_delete=models.CASCADE)
	def __str__(self):
		return str(self.iso_id) + " " + str(self.plate_id.plate_id)




