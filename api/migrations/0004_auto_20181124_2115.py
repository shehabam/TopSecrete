# Generated by Django 2.1.2 on 2018-11-24 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_viewrs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='viewrs',
            new_name='viewers',
        ),
    ]