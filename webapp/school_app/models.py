from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime

class Student(models.Model):
    """Школьники"""

    class Meta:
        db_table = "students"
        verbose_name = "Информация о школьнике"
        verbose_name_plural = "Информация о школьниках"
    
    student_name = models.TextField(verbose_name="Школьник")
    student_year = models.TextField(verbose_name="Год обучения")
    student_group = models.TextField(verbose_name="Класс")

    def __str__(self):
        return f"{self.student_name} {self.student_group}"

class Teacher(models.Model):
    """Учителя"""

    class Meta:
        db_table = "teachers"
        verbose_name = "Информация об учителе"
        verbose_name_plural = "Информация об учителях"

    teacher_name = models.TextField(verbose_name="Учитель")
    teacher_edu = models.TextField(verbose_name="Образование учителя")
    teacher_subject = models.TextField(verbose_name="Предмет учителя")

    def __str__(self):
        return f"{self.teacher_name} {self.teacher_subject}"

class Attendance(models.Model):
    """Посещаемость"""

    class Meta:
        db_table = "attendance"
        verbose_name = "Посещения обучающегося"
        verbose_name_plural = "Посещения обучающихся"
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Школьник")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Учитель")
    date = models.DateField(verbose_name="Дата занятия")
    indicator = models.BooleanField(verbose_name="Посещение")

    def __str__(self):
        return f"{self.student} {self.date} {self.indicator} {self.teacher}"

def mark_validator(mark):
    if mark not in [0, 2, 3, 4, 5]:
        raise ValidationError(
            gettext_lazy('%(mark)i is wrong mark'),
            params={'mark':mark}
        )

class Performance(models.Model):
    """Успеваемость"""

    class Meta:
        db_table = "performance"
        verbose_name = "Успеваемость школьника"
        verbose_name_plural = "Успеваемость школьников"

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Школьник")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Учитель")
    date = models.DateField(verbose_name="Дата занятия")
    mark = models.IntegerField(verbose_name="Оценка",validators=[mark_validator])

    def __str__(self):
        return f"{self.student} {self.date} {self.mark} {self.teacher}"