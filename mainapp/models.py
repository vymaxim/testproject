from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=64, unique=True)
    floor = models.IntegerField()

    def __str__(self):
        return f'{self.name} этаж {self.floor}'


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    GENDER_CHOISES = (
        ('Mуж.', 'Муж.'),
        ('Жен.', 'Жен.')
    )
    name = models.CharField(max_length=64, verbose_name='Имя')
    surname = models.CharField(max_length=64, verbose_name='Фамилия')
    age = models.PositiveIntegerField(blank=True, verbose_name='Возраст')
    gender = models.CharField(max_length=4, choices=GENDER_CHOISES, verbose_name='Пол')
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name='Отдел')
    programming_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, verbose_name='Язык')

    def __str__(self):
        return f'{self.name} {self.surname}'
