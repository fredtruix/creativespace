# Generated by Django 3.2.5 on 2022-02-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
