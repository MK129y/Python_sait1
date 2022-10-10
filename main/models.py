from django.db import models

# Create your models here.
class Task(models.Model):
    titel = models.CharField('Название', max_length=50)
    task = models.TextField('Opisan')

    def __str__(self):
        return  self.titel

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural= 'Задачи'
