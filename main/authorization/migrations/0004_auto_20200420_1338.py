# Generated by Django 3.0.5 on 2020-04-20 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordinance', '0004_auto_20200420_1338'),
        ('authorization', '0003_remove_account_is_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='is_educator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='educator', to='ordinance.Classroom'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='ordinance.Classroom'),
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='account',
            name='is_teacher',
            field=models.ManyToManyField(to='ordinance.Subject'),
        ),
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.ManyToManyField(to='authorization.AccountType'),
        ),
    ]
