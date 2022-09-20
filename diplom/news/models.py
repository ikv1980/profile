from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image #Альтернативная установка:  python -m pip install Pillow

# Таблица новостей
class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Текст статьи')
    img = models.ImageField('Картинка для статьи', default='default.webp', upload_to='news_images', blank=True)
    date = models.DateTimeField('Дата', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    views = models.IntegerField('Просмотры', default=1)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)
        if image.height > 300 or image.width > 600:
            resize = (300, 600)
            image.thumbnail(resize)
            image.save(self.img.path)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'