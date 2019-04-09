# Generated by Django 2.1.5 on 2019-04-09 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Picker', '0005_auto_20190402_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishcategory',
            name='dishes',
            field=models.ManyToManyField(blank=True, to='Picker.Dish'),
        ),
        migrations.AlterField(
            model_name='ingredientcategory',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='Picker.Ingredient'),
        ),
    ]