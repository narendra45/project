from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/",views.login, name="login"),
    path("verify/",views.verifyuser, name='verify'),
    path("logout/",views.logout,name="logout"),
    path("newcredentials/",TemplateView.as_view(template_name='addcr.html'),name='newcredentials'),
    path('addcr/',views.addcr,name='addcr'),
    path('viewcr/',views.viewCr,name='viewcr'),
    path('updatecr/',views.updateCredentials,name='updatecr'),
    path('saveupdatecr/',views.saveUpdateCredentials,name='updatecr'),
    path('deletecr/',views.deleteCredentials,name='deletecr'),
    path("viewdetails/",views.viewDetails,name='viewsetails'),
    path("updatedetails/",views.updateDetails,name='updatedetails'),
    path('saveupdatedetails/',views.saveUpdateDetails,name='saveUpdatedetails'),

    ]
