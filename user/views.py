from django.shortcuts import render , redirect
from .forms import UserCreationForm , LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout


def register(request):
    if request.method == 'POST' :
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid :
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password1'])
            new_user.save()
            messages.success(
                request, f'تهانينا {new_user.username} لقد تمت عملية التسجيل بنجاح'
            )
            return redirect('home')
    else :
            register_form = UserCreationForm()


    context = {
        'title' : 'Sign-Up' ,
        'register_form' : register_form ,
    }
    return render(request,'user/register.html',context)

def user_login(request):
    if request.method == 'POST' :
        loginform = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        h = authenticate(request,username=username,password=password)
        if h is not None :
            login(request , h)
            return redirect('home')
        else :
            messages.warning('there is an erreur in username or password')
    else :
        loginform = LoginForm()
    context = {
        'title' : 'Log-in', 
        'loginform' : loginform
    }
        
    return render(request , 'user/login.html',context )

def user_logout(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'Log Out',
    })
    

        