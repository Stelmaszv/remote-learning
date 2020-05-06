from django.db import models
import datetime
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
    rotedata = models.DateTimeField(default=datetime.datetime.now())
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
class DashbordType(models.Model):
    name = models.CharField(max_length=240)
    def __str__(self):
        return self.name
class Dashbord(models.Model):
    theme         = models.CharField(max_length=240,verbose_name="Nagłówek")
    description   = models.TextField(verbose_name="Treść")
    file = models.FileField(upload_to='media', null=True, blank=True, verbose_name="Dodaj Plik")
    place =  models.ForeignKey(to='authorization.AccountType', on_delete=models.SET_NULL, null=True, blank=True,related_name='place',verbose_name="Typ uprawnień")
    lesson = models.ForeignKey(to='ordinance.Lesson', on_delete=models.SET_NULL, null=True, blank=True,related_name='lessons')
    type = models.ForeignKey(DashbordType, on_delete=models.SET_NULL, null=True, blank=True,related_name='lessons')
    author = models.ForeignKey(to='authorization.Account', on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.theme


