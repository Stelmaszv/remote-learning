from core.baseview import baseCreate;
from django.contrib.auth.forms import UserCreationForm
from core.decorators import not_login
class register(baseCreate):
    success_url = '/accounts/login/'
    template_name = 'registeration/register.html'
    form = UserCreationForm
    @not_login
    def get(self, request, *args, **kwargs):
        return self.addGet(request)