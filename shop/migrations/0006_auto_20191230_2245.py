# Generated by Django 3.0 on 2019-12-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20191230_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='update_desc',
            field=models.CharField(max_length=5000),
        ),
    ]
