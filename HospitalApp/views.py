from django.contrib.auth.models import User, Group
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from .models import *
# Create your views here.
def IndexPage(request):
    return render(request,'index.html')
def LoginPage(request):
    error = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            error = "Invalid email or password."
    return render(request, 'login.html', {'error': error})
def AboutPage(request):
    return render(request,'about.html')

def CreateAccountPage(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        dob = request.POST['dob']
        blood = request.POST['blood']
        try:
            if password == confirmPassword:
                PatientModel.objects.create(Name=name, Email=email, Gender=gender, PhoneNumber=phone,
                                            Address=address, BirthDate=dob, bloodGroup=blood)
                user = User.objects.create_user(first_name=name, email=email, password=password, username=email)
                Patient_Group = Group.objects.get(name='Patient')
                Patient_Group.user_set.add(user)
                error = 'no'
            else:
                error = 'yes'
        except Exception as e:
            error = 'yes'
    return render(request, 'createaccount.html', {'error': error})
def LogoutFunction(request):
    logout(request)
    return redirect('login')

def Home(request):
    if not request.user.is_active:
        return redirect('login')
    user1 = request.user.groups.all()[0].name
    if user1=='Patient':
        return render(request,'patienthome.html')
def Profile(request):
    if not request.user.is_active:
        return redirect('login')
    user1 = request.user.groups.all()[0].name
    if user1 == 'Patient':
        patient_details = PatientModel.objects.all().filter(Email=request.user)
        context ={'patientDetails':patient_details}

        return render(request, 'pateintprofile.html',context)

