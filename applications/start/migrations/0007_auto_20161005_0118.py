# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0006_auto_20161004_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angle', models.IntegerField()),
                ('game_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.GameSession')),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.Movement')),
            ],
        ),
        migrations.AddField(
            model_name='gamesession',
            name='movements',
            field=models.ManyToManyField(through='start.Performance', to='start.Movement'),
        ),
    ]