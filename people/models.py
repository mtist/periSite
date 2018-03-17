from django.db import models


class People(models.Model):
    name = models.CharField('Имя', max_length=32)
    surname = models.CharField('Фамилия', max_length=32)
    email = models.EmailField('Почта')
    cafeId = models.IntegerField(name='Кафе')

    # def __str__(self):
    #     return self.id


class Cafe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Название', max_length=32)
    pic = models.ImageField('Фото')
    address = models.CharField('Адрес', max_length=64)
    icon = models.ImageField('Иконка')

    # def __str__(self):
    #     return self.id
