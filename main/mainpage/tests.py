from django.test import SimpleTestCase
from django.urls import reverse,resolve
from mainpage.views import main
from authorization.models import Account
from django.test import TransactionTestCase
class Main_Page_Test(TransactionTestCase):
    def test_main_page_url(self):
        url= reverse('main')
        self.assertEquals(resolve(url).func.view_class,main)
    def test_login_main_page(self):
        self._create_User()
        response = self.client.post('/auth/accounts/login', self.data, follow=True)
        self.assertTrue(response.context['user'].is_active)
    def _create_User(self):
        self.data = {
            'email'   : 'test@email.com',
            'password': 'secret',
        }
        Account.object.create_user(email='test@email.com',password='secret',username='test')