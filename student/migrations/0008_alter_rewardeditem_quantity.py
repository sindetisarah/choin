# Generated by Django 3.2.8 on 2021-11-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20211108_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewardeditem',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]