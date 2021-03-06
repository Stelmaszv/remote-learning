from django.shortcuts import redirect
def login_required(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if args[1].user.is_anonymous:
            print(args[1])
            return redirect('auth/accounts/login/')
        return value
    return wrapper
def not_login(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if args[1].user.is_authenticated:
            return redirect('/')
        return value
    return wrapper
def login_manager(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if args[1].user.type.name !='manager':
            return redirect('/')
        return value
    return wrapper
def login_educator(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if args[1].user.type.name !='educator':
            return redirect('/')
        return value
    return wrapper