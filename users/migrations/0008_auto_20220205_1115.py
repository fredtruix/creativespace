# Generated by Django 3.2.5 on 2022-02-05 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Behance',
            new_name='behance',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Dribble',
            new_name='dribble',
        ),
    ]