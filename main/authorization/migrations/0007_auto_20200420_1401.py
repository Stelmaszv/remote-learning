# Generated by Django 3.0.5 on 2020-04-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_auto_20200420_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
