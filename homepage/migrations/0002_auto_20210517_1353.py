# Generated by Django 3.0 on 2021-05-17 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='fullname',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
