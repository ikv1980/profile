from django.db import models
from PIL import Image


# Create your models here.
class Education(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    company = models.CharField(verbose_name='Компания', max_length=50)
    url = models.CharField(verbose_name='Ссылка на сертификат', max_length=1000)
    img = models.ImageField('Изображение', upload_to='sertificat', blank=True)

    # Указываем красивые подписи объектов
    def __str__(self):
        return f'{self.company}: {self.name}'

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'