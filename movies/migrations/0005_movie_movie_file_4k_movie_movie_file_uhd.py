# Generated by Django 4.1.3 on 2022-11-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_scene_image_1_movie_scene_image_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_file_4k',
            field=models.FileField(default=None, upload_to='movie_file/'),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_file_UHD',
            field=models.FileField(default=None, upload_to='movie_file/'),
        ),
    ]