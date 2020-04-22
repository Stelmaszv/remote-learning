from core.baseview import baseCreate,baseListView;
from core.decorators import login_required,login_manager,login_educator
from authorization.forms import educator,manager
from .forms import Lesson as LessonForm
from .models import Lesson
from authorization.models import Account
from authorization.formMenager import passwordGeneartor
from helpel import email
from django.shortcuts import render
class add_Student(baseCreate):
    template_name = 'ordinance/addperson.html'
    success_url = '/ordinance/myStudents/'
    form=educator
    getObject = Account
    @login_educator
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def postSave(self, request, *args, **kwargs):
        item = Account.objects.latest('id')
        item.username = self.form.cleaned_data['first_name'] + ' ' + self.form.cleaned_data['last_name']
        password = passwordGeneartor().setPassword()
        print(password)
        item.set_password(password)
        item.staff = True
        item.is_student = request.user.is_educator
        item.save()
        email().sent('Dane do konta', 'kotek',['zupartl@johnderasia.com'])
class add_Personel(baseCreate):
    template_name = 'ordinance/addperson.html'
    success_url = '/ordinance/myPersonel/'
    form=manager
    @login_manager
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def postSave(self, request, *args, **kwargs):
        item = Account.objects.latest('id')
        item.username = self.form.cleaned_data['first_name'] + ' ' + self.form.cleaned_data['last_name']
        password = passwordGeneartor().setPassword()
        print(password)
        item.set_password(password)
        item.staff = True
        item.save()
        email().sent('Dane do konta', 'kotek', ['zupartl@johnderasia.com'])
class addLesson(baseCreate):
    template_name = 'ordinance/addLesson.html'
    success_url = '/'
    form=LessonForm
    def get(self, request, *args, **kwargs):
        self.form.email=request.user.email
        return self.addGet(request)
class myStudents(baseListView):
    template_name = 'ordinance/myStudents.html'
    @login_educator
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self, request):
        self.context = {
            'items': Account.objects.filter(is_student__name=request.user.is_educator).order_by('-last_name')
        }
class myLesson(baseListView):
    template_name = 'ordinance/myLessons.html'
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self, request):
        self.context = {
            'items': Lesson.objects.all().order_by('-data')
        }
class myPersonel(baseListView):
    template_name = 'ordinance/myPersonel.html'
    @login_manager
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self, request):
        self.context = {
            'items': Account.objects.filter(is_student__name=request.user.is_educator).order_by('-last_name')
        }


