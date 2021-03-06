# Generated by Django 4.0.4 on 2022-05-09 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.lecture', verbose_name='Лекция')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Докладчик',
                'verbose_name_plural': 'Докладчики',
            },
        ),
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.DateTimeField(blank=True, null=True, verbose_name='Время прихода')),
                ('conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.conference', verbose_name='Конференция')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConferenceOrganizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.conference', verbose_name='Конференция')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConferenceModerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_category', models.BooleanField(default=False, verbose_name='Возможность изменять категорию конференции')),
                ('change_identity', models.BooleanField(default=False, verbose_name='Возможность изменять айдентику')),
                ('change_date', models.BooleanField(default=False, verbose_name='Возможность изменять дату проведения конференции')),
                ('manage_speakers', models.BooleanField(default=False, verbose_name='Возможность управлять докладчиками')),
                ('change_landing', models.BooleanField(default=False, verbose_name='Возможность изменять лендинг конференции')),
                ('conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.conference', verbose_name='Конференция')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
