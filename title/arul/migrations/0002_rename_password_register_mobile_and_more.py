# Generated by Django 4.2.1 on 2023-10-15 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arul', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='password',
            new_name='Mobile',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='username',
            new_name='Name',
        ),
    ]
