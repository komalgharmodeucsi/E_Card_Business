# Generated by Django 3.1.2 on 2020-10-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Card_App', '0014_auto_20201028_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(default='', max_length=70),
        ),
    ]
