from django.db import models
class Dashbord(models.Model):
    theme         = models.CharField(max_length=240,verbose_name="Nagłówek")
    description   = models.TextField(verbose_name="Treść")
    def __str__(self):
        return self.theme


