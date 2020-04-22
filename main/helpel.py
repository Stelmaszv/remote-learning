from django.core.mail import send_mail
class email:
    def sent(self,subject,content,adress):
        print('email')
        #send_mail(subject, content, 'stelmaszv@gmail.com', adress)