# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_address = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")

    def __unicode__(self):
    	return "{}, {}".format(self.user,self.last_name)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Student(models.Model):
	id = models.AutoField(primary_key=True)

	student_username = models.ForeignKey(User)
	student_first_name = models.CharField(max_length = 200)
	student_family_name = models.CharField(max_length = 200)

	def __unicode__(self):
		return unicode(self.student_username)

class Mark(models.Model):
	id = models.AutoField(primary_key=True)
	student_username = models.ForeignKey(User)

	mark_hesaban = models.FloatField()
	mark_fizic = models.FloatField()
	mark_shimi = models.FloatField()

	def __unicode__(self):
		return "{}, {}".format(self.student_username, self.id)

class Study(models.Model):
	id = models.AutoField(primary_key=True)
	student_username = models.ForeignKey(User)

	study_hesaban = models.FloatField()
	study_fizic = models.FloatField()
	study_shimi = models.FloatField()

	def __unicode__(self):
		return "{}, {}".format(self.student_username, self.id)

class SysMark(models.Model):
	id = models.AutoField(primary_key=True)
	student_username = models.ForeignKey(User)

	sys_mark_lesson = models.CharField(max_length = 200,default='')
	sys_mark = models.FloatField(blank=True,null=True)

	def __unicode__(self):
		return "{}, {}".format(self.student_username, self.id)

class PracLevel(models.Model):
	id = models.AutoField(primary_key=True)
	student_username = models.ForeignKey(User)

	prac_level_lesson = models.CharField(max_length = 200,default='')
	prac_level = models.FloatField(blank=True,null=True)

	def __unicode__(self):
		return "{}, {}".format(self.student_username, self.id)

class Practice(models.Model):
	practice_id = models.AutoField(primary_key=True)

	practice_title = models.CharField(max_length = 200)
	practice_lesson = models.CharField(max_length = 200,default='')
	practice_content = models.ImageField(upload_to='web/static/media/practices')
	practice_level = models.CharField(max_length = 200)

	def __unicode__(self):
		return "{}, {}".format(self.practice_title, self.practice_id)

class Question(models.Model):
	question_id = models.AutoField(primary_key=True)

	question_title = models.CharField(max_length = 200)
	question_lesson = models.CharField(max_length = 200,default='')
	question_content = models.ImageField(upload_to='web/static/media/questions')
	question_answer1 = models.CharField(max_length = 200)
	question_answer2 = models.CharField(max_length = 200)
	question_answer3 = models.CharField(max_length = 200)
	question_answer4 = models.CharField(max_length = 200)
	question_right_answer = models.CharField(max_length = 200)

	def __unicode__(self):
		return "{}, {}".format(self.question_title, self.question_id)
	