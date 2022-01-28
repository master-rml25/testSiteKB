from django.db import models


class Person(models.Model):

    DOSTUP_CHOICES = (  # список уровней доступа
        ('1', 'Мониторинг'),
        ('2', 'Мониторинг + карта'),
        ('3', 'Управление устройствами'),
    )

    operator = models.CharField(
        max_length=50,
        verbose_name='Логин оператора',
        help_text="Логин должен совпадать с логином пользователей"
    )
    organisation = models.CharField(
        max_length=50,
        verbose_name='Название организации'
    )
    site_organis = models.CharField(
        max_length=50,
        default="www.site.site",
        verbose_name='Сайт организации'
    )
    dostup = models.CharField(
        max_length=25,
        verbose_name='Уровень доступа',
        choices=DOSTUP_CHOICES
    )

    def __str__(self):
        return f"{self.operator}, {self.organisation}"

    class Meta:
        ordering = ('organisation',)
