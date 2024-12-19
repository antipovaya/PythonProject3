from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import  messages
from .forms import UserRegistrationForm, LoginForm, UserEditForm, ProfileEditForm
from .models import Profile


def user_login(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) # Проверяем учетные данные
            if user is not None:
                if user.is_active:           # проверяем активна ли учетка
                    login(request, user)     # Выполняем вход
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'usersapp/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'usersapp/profile.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)  # Создали но пока не сохранили
            new_user.set_password(user_form.cleaned_data['password'])  # установили вывбранный пароль
            new_user.save()  # Сохранили нового пользователя
            # создали профиль для нового пользователя:
            Profile.objects.create(user=new_user)
            return render(request,'usersapp/register_done.html',{'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'usersapp/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'usersapp/pfofile.html',{'user_form': user_form, 'profile_form': profile_form})


def logout_view(request):
    logout(request)
    return redirect('recipesapp/home.html')
# Create your views here.
