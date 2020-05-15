from django.test import SimpleTestCase
from django.test import TransactionTestCase
from django.urls import reverse,resolve
from ordinance.views import add_Student
class ordinance_Test(TransactionTestCase):
    def test_add_Student_url(self):
        url= reverse('mainpage:add_Student')
        self.assertEquals(resolve(url).func.view_class,add_Student)
    def test_add_Student_templete(self):
        respanse= self.client.get(reverse('main:add_Student'))
        self.asssertEquels(respanse.status_code,200)
        self.assertTemplateUsed(respanse,'ordinance/addperson.html')
    def test_sentMess_post(self):
        respanse= self.client.post(reverse('main:sentMess',args=[1]),{
            'subject' :'test',
            'message' : 'test message'
        })
        self.asssertEquels(respanse.status_code, 302)

