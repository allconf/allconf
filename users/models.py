from django.db import models
from manager.models import Lecture, Conference
from django.conf import settings


class Speaker(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='lectures'
    )
    lecture = models.OneToOneField(
        Lecture,
        verbose_name='Лекция',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Докладчик'
        verbose_name_plural = 'Докладчики'


class ConferenceOrganizer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='orginized_conferences'
    )
    conference = models.OneToOneField(
        Conference,
        verbose_name='Конференция',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'


class ConferenceModerator(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='moderated_conferences'
    )
    change_category = models.BooleanField(
        'Возможность изменять категорию конференции',
        default=False
    )
    change_identity = models.BooleanField(
        'Возможность изменять айдентику',
        default=False
    )
    change_date = models.BooleanField(
        'Возможность изменять дату проведения конференции',
        default=False
    )
    manage_speakers = models.BooleanField(
        'Возможность управлять докладчиками',
        default=False
    )
    change_landing = models.BooleanField(
        'Возможность изменять лендинг конференции',
        default=False
    )
    conference = models.ForeignKey(
        Conference, verbose_name='Конференция',
        on_delete=models.CASCADE,
        related_name='moderators'
    )

    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'


class Listener(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='booked_conferences'
    )
    arrival_time = models.DateTimeField(
        'Время прихода',
        null=True,
        blank=True
    )
    conference = models.ForeignKey(
        Conference,
        verbose_name='Конференция',
        on_delete=models.CASCADE,
        related_name='listeners'
    )

    class Meta:
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетители'
