# Generated by Django 2.2.7 on 2019-11-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.CharField(choices=[('UNKNOWN', 'Unknown'), ('SPRING', 'Spring'), ('SUMMER', 'Summer'), ('FALL', 'Fall'), ('WINTER', 'Winter')], default='UNKNOWN', max_length=6),
        ),
        migrations.AlterField(
            model_name='season',
            name='year',
            field=models.CharField(default='0000', max_length=4),
        ),
    ]