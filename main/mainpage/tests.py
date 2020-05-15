from django.test import SimpleTestCase
from django.urls import reverse,resolve
from mainpage.views import main
from authorization.models import Account
from django.test import TransactionTestCase
class Main_Page_Test(TransactionTestCase):
    def test_main_page_url(self):
        url= reverse('main')
        self.assertEquals(resolve(url).func.view_class,main)
    def test_mian_page_templete(self):
        respanse= self.client.get(reverse('main'))
        self.asssertEquels(respanse.status_code,200)
        self.assertTemplateUsed(respanse,'mainpage/mian.html')
