# Generated by Django 5.1 on 2024-08-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.URLField(default='https://res.cloudinary.com/dycdgsbm3/image/upload/v1724406847/person-placeholder-5_pttwjo.png'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
