# Generated by Django 3.2.6 on 2022-04-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='comment/photos/%Y/%m/%d/', verbose_name='Фото профиля'),
        ),
    ]
