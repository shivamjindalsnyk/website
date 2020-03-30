# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2019-12-30 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0174_auto_20191125_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalapplication',
            name='time_commitment_updates',
            field=models.TextField(blank=True, help_text='Make sure your time commitments lists any current or future jobs you have, even if you are taking a leave of absence.', max_length=8000, verbose_name='(Optional) If your time commitments are incorrect or have changed, please provide your updated time commitments.'),
        ),
        migrations.AddField(
            model_name='finalapplication',
            name='time_commitments_correct',
            field=models.BooleanField(default=False, help_text='If any time commitments (like a job or school) are missing, say no.', verbose_name='Are the time commitments listed above correct?'),
        ),
    ]