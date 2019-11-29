from django.contrib import messages
from django.shortcuts import render, redirect

from employee.models import EmployeeDetails


def addEmployee(request):

    return render(request,'emp/empdetails.html')


def saveEmployee(request):
    if request.method == 'POST':
        empid = request.POST.get('empid')
        empname = request.POST.get('empname')
        empmail = request.POST.get('empmail')
        emploc = request.POST.get('emploc')
        empdoj = request.POST.get('empdoj')
        emprol = request.POST.get('emprol')
        empqua = request.POST.get('empqua')
        emprem = request.POST.get('emprem')
        EmployeeDetails(emp_id=empid,emp_name=empname,emp_mail=empmail,emp_location=emploc,emp_doj=empdoj,emp_role=emprol,
                        emp_qualificatiov=empqua,emp_remarks=emprem).save()
        return render(request,'welcome.html',{'message':'Employee Saved Successfully'})
    else:
        return redirect('/employee/employee/')


def viewAllEmp(request):
    emp_obj = EmployeeDetails.objects.all()
    return render(request,'emp/allemp.html',{'data':emp_obj})


def updatEemployee(request):
    emp_id = request.POST.get('empid')
    try:
        emp_obj = EmployeeDetails.objects.get(emp_id=emp_id)
        return render(request,'emp/updateemp.html',{'data':emp_obj})
    except:
        messages.info(request,'Employee not exits')
        return redirect('/employee/updateemp/')


def showDelEmp(request):
    emp_id = request.POST.get('empid')
    try:
        emp_obj = EmployeeDetails.objects.get(emp_id=emp_id)
        return render(request, 'emp/show_del_emp.html', {'data': emp_obj})
    except:
        return redirect('/employee/showdelemp/')


def deletEmpoyee(request):
    emp_id = request.POST.get('empid')
    emp_obj = EmployeeDetails.objects.get(emp_id=emp_id).delete()
    return redirect('/employee/viewallemp/')