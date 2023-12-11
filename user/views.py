from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import User, Student, StudentProfile
from .forms import UserUpdateForm, StudentRegisterForm, StudentProfileForm
from django.conf import settings


def profile_view(request):
    obj = User.objects.get(id=request.user.id)
    return render(request, 'profile.html', {"user": obj})


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email):
            messages.warning(request, 'User Exists with This Email.')
        elif name and phone and email and password:
            user = User(name=name, email=email, phone_number=phone)
            user.set_password(raw_password=password)
            user.save()
            messages.success(request, "Your Request Pending For Approval.")
            redirect('login')
    return render(request, 'register.html')


def student_register(request):
    form = StudentRegisterForm()
    if request.method == "POST":
        form = StudentRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.set_password(form.cleaned_data['password'])
            student.save()
            profile = StudentProfile(student=student)
            profile.save()
            return redirect('login')
        else:
            return render(request, 'student_register.html', {"form": form})

    return render(request, 'student_register.html', {"form": form})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            messages.warning(request, "Invalid Email or Password")
        else:
            login(request, user)
            if user.is_superuser:
                return redirect('admin:index')
            elif user.is_advisor():
                return redirect ("profile")
            elif user.is_student():
                return redirect('student_profile', id = user.id)


    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def complete_profile(request):
    user_form = StudentProfile.objects.get(student=request.user)
    if request.method == "POST":
        form = StudentProfileForm(request.POST, request.FILES, instance=user_form)
        if form.is_valid():
            form.save()
            print(request.FILES)
            return redirect("student_profile", id=request.user.id)  # Redirect to the profile page after successfully saving the form
        else:
            print("form errors:", form.errors)
            print("form non_field_errors:", form.non_field_errors())
    else:
        print("form invalid")
        form = StudentProfileForm(instance=user_form)
    return render(request, 'complete_profile.html', {'form': form})


def student_profile(request, id):
    student = Student.objects.get(id=id)
    profile = StudentProfile.objects.get(student=student)
    return render(request, 'student_profile.html', {'student':student, 'profile': profile})


def user_info_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'update_user.html', {'form': form})


def password_reset(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        if user:
            request.session['user_mail'] = user.email
            return redirect('password_reset_confirm')
        else:
            messages.warning(request, "User Not Found With This Gmail")
    return render(request, 'password_reset.html')


def password_confirm(request):
    if request.method == "POST":
        passwd = request.POST.get('password')
        mail = request.session.get('user_mail')
        user = User.objects.get(email=mail)
        user.set_password(passwd)
        user.save()
        messages.success(request, "password Suceesfully Changed")
        return redirect('login')
    return render(request, 'recover.html')
