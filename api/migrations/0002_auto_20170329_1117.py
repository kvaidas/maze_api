# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 08:17
from __future__ import unicode_literals

import json
import os

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def forwards_func(apps, schema_editor):
    Maze = apps.get_model("api", "Maze")
    db_alias = schema_editor.connection.alias
    maze_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mazes.json')
    with open(maze_file) as data_file:
        mazes = json.load(data_file)
    Maze.objects.using(db_alias).bulk_create([
        Maze(maze=mazes[x]) for x in range(0, len(mazes))
    ])


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Maze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maze', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evaluationresult',
            name='maze',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Maze'),
        ),
        migrations.AddField(
            model_name='evaluationresult',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evaluationresult',
            name='snippet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Snippet'),
        ),
        migrations.RunPython(forwards_func),
    ]
