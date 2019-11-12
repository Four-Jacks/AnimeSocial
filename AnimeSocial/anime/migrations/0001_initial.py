# Generated by Django 2.2.7 on 2019-11-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('title_jap', models.CharField(blank=True, default='N/A', max_length=256, null=True)),
                ('img_url', models.CharField(blank=True, default='https://i.pinimg.com/originals/11/ea/01/11ea01854b381fa350ca6ed8c77fe13b.png', max_length=256, null=True)),
                ('type', models.CharField(blank=True, default='N/A', max_length=5, null=True)),
                ('season', models.CharField(blank=True, default='N/A', max_length=11, null=True)),
                ('status', models.CharField(blank=True, default='N/A', max_length=16, null=True)),
                ('air_date', models.CharField(blank=True, default='N/A', max_length=32, null=True)),
                ('synopsis', models.TextField(blank=True, default='N/A', null=True)),
            ],
            options={
                'verbose_name_plural': 'anime',
            },
        ),
    ]
