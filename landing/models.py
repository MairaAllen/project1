from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    teaching_course = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


# Имя поля = models.ТипПоля(его атрибуты)
# сохранение изменений или нововведений в специальный файл
# отправка изменений в базу данных

class Lead(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.last_name} ({self.phone_number})'
    


#Foreignkey - тип поля один-к-одному
# это поле необходимое для создания связи какого либо поля с другой моделью

# атрибут null() - по умолчанию ВО ВСЕХ ПОЛЯХ этот атрибут приравнивается к False
# необходим для определения обязательности внесения информации в какое либо поле
# так как в БД все поля по умолчанию должны быть непустыми

# есть три сценария действия БД после 
# удаления какой либо модели к которой налажена связь:
# 1) если модель была удалена, то будет удален и столбец в таблице, который ссылался на эту модель - models.CASCADE
# 2) если модель была удалена, то поля столбца, который ссылался на эту модель примет значение null - models.SET_NULL
# 3) если модель была удалена, то значение полей столбца,
# который ссылался на эту модель , сохранятся - models.PROTECT

