# Generated by Django 4.1.7 on 2023-03-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0004_alter_rockband_musicians'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rockband',
            old_name='genre',
            new_name='genres',
        ),
    ]
