# Generated by Django 3.1.5 on 2021-01-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0022_algorithm_sr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='SR',
            field=models.FloatField(default=0),
        ),
    ]