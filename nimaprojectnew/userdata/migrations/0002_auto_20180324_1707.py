# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-24 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180324_1703'),
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applieduser',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Branch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Branch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eligibility',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Branch'),
            preserve_default=False,
        ),
    ]
