from django.db import models
class Classroom(models.Model):
    name = models.CharField(max_length=30, unique=True)
    students = models.ManyToManyField(to='authorization.Account')
    def __str__(self):
        return self.name
class Subject(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
class Tasks(models.Model):
    student        = models.ForeignKey(to='authorization.Account', on_delete=models.SET_NULL, null=True, blank=True)
    data_recived   = models.BooleanField(default=False)
    taskfile = models.FileField(upload_to='media', null=True, blank=True, verbose_name="Dodaj Plik")
    lessons = models.ForeignKey(to='ordinance.Lesson', on_delete=models.SET_NULL, null=True, blank=True,related_name='lesson')
    rote = models.IntegerField()
    def __str__(self):
        return self.student.username
class Lesson(models.Model):
    theme         = models.CharField(max_length=240,verbose_name="Temat zajęc")
    description   = models.TextField(verbose_name="Opis zajęc")
    data          = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    classroom     = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True)
    subjects      = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    teacher       = models.ForeignKey(to='authorization.Account', on_delete=models.SET_NULL, null=True, blank=True)
    taskfile      = models.FileField(upload_to='media', null=True,blank=True,verbose_name="Dodaj Plik")
    tasks         = models.ManyToManyField(Tasks)
    def __str__(self):
        return self.theme

