# Generated by Django 3.0.5 on 2020-05-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinance', '0022_auto_20200505_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashbord',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
        ),
    ]
