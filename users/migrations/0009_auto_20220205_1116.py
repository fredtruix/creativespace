# Generated by Django 3.2.5 on 2022-02-05 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20220205_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='behance',
        ),
        migrations.RemoveField(
            model_name='user',
            name='disha',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dribble',
        ),
        migrations.RemoveField(
            model_name='user',
            name='github',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gitlab',
        ),
        migrations.RemoveField(
            model_name='user',
            name='meduim',
        ),
    ]
