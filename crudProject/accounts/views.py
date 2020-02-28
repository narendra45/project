from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import UserRegistrationForm
from accounts.models import RegistrationModel


def signUpView(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:

                firstName = form.cleaned_data['first_name']
                lastName = form.cleaned_data['first_name']
                Email = form.cleaned_data['email_id']
                userName = form.cleaned_data['user_name']
                contactNo = form.cleaned_data['contact_no']
                password = form.cleaned_data['password']
                user = User.objects.create_user(username=userName,password=password, email=Email,
                                                first_name=firstName, last_name=lastName)

                user.save()

                RegistrationModel(contact_no=contactNo,user_id=user.id).save()


                messages.info(request,'REgistered Successfully please please login ')
                return redirect('home')
            except:
                messages.info(request,'phone number or mail already exists ')
                return redirect('register')


    return render(request, 'accounts/registration.html', {'form': form})



def loginCheck(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        try:
            user = auth.authenticate(username=username, password=password)
        except:
            messages.info(request, 'invalid credentials')
            return redirect('/login/')
        else:
            if user is not None:
                auth.login(request, user)

                return redirect('/accounts/home/')
        messages.info(request,'invalid Credentials')
        return redirect('/login/')

    return render(request,'accounts/login.html')



def logout(request):
    auth.logout(request)
    return redirect('home')

