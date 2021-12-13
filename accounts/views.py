from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from .forms import ProfileRegisterForm , ProfileEditForm , UserEditForm
from django.contrib.auth.models import User
from .models import PorfileModel
from accounts.apps import AccountsConfig

def profileRegisterView(request):

    if request.method=="POST":
        profileRegisterForm=ProfileRegisterForm(request.POST,request.FILES)
        if profileRegisterForm.is_valid():

            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                email=profileRegisterForm.cleaned_data['email'],
                                password=profileRegisterForm.cleaned_data['password'],
                                first_name=profileRegisterForm.cleaned_data['first_name'],
                                last_name=profileRegisterForm.cleaned_data['last_name'])

            user.save()

            profileModel=PorfileModel(user=user,
                                       Profleimage=profileRegisterForm.cleaned_data['ProfileImage'],
                                        status=profileRegisterForm.cleaned_data['Gender'],
                                        credit=profileRegisterForm.cleaned_data['Credit'])

            profileModel.save()

            return redirect("/concert")
    else:
        profileRegisterForm=ProfileRegisterForm()

    context={
        "formData":profileRegisterForm
    }
    return render(request,"accounts/profileRegister.html",context)


def Login_View (request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/concert")
        else:
            context={
                "username":username,
                "errorpass":"رمز عبور و یا نام کاربری نامعتبر است "
            }
            return render(request,"accounts/login.html",context)
    return render(request,"accounts/login.html",{})

def Logout_View (request):
        logout(request)
        return redirect("/concert")

def Profile_view (request):
    profile = request.user.profile
    return render(request,"accounts/profile.html",{"profile":profile})


def Profile_Edit_View(request):
    
    if request.method=="POST":
        profileEditForm=ProfileEditForm(request.POST,request.FILES, instance=request.user.profile)
        userEditForm=UserEditForm(request.POST,instance=request.user)
        if profileEditForm.is_valid and userEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return redirect("/accounts/profile")
    else:
        profileEditForm=ProfileEditForm(instance=request.user.profile)
        userEditForm=UserEditForm(instance=request.user)

    context={

        "profileEditForm":profileEditForm,
        "userEditForm":userEditForm,
        "ProfileImage":request.user.profile.Profleimage,
        
    }

    return render(request,"accounts/profileEdit.html",context)

