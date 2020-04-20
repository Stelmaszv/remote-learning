from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager
from ordinance.models import Classroom,Subject
class AccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('user has no email')
        if not username:
            raise ValueError('user has no email')
        user= self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password):
        user= self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin= True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
class AccountType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
class Account(AbstractBaseUser):
    first_name          = models.CharField(max_length=250, null=True, blank=True)
    last_name           = models.CharField(max_length=250, null=True, blank=True)
    email               = models.EmailField(verbose_name="email",max_length=50,unique=True)
    username            = models.CharField(max_length=30)
    date_joined         = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=True)
    is_superuser        = models.BooleanField(default=False)
    type                = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True, blank=True,related_name='type')
    is_student          = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True,related_name='student')
    is_teacher          = models.ManyToManyField(Subject, null=True, blank=True)
    is_educator         = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True,related_name='educator')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    object=AccountManager()
    objects = models.Manager()

    def __str__(self):
        return str(self.first_name)+" "+str(self.last_name)
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True