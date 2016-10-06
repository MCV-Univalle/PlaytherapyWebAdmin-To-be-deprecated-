# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-04 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('therapist', '0004_therapist'),
        ('patient', '0005_auto_20161004_0146'),
        ('start', '0003_auto_20161004_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('score', models.IntegerField()),
                ('repetitions', models.IntegerField()),
                ('time', models.IntegerField()),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Minigame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TherapySession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('objective', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapist.Therapist')),
            ],
        ),
        migrations.AddField(
            model_name='minigame',
            name='movements',
            field=models.ManyToManyField(to='start.Movement'),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='minigame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.Minigame'),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='therapy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.TherapySession'),
        ),
    ]
