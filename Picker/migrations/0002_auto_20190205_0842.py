# Generated by Django 2.1.5 on 2019-02-05 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Picker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fridge',
            old_name='ingredient_id',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='fridge',
            old_name='user_id',
            new_name='user',
        ),
    ]
