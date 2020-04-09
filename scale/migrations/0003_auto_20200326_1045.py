# Generated by Django 3.0.4 on 2020-03-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale', '0002_user_hex_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.FloatField(default=170),
        ),
    ]
