# Generated by Django 2.2 on 2019-11-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_auto_20191117_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='prohibition',
            field=models.TextField(blank=True),
        ),
    ]