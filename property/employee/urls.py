from django.urls import path

from employee import views

urlpatterns = [
    path('addemp/',views.addEmployee,name = 'addemp'),
    path('saveemp/',views.saveEmployee,name = 'saveemp'),
    path('viewallemp/',views.viewAllEmp,name = 'viewallemp'),
    path('updateemp/',views.updatEemployee,name='updateemp'),
    path('showdelemp/',views.showDelEmp,name = 'showdelemp'),
    path('deletemp/',views.deletEmpoyee,name='deletemp'),
]