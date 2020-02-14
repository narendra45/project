from django.shortcuts import render,redirect
from djapp.forms import RegistrationForm,LoginForm,FeedbackForm
from django.http.response import HttpResponse
from djapp.models import RegistrationData,FeedbackData

def registration_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            uname = request.POST.get('user_name')
            pwd = request.POST.get('password')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            data = RegistrationData(
                first_name=fname,
                last_name=lname,
                user_name=uname,
                password=pwd,
                mobile=mobile,
                email=email
            )
            data.save()
            rform = RegistrationForm()
            return render(request, 'reg.html', {'xyz': rform})
        else:
            return HttpResponse('USer Invalid Data')
    else:
        rform = RegistrationForm()
        return render(request,'reg.html',{'xyz':rform})

def Login_View(request):
    if request.method =="POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('user_name')
            pwd = request.POST.get('password')

            user = RegistrationData.objects.filter(user_name=uname)
            password = RegistrationData.objects.filter(password=pwd)

            if user and password:
                return redirect('/home/')
                # return HttpResponse("Success")
            else:
                return HttpResponse("Fail")
        else:
            return HttpResponse('User Invalid Data')
    else:
        lform = LoginForm()
        return render(request,'logindata.html',{'lform':lform})


def home_view(request):
    return render(request,'project_home.html')

from djapp.forms import ContactForm
from djapp.models import ContactData

def contact_view(request):
    if request.method =="POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')

            courses = cform.cleaned_data.get('courses')
            trainers = cform.cleaned_data.get('trainers')
            branches = cform.cleaned_data.get('branches')
            date = cform.cleaned_data.get('date')
            gender = cform.cleaned_data.get('gender')
            data = ContactData(
                name=name,
                mobile=mobile,
                email=email,
                courses=courses,
                trainers=trainers,
                branches=branches,
                date=date,
                gender=gender
            )
            data.save()
            cform = ContactForm()
            return render(request,'project_contact.html',{'cform':cform})
        else:
            return HttpResponse('User Invalid Data')
    else:
        cform = ContactForm()
        return render(request,'project_contact.html',{'cform':cform})




from djapp.models import CoursesData
def services_view(request):
    courses = CoursesData.objects.all()
    return render(request,'project_services.html',{'courses':courses})




import  datetime as dt
date1 = dt.datetime.now()
def feedback_view(request):
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date = date1
            )
            data.save()
            fform = FeedbackForm()
            data = FeedbackData.objects.all()
            return render(request,'project_feedback.html',{'fform':fform,'data':data})
        else:
            return HttpResponse("User Missed Some Values")
    else:
        data = FeedbackData.objects.all()
        fform = FeedbackForm()
        return render(request,'project_feedback.html',{'fform':fform,'data':data})







def gallery_view(request):
    return render(request,'project_gallery.html')