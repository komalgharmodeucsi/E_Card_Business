# Generated by Django 3.1.2 on 2020-10-28 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Card_App', '0016_auto_20201028_1850'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
    ]
