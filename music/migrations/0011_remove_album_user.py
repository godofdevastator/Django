# Generated by Django 2.0 on 2018-01-01 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_album_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='User',
        ),
    ]
