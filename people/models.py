from django.db import models


class Cafe(models.Model):
    name = models.CharField('Название', max_length=32)
    pic = models.ImageField('Фото')
    address = models.CharField('Адрес', max_length=64)
    icon = models.ImageField('Иконка')

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField('Имя', max_length=32)
    surname = models.CharField('Фамилия', max_length=32)
    email = models.EmailField('Почта')
    cafe = models.ForeignKey(Cafe, name='Кафе', on_delete=models.CASCADE)

    def __str__(self):
        return self.surname
