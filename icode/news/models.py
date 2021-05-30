from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    preview_image = models.ImageField(upload_to='preview/%Y/%m/%d', verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'news_news'
        verbose_name = _('новость')
        verbose_name_plural = _('новости')
        ordering = ('created_at',)
