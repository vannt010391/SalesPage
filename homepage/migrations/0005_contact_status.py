# Generated by Django 3.0 on 2021-05-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20210525_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('Wait', 'Chờ xử lý'), ('SPAM', 'SPAM'), ('COMPLETED', 'HOÀN TẤT')], default='Wait', max_length=50),
        ),
    ]
