# Generated by Django 3.1.1 on 2020-09-29 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0007_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likers',
        ),
    ]