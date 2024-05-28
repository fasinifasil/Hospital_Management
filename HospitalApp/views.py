from django.contrib.auth.models import User, Group
from django.shortcuts import render
from .models import *
# Create your views here.
def IndexPage(request):
    return render(request,'index.html')
def LoginPage(request):
    return render(request,'login.html')
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
