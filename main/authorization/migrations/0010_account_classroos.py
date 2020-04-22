# Generated by Django 3.0.5 on 2020-04-22 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordinance', '0009_auto_20200422_1443'),
        ('authorization', '0009_auto_20200422_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='classroos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classromms', to='ordinance.Classroom', verbose_name='Czy jest studentem ? (jesli nie pomiń)'),
        ),
    ]
