# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 01:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('confabulation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile', models.CharField(max_length=2000)),
                ('participation_group', models.CharField(choices=[(b'non-photgrapher', b'non_photographer'), (b'photographer', b'photographer'), (b'student', b'student')], max_length=50)),
                ('gender', models.CharField(choices=[(b'female', b'female'), (b'male', b'male'), (b'other', b'other')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FilePathField()),
                ('duration', models.DurationField()),
                ('order_in_recording', models.IntegerField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('data_collection_circumstances', models.CharField(max_length=2000)),
                ('sound_recording', models.FilePathField(blank=True, null=True)),
                ('photos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='confabulation.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('transscribe_eng', models.CharField(blank=True, max_length=10000, null=True)),
                ('transscribe_hu', models.CharField(blank=True, max_length=10000, null=True)),
                ('video_url', models.FilePathField(blank=True, null=True)),
                ('thumbnail', models.FilePathField(blank=True, null=True)),
                ('analysis_points', models.CharField(choices=[(b'confabulation', b'confabulation'), (b'connection', b'connection'), (b'emotion', b'emotion'), (b'framing', b'framing'), (b'interaction', b'interaction')], max_length=50)),
                ('emotions', models.CharField(blank=True, choices=[(b'conflicted', b'conflicted'), (b'surprsied', b'surprised'), (b'traume', b'trauma')], max_length=50, null=True)),
                ('interactions', models.CharField(blank=True, choices=[(b'analyzer', b'analyze'), (b'audience', b'audience'), (b'block', b'block'), (b'non-block trigger', b'non_block_trigger'), (b'respond to trigger', b'respond_to_trigger')], max_length=50, null=True)),
                ('framing', models.CharField(blank=True, choices=[(b'connection', b'connection'), (b'gray matter', b'gray_matter'), (b'identify only', b'identify_only'), (b'insecure deflection', b'insecure_deflection'), (b'theme', b'theme'), (b'theme subject', b'theme_ubject'), (b'themeconnection', b'themeconnection')], max_length=50, null=True)),
                ('connections', models.CharField(blank=True, choices=[(b'story to story connection', b'story_to_story'), (b'theme over multiple stories', b'theme'), (b'common motif over multiple themes', b'theme_motif'), (b'theme to theme connection', b'theme_to_theme')], max_length=50, null=True)),
                ('photos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='confabulation.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='StoryConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.ManyToManyField(to='confabulation.Story')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confabulation.Story')),
            ],
        ),
        migrations.CreateModel(
            name='ThemeConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.ManyToManyField(to='confabulation.Theme')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='themes',
            field=models.ManyToManyField(to='confabulation.Theme'),
        ),
        migrations.AddField(
            model_name='recording',
            name='stories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='confabulation.Story'),
        ),
        migrations.AddField(
            model_name='participant',
            name='recording',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='confabulation.Recording'),
        ),
    ]
