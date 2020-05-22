from core.baseview import baseListView
from ordinance.models import Lesson,Dashbord
from django.shortcuts import redirect
class abstractMain():
    list=[]
    dasbord = Dashbord.objects.all()
    def show(self,request) -> list:
        pass
    def basic_Show(self,request)-> list:
        for item in self.dasbord:
            if request.user.type.name==item.place.name \
                    or item.place.name=='all' \
                    or item.author==request.user:
                self.list.append(item)
        return self.list;
class educator(abstractMain):
    def show(self,request) -> abstractMain:
        return self.basic_Show(request)
class studnet(abstractMain):
    def show(self,request) -> list:
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
    def show(self,request) -> abstractMain:
        return self.basic_Show(request);
class manager(abstractMain):
    def show(self,request) -> Dashbord:
        return Dashbord.objects.all();
class main(baseListView):
    template_name = 'mainpage/mian.html'
    def setContext(self, request) -> None:
        self.context ={
            'list':self.return_Objects(request)
        }
    def get(self, request, *args, **kwargs) -> baseListView:
        if request.user.is_anonymous:
            self.context={}
            return redirect('auth/accounts/login/')
        return self.addGet(request)
    def return_Objects(self,request) -> abstractMain:
        views={'educator' : educator,'student': studnet,'teacher':teacher,'manager' :manager}
        redirect('/auth/accounts/login/')
        view=views[request.user.type.name]
        return  view().show(request)
