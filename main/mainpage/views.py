from core.baseview import baseListView
from ordinance.models import Lesson
from django.contrib.auth.forms import UserCreationForm
from core.decorators import login_required
from authorization.models import Account
class main(baseListView):
    success_url = 'auth/accounts/login/'
    template_name = 'mainpage/mian.html'
    def setContext(self, request):
        self.context ={
            'list':self.reutn_Objects(request)
        }
    def reutn_Objects(self,request):
        list=Lesson.objects.all()
        for item in list:
            item.if_Recived=self.if_Recived(request,item);
        return list
    def if_Recived(self,request,object):
        tasks = object.tasks.all()
        for task in tasks:
            if task.student.id == request.user.id:
                return True;
        return False;