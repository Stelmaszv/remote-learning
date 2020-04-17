from core.baseview import baseCreate;
from django.contrib.auth.forms import UserCreationForm
from core.decorators import login_required
class main(baseCreate):
    success_url = 'auth/accounts/login/'
    template_name = 'mainpage/mian.html'
    form = UserCreationForm
    @login_required
    def get(self, request, *args, **kwargs):
        return self.addGet(request)