# Generated by Django 3.0 on 2021-05-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='content',
            new_name='messages',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='status',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
