from django.contrib import messages
from django.shortcuts import render, redirect

from plotuser.models import PlotUser


def saveUser(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        username = request.POST.get('username')
        number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        PlotUser(user_id=userid,user_name=username,user_cont_no=number,user_mail=email,user_address=address).save()
        return render(request,'welcome.html',{'message':'user added Successfully'})
    else:
        return redirect('/plotuser/adduser/')


def viewUserDetails(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        try:
            details = PlotUser.objects.get(user_id=userid)
            return render(request,'plotuser/viewuserdetails.html',{'data':details})
        except:
            messages.info(request, 'User not exists')
            return redirect('/plotuser/viewuser/')



def showDelUserDetails(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        try:
            details = PlotUser.objects.get(user_id=userid)
            return render(request, 'plotuser/viewdeluserdetails.html', {'data': details})
        except:
            messages.info(request, 'User not exists')
            return redirect('/plotuser/showdeluserid/')
    else:
        return redirect('/plotuser/showdeluserid/')


def conformDelUser(request):
    user_id = request.POST.get('empid')
    user_obj = PlotUser.objects.get(user_id=user_id).delete()
    return redirect('/welcome/')
