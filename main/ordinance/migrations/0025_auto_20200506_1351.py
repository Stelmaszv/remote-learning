# Generated by Django 3.0.5 on 2020-05-06 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordinance', '0024_auto_20200505_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashbordType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
            ],
        ),
        migrations.AddField(
            model_name='dashbord',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='ordinance.DashbordType'),
        ),
    ]
