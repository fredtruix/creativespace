# Generated by Django 3.2.5 on 2022-02-06 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20220206_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='name',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='name',
        ),
        migrations.DeleteModel(
            name='Creator',
        ),
        migrations.DeleteModel(
            name='Design',
        ),
        migrations.DeleteModel(
            name='Developer',
        ),
    ]
