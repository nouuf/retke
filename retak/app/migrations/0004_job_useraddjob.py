# Generated by Django 3.2.2 on 2021-05-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210507_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='useraddjob',
            field=models.ManyToManyField(related_name='useraddjob', to='app.User'),
        ),
    ]
