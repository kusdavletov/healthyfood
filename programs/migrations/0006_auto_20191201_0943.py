# Generated by Django 2.1.1 on 2019-12-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_auto_20191130_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='breakfast_image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='brunch_image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='dinner_image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='dunch_image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='lunch_image',
            field=models.TextField(),
        ),
    ]
