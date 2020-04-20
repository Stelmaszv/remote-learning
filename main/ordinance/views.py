from core.baseview import baseCreate;
from core.decorators import login_required
from authorization.forms import educator
from authorization.models import Account
from authorization.formMenager import passwordGeneartor
from django.core.mail import send_mail
class add_person(baseCreate):
    template_name = 'ordinance/addperson.html'
    success_url = '/'
    form=educator
    getObject = Account
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)
    def postSave(self, request, *args, **kwargs):
        password=passwordGeneartor().setPassword()
        print(password)
        item = Account.objects.latest('id')
        item.username = self.form.cleaned_data['first_name'] + ' ' + self.form.cleaned_data['last_name']
        item.is_student = request.user.is_educator
        item.set_password(password)
        item.staff = True
        item.save()
        send_mail('Dane do konta', 'kotek', 'stelmaszv@gmail.com',['zupartl@johnderasia.com'],fail_silently=False)

