# Generated by Django 3.1.2 on 2020-10-28 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Card_App', '0011_auto_20201028_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='firstname',
        ),
    ]
