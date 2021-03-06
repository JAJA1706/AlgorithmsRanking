# Generated by Django 3.1.4 on 2021-01-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0020_benchmark_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='algorithm',
            old_name='score',
            new_name='score1',
        ),
        migrations.AddField(
            model_name='algorithm',
            name='score2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='algorithm',
            name='total_score',
            field=models.FloatField(default=0),
        ),
    ]
