# Generated by Django 2.2.7 on 2019-11-15 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_auto_20191113_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.CharField(choices=[('SUMMER', 'Summer'), ('UNKNOWN', 'Unknown'), ('SPRING', 'Spring'), ('FALL', 'Fall'), ('WINTER', 'Winter')], default='UNKNOWN', max_length=6),
        ),
    ]
