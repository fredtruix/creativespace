# Generated by Django 3.2.5 on 2022-02-08 14:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]