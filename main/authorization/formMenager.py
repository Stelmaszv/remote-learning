from .forms import educator
import random
class authorizationForm:
    def __init__(self,request):
        self.request=request
    def return_object(self) -> educator:
        return  educator()
class passwordGeneartor:
    def setPassword(self) -> str :
        passwordString=''
        randomNumber='0123456789'
        randomString='QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKklLMmNnBbVvCcXxZz'
        randomSpecjial='!@#$%^&*()_+{}:"|<>?|'
        randomStringArray=[]
        randomNumberArray=[]
        randomSpecjialArray=[]
        password=[]
        for string in randomString:
            randomStringArray.append(string)
        for number in randomNumber:
            randomNumberArray.append(number)
        for specjial in randomSpecjial:
            randomSpecjialArray.append(specjial)
        letters=random.sample(randomStringArray, 8)
        numbers = random.sample(randomNumberArray, 3)
        specjials = random.sample(randomSpecjialArray, 2)
        for leter in letters:
            password.append(leter)
        for number in numbers:
            password.append(number )
        for specjial in specjials:
            password.append(specjial)
        for password in password:
            passwordString += password
        return passwordString




