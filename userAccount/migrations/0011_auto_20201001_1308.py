# Generated by Django 3.1.1 on 2020-10-01 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0010_auto_20201001_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userImage',
            field=models.ImageField(default='media/default/20A-1User-512.png', upload_to='media/Profiles'),
        ),
    ]
