from __future__ import unicode_literals
from django.db import models
from common.utils import ChoiceEnum
from colorful.fields import RGBColorField
from datetime import timedelta


## participants
class ParticipantTypes(ChoiceEnum):
    student = 'student'
    photographer = 'photographer'
    non_photographer = 'non-photgrapher'

class Gender(ChoiceEnum):
    male = 'male'
    female = 'female'
    other = 'other'

class Participant(models.Model):
    def __str__(self):
        return ("%s" % self.name)

    name = models.CharField(max_length=200)
    profile = models.TextField(null=True)
    participation_group = models.CharField(max_length=50, choices=ParticipantTypes.choices())
    gender = models.CharField(max_length=20, choices=Gender.choices())


## recorded databases
class Recording(models.Model):
    def __str__(self):
        return ("%s" % self.name)

    name = models.CharField(max_length = 100)
    date = models.DateField()
    duration = models.DurationField(null=True, blank=True)
    data_collection_circumstances = models.TextField(default="", blank=True)
    sound_recording_url = models.URLField(null=True, blank = True)
    participant = models.ForeignKey('Participant', null=True)

class Photo(models.Model):
    def __str__(self):
        return ("%s" % self.name)
    name = models.CharField(max_length = 50)
    file_path = models.FilePathField(null=True, blank = True)
    file_url = models.URLField(null = True, blank = True)

class Transscription(models.Model):
    date = models.DateField()
    text_eng = models.TextField(default="", blank=True)
    text_hu = models.TextField(default="", blank=True)
    recording = models.ForeignKey('Recording')
    story = models.OneToOneField('Story', null=True, blank =True)

class Story(models.Model):
    class Meta:
        verbose_name_plural = 'Stories'
        ordering = ['-name']

    def __str__(self):
        return ("%s" % self.name)
    name = models.CharField(max_length = 100)
    participant = models.ForeignKey('Participant', null=True)
    photos = models.ManyToManyField('Photo', null=True, blank=True)
    order_in_recording = models.IntegerField( null=True, blank=True) # marks the position of the photo in the recoding
    duration = models.DurationField(null=True, blank=True, default=timedelta)
    video_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    analysis = models.ManyToManyField('AnalysisPoint', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    #todo connections



## analysis

class AnalysisType(models.Model):
    def __str__(self):
        return ("%s" % self.name)
    name = models.CharField(max_length = 50)
    description = models.TextField( default="", blank=True)


class AnalysisPoint(models.Model):
    def __str__(self):
        return ("%s" % self.name)
    name = models.CharField(max_length = 50)
    analysis_type = models.ForeignKey('AnalysisType')
    description = models.CharField(max_length=2000, null=True, blank=True)
    color_code = RGBColorField()

## connection types
class ConnectionRange(ChoiceEnum):
    interconnection = 'Interconnection'
    intraconnection = 'Intraconnection'

class StoryToStoryConnection(models.Model):
    story1 = models.ForeignKey('Story', related_name='story1')
    story2 = models.ForeignKey('Story', related_name='story2')
    connection_range = models.CharField(max_length=30, choices=ConnectionRange.choices())

class StoryInTheme(models.Model):
    number = models.IntegerField()
    story = models.ForeignKey('Story')
    theme = models.ForeignKey('Theme')

class Theme(models.Model):
    def __str__(self):
        return ("%s" % self.name)
    name = models.CharField(max_length = 50)
    description = models.TextField(default="", blank=True)
    stories = models.ManyToManyField('Story', through=StoryInTheme)
    connection_range = models.CharField(max_length=30, choices=ConnectionRange.choices())

class ThemeInChain(models.Model):
    number = models.IntegerField()
    theme = models.ForeignKey('Theme')
    chain = models.ForeignKey('Chain')

class Chain(models.Model):
    def __str__(self):
        return("%s" % self.name)

    name = models.CharField(max_length = 50)
    description = models.TextField(default="", blank=True)
    themes = models.ManyToManyField('Theme', through=ThemeInChain)
    connection_range = models.CharField(max_length=30, choices=ConnectionRange.choices())

