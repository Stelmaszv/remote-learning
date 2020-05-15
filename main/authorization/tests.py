from django.test import TransactionTestCase
from authorization.models import Account
class Auth_Test(TransactionTestCase):
    def test_login(self):
        self._create_User()
        respane= self.client.post('/auth/accounts/login', self.data, follow=True)
        self.assertFalse(respane)
    def _create_User(self):
        self.data = {
            'email'   : 'test@gmail.com',
            'password': '123',
        }
        Account.object.create_user(
            email=Account.object.normalize_email('test@gmail.com'),
            password='123',
            username='313'
        )
        Account.object.create_user(email='test@email.com',password='secret',username='test')