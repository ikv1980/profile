from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Link(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    longlink = models.CharField(verbose_name='Длинная ссылка', max_length=1000)
    title = models.CharField(verbose_name='Заголовок ссылки', max_length=500)
    slug = models.SlugField(verbose_name='Идентификатор', unique=True)

    # Указываем красивые подписи объектов
    def __str__(self):
        return f'/{self.user}/{self.slug}/ - ({self.title[0:25]}...)'

    class Meta:
        verbose_name = 'Cсылка'
        verbose_name_plural = 'Cсылки'
