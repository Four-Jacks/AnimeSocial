# Generated by Django 2.2.7 on 2019-11-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0010_auto_20191116_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.CharField(choices=[('WINTER', 'Winter'), ('SUMMER', 'Summer'), ('UNKNOWN', 'Unknown'), ('SPRING', 'Spring'), ('FALL', 'Fall')], default='UNKNOWN', max_length=6),
        ),
    ]
