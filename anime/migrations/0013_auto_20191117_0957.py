# Generated by Django 2.2.7 on 2019-11-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0012_auto_20191117_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.CharField(choices=[('SPRING', 'Spring'), ('WINTER', 'Winter'), ('UNKNOWN', 'Unknown'), ('FALL', 'Fall'), ('SUMMER', 'Summer')], default='UNKNOWN', max_length=6),
        ),
    ]
