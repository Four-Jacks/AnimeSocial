# Generated by Django 2.2.7 on 2019-11-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0017_auto_20191117_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.CharField(choices=[('FALL', 'Fall'), ('UNKNOWN', 'Unknown'), ('WINTER', 'Winter'), ('SUMMER', 'Summer'), ('SPRING', 'Spring')], default='UNKNOWN', max_length=6),
        ),
    ]