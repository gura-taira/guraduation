from django.db import models


class Affair(models.Model):
    """事件情報"""
    place = models.CharField('町名', max_length=255)
    name = models.CharField('事件名', max_length=255, blank=True)
    time = models.CharField('発生時刻', max_length=127)
    content = models.TextField('事件内容', blank=True)

    def __str__(self):
        return self.name


