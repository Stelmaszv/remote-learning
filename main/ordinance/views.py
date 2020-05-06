from core.baseview import baseCreate,baseListView,baseShowView,baseUpdateView;
from core.decorators import login_required,login_manager,login_educator
from authorization.forms import educator,manager
from .forms import Lesson as LessonForm,TasksSolution,TasksSetRote,AccountForm,DashbordForm
from .models import Lesson,Tasks,Classroom,Dashbord,DashbordType
from authorization.models import Account,AccountType
from authorization.formMenager import passwordGeneartor
from helpel import email
from django.shortcuts import redirect,render
import datetime
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
class addDashbord(baseCreate):
    template_name = 'ordinance/addLesson.html'
    success_url = '/'
    form = DashbordForm
    def postSave(self, request, *args, **kwargs):
        Type = DashbordType.objects.get(name='normal')
        self.item.author=request.user
        self.item.type=Type
        self.item.save()
class addLesson(baseCreate):
    template_name = 'ordinance/addLesson.html'
    success_url = '/'
    form=LessonForm
    def get(self, request, *args, **kwargs):
        self.form.email=request.user.email
        return self.addGet(request)
    def post(self,request, *args, **kwargs):
        self.form.email = request.user.email
        print(request)
        return self.addPost(request)
    def postSave(self, request, *args, **kwargs):
        classrom=Classroom.objects.get(name=self.item.classroom).students.all()
        for student in classrom:
            task = Tasks(student=student, data_recived=False,lessons=self.item,rote=0)
            task.save()
            self.item.tasks.add(task)
            self.item.save()
        Type=DashbordType.objects.get(name='lesson')
        place=AccountType.objects.get(name='student')
        dashbord=Dashbord(theme=self.item.theme,description=self.item.description,place=place,lesson=self.item,type=Type,author=request.user)
        dashbord.save()
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
class myTask(baseListView):
    template_name = 'ordinance/myTasks.html'
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self, request):
        self.context = {
            'items': self.set_Data(self.set_Objects(request),request)
        }
    def set_Data(self,objects,request):
        for item in objects:
            for task in item.tasks.all():
                if task.student == request.user:
                    item.idAction=task.id
                    item.stan = 'ToAceptRecived'
                    if task.data_recived == True:
                        item.stan = 'ConfirmRecived'
                    if task.rote>0:
                        item.stan = 'rote'
                        item.rote = task.rote
        return objects
    def set_Objects(self,request):
        lesson = Lesson.objects.all()
        lessonNewArray=[];
        for item in lesson:
            if item.classroom == request.user.is_student:
                lessonNewArray.append(item)
        return lessonNewArray
class sentSolution(baseUpdateView):
    success_url = '/'
    template_name = 'ordinance/sentSolution.html'
    getObject = Tasks
    form = TasksSolution
    def setContext(self,request, *args, **kwarg):
        self.context={
            'item':Lesson.objects.get(id=self.kwargs.get("lessonId")),
            'form':self.form
        }
class setRote(baseUpdateView):
    success_url = '/'
    template_name = 'ordinance/sentSolution.html'
    getObject = Tasks
    form = TasksSetRote
    def postSave(self, request, *args, **kwargs):
        self.item.rotedata=datetime.datetime.now()
        self.item.save()
class myRotes(baseListView):
    getObject = Tasks
    template_name = 'ordinance/myrotes.html'
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self,request):
        self.context={
            'items':self.get_object(request),
        }
    def get_object(self,request):
       query=self.getObject.objects.filter(student__email=request.user.email)
       return query
class ShowLesson(baseShowView):
    template_name='ordinance/showlesson.html'
    getObject=Lesson
    def setContext(self,request):
        self.context={
            'context':self.get_object(),
            'students':self.get_students()
        }
    def get_students(self):
        tasks=self.get_object().tasks.all()
        for task in tasks:
            task.status = 'ToAceptRecived'
            if task.data_recived == True:
                task.status= 'ConfirmRecived'
            if  task.taskfile:
                task.status = ''
        return tasks
class sentMess(baseUpdateView):
    success_url = '/ordinance/myStudents/'
    template_name = 'ordinance/sentMess.html'
    getObject = Account
    form = AccountForm
    def post(self,request, *args, **kwargs):
        self.setContext(request)
        self.form = self.setform(request)
        if self.form.is_valid():
            email().sent(self.form.cleaned_data['subject'], self.form.cleaned_data['message'], [self.get_object().email])
            return redirect(self.success_url)
        else:
            self.setContext(request)
            return render(request, self.template_name, self.context)
        return render(request, self.template_name, self.context)
class passwordReset(baseShowView):
    template_name = 'ordinance/showlesson.html'
    success_url = '/ordinance/myStudents/'
    getObject = Account
    def get(self, request, *args, **kwargs):

        password = passwordGeneartor().setPassword()
        print(password)
        item = Account.objects.get(id=self.kwargs.get("id"))
        mess= 'Email : '+item.email+' hasło: '+password
        email().sent('Nowe hasło', mess, [item.email])
        item.set_password(password)
        item.save()
        return redirect(self.success_url)
class ConfirmRecivedLesson(ShowLesson):
    getObject = Lesson
    template_name = 'ordinance/showlesson.html'
    success_url = '/'
    def get(self, request, *args, **kwargs):
        id_ = self.kwargs.get("id")
        task=Tasks(student=request.user,data_recived=True,rote=0)
        task.save()
        myTask=Lesson.objects.get(id=id_)
        myTask.tasks.add(task)
        myTask.save
        return redirect(self.success_url)
class myPersonel(baseListView):
    template_name = 'ordinance/myPersonel.html'
    @login_manager
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def setContext(self, request):
        self.context = {
            'items': Account.objects.filter(is_student__name=request.user.is_educator).order_by('-last_name')
        }

