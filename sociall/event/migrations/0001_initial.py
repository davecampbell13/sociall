# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instagram_hashtag', models.CharField(max_length=255)),
                ('instagram_handle', models.CharField(max_length=255)),
                ('twitter_hashtag', models.CharField(max_length=255)),
                ('twitter_handle', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_url', models.TextField()),
                ('caption', models.TextField()),
                ('post_by', models.CharField(max_length=255)),
                ('post_date', models.DateTimeField()),
                ('tags', models.TextField()),
                ('like_count', models.CharField(max_length=255)),
                ('show', models.BooleanField()),
                ('event', models.ForeignKey(to='event.Event')),
            ],
        ),
    ]
