# Generated by Django 2.2.7 on 2019-11-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191115_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(default='https://thehaletelescope.com/wp-content/uploads/2018/10/weeb.jpg', max_length=256),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='favorite_anime',
            field=models.CharField(default='Cowboy Bebop', max_length=256),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(default='I love anime', max_length=256),
        ),
    ]
