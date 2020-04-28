# Generated by Django 3.0.5 on 2020-04-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinance', '0009_auto_20200422_1443'),
        ('authorization', '0011_auto_20200422_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='classrooms',
        ),
        migrations.AddField(
            model_name='account',
            name='classrooms',
            field=models.ManyToManyField(blank=True, null=True, related_name='classromms', to='ordinance.Classroom', verbose_name='Jeśli jest nauczycielem to jakich przemiotów uczy ? (jesli nie to pomiń)'),
        ),
    ]