# Generated by Django 4.0.4 on 2022-05-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_alter_conference_title_alter_lecture_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='upload',
            field=models.ImageField(null=True, upload_to='uploads/', verbose_name='Главное изображение'),
        ),
    ]