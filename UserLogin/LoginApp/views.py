from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()
from django.contrib import messages

import json
# Create your views here.
def home(request):
    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        authUser = authenticate(
            username=username,
            password=password
        )
        if authUser is not None:
            login(request, authUser)
            return render(request, 'home.html')
        else:
            messages.error(request, 'Invalid Credentials')
        return render(request, 'login.html')
    return render(request, 'home.html')


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        authUser = authenticate(
            username=username,
            password=password
        )
        if authUser is not None:
            login(request, authUser)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
        return render(request, 'login.html')
    return render(request, 'login.html')


def register(request, json=None):
    u = User()
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        comapany_name = request.POST.get('comapany_name')
        company_role = request.POST.get('company_role')
        country = request.POST.get('country')
        PHI = request.POST.get('PHI')
        application_name=request.POST.get('application_name')
        contact_Name = request.POST.get('contact_Name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        consent = request.POST.get('consent')
        print(email)

        data = {"Company Name": "comapany_name",
                "Company Role": "company_role",
                "Country": "country",
                "Where will PHI be stored (country)": "PHI",
                "Application Name": "application_name",
                "Contact Name": "contact_Name",
                "Phone": "phone",
                "Email": "Email",
                "Password": "password",
                "Consent": "consent"
                }
        out_file = open("user.json", "w")
        json.dump(data, out_file, indent=6)
        out_file.close()

        # json_formatted_str = json.dumps(data)
        # with open("user.json", "w") as f:
        #     f.write(json_formatted_str)

        createNewUser = User.objects.create_user(
            username=comapany_name,
            company_role=company_role,
            country=country,
            PHI=PHI,
            application_name=application_name,
            contact_Name=contact_Name,
            email=email,
            phone=phone,
            password=password,
            consent=consent

        )

        createNewUser.save()

        return redirect('/')

    return render(request, 'register.html')


def logoutView(request):
    logout(request)
    return redirect('/')


def changePassword(request):
    if request.user.is_authenticated:
        username = request.user.username
        if request.method == 'POST':
            newpassword = request.POST.get('password')
            u = User.objects.get(username=username)
            u.set_password(newpassword)
            u.save()
            messages.success(request, 'Password Chnaged Please login with new password')
            return render(request, 'login.html')

    return render(request, 'chnagepassword.html')


