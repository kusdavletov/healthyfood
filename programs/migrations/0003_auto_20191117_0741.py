# Generated by Django 2.2 on 2019-11-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20191117_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='breakfast_image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='brunch_image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='dinner_image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='dunch_image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='lunch_image',
            field=models.URLField(),
        ),
    ]