# Generated by Django 3.2.8 on 2021-11-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]