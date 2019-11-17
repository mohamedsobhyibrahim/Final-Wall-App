from django.shortcuts import render,redirect
from .forms import UserCreationForm,LogiForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.models import post
from django.core.mail import send_mail

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            #username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()


            user_email = form.cleaned_data['email']

            send_mail(
                'The Wall App' ,
                 'Congratulations your registered success',
                 'wallapp20@gmail.com',
                 [user_email], 
                 fail_silently=False
            )


            # messages.success(
          
            messages.success(
                request, f'Congratulations {new_user} your registerd success')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title': 'register',
        'form': form,
    })

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.warning(
                request, 'Wrong username or password')

    return render(request, 'user/login.html', {
        'title': 'login ',
    })

def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'logout'
    })

def profile(request):
    posts = post.objects.filter(author=request.user)
    return render(request,'user/profile.html',{
        'title':'profile',
        'posts':posts,
    })




