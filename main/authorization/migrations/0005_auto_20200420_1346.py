# Generated by Django 3.0.5 on 2020-04-20 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_auto_20200420_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_manager',
        ),
        migrations.RemoveField(
            model_name='account',
            name='type',
        ),
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='authorization.AccountType'),
        ),
    ]
