from core.baseview import baseListView
from ordinance.models import Lesson,Dashbord
from django.shortcuts import redirect
from core.decorators import login_required
class main(baseListView):
    template_name = 'mainpage/mian.html'
    def setContext(self, request):
        self.context ={
            'list':self.return_Objects(request)
        }
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def return_Objects(self,request):
        views={'educator' : educator,'student': studnet,'teacher':teacher,'manager' :manager}
        view=views[request.user.type.name]
        return  view().show(request)
class abstractMain():
    list=[]
    dasbord = Dashbord.objects.all()
    def show(self,request):
        pass
    def basic_Show(self,request):
        for item in self.dasbord:
            if request.user.type.name==item.place.name \
                    or item.place.name=='all' \
                    or item.author==request.user:
                self.list.append(item)
        return self.list;
class educator(abstractMain):
    def show(self,request):
        return self.basic_Show(request)
class studnet(abstractMain):
    def show(self,request):
        for item in self.dasbord:
            if request.user.type.name==item.place.name \
                    and self.if_in_class(request, item)\
                    and item.type.name=='lesson' \
                    or item.type.name=='normal':
                self.list.append(item)
        return  self.list
    def if_in_class(self,request,object):
        if object.lesson:
            if object.lesson.classroom==request.user.is_student:
                return True
            return False
        return False
class teacher(abstractMain):
    def show(self,request):
        return self.basic_Show(request);
class manager(abstractMain):
    def show(self,request):
        return Dashbord.objects.all();