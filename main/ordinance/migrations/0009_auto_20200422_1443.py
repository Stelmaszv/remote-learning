# Generated by Django 3.0.5 on 2020-04-22 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordinance', '0008_lesson_subjects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='subject',
            new_name='theme',
        ),
    ]