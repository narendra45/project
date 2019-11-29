import random

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.models import Otp, Credentials
from twilio.rest import Client

from task import settings


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        contact = request.POST['phoneno']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                userotp = Otp(user_id=user.id, contact=contact)
                userotp.save()
                return redirect('login')

        else:
            messages.info(request, 'password not matching..')
            return redirect('register')

    else:
        return render(request, 'account/register.html')


def verifyuser(request):

    otp = request.POST.get('otp')
    username=request.POST.get('username')
    password=request.POST.get('password')
    me = User.objects.get(username=username)
    userotp = Otp.objects.get(user_id=me.pk,otp=otp)
    userotp.otp_verified=True
    userotp.save()
    if userotp is not None:
        if userotp.otp_verified==True:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                userotp.otp_verified=False
                userotp.save()
                return redirect('welcome')
            else:
                return render(request, 'account/login.html', {'message': 'invalid Otp'})
        else:
            return render(request,'account/login.html',{'message':'invalid Credentials'})
    else:
        return render(request,'account/login.html',{'message':'invalid otp please login again'})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username, password=password)
        except:
            messages.info(request, 'invalid credentials')
            return redirect('/accounts/login/')
        else:
            if user is not None:
                userotp = Otp.objects.get(user_id=user.id)
                otp = random.randint(1000, 9999)
                userotp.otp = str(otp)
                userotp.save()
                #SENDING OTP TO MOBILE BY USING TWILIO DEFAULT CODE
                '''contact_no='+91' + str(userotp.contact)
                account_sid = 'ACbc8a49aef33aa0b3f8afff2a7ee8354e'
                auth_token = 'dff2f5884c63f4b14c7e40edf98556a6'
                client = Client(account_sid, auth_token)
                message = client.messages \
                    .create(
                    body="you otp" + str(otp),
                    from_='+12054489653',
                    to=contact_no
                )
                print(message.sid)
                '''
                # SENDING OTP TO EMAIL
                mail_body = '<h1>Welcome to our Application!!!</h1>'
                mail_body += 'Please Enter on below link to verify your email account !!!<br /><br /><hr />'
                mail_body += str(otp)
                mail_obj = EmailMessage("Please Verify Your Otp",
                                        mail_body, settings.EMAIL_HOST_USER, [user.email])
                mail_obj.content_subtype = 'html'
                mail_obj.send()

                return render(request, 'account/veriftotp.html',{'user':{'username':username,'password':password}})
            else:
                return render(request, 'account/login.html')

    else:
        return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('welcome')

def addcr(request):
    if request.method=='POST':
        crnamae=request.POST.get('crname')
        crid=request.POST.get('crid')
        userid=request.POST.get('userid')
        user=User.objects.get(id=userid)
        Credentials(credential_name=crnamae,credential=crid,user=user).save()
        return render(request,'welcome.html',{'message':'Credentials are Added Successfully'})
    else:
        return redirect('/addcr/')

def viewCr(request):
    userid = request.GET.get('idno')
    print(userid)
    credentialsObj=Credentials.objects.filter(user=userid)
    print(credentialsObj)
    return render(request,'viewallcr.html',{'data':credentialsObj})

def updateCredentials(request):
    credentialid = request.GET.get('idno')
    print(credentialid)
    credentialsObj = Credentials.objects.get(id=credentialid)
    return render(request,'saveupdatecr.html',{'data':credentialsObj})

def saveUpdateCredentials(request):
    if request.method=='POST':
        crnamae=request.POST.get('crname')
        credential=request.POST.get('cred')
        creid=request.POST.get('crid')
        credentialsObj = Credentials.objects.get(id=creid)
        credentialsObj.credential_name=crnamae
        credentialsObj.credential=credential
        credentialsObj.save()
        remainCr=Credentials.objects.filter(user=credentialsObj.user)

        return render(request,'viewallcr.html',{'data':remainCr,'message':'Credentials are updated Successfully'})
    else:
        return redirect('/viewcr/')


def deleteCredentials(request):
    idno=request.GET['idno']
    Credentials.objects.get(id=idno).delete()
    return render(request,'viewallcr.html',{'message':'Credentials are deleted successfully'})



def viewDetails(request):
    idno=request.GET.get('idno')
    viewCredentials = Otp.objects.get(user=idno)
    return render(request,'viewall.html',{'info':viewCredentials})


def updateDetails(request):
    idno = request.GET.get('idno')
    Credentials = Otp.objects.get(user=idno)
    return render(request, 'update.html', {'info': Credentials})


def saveUpdateDetails(request):
    if request.method == 'POST':
        id=request.POST['userid']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        userobj = User.objects.get(id=id)
        userobj.first_name=first_name
        userobj.last_name=last_name
        userobj.save()
        return render(request,'welcome.html',{'message':'Credentials Updated successfully'})
    else:
        return redirect('welcome')