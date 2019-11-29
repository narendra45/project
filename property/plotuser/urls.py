from django.urls import path
from django.views.generic import TemplateView

from plotuser import views

urlpatterns = [
    path('adduser/',TemplateView.as_view(template_name='plotuser/adduser.html')),
    path('saveuser/',views.saveUser,name = 'saveuser'),
    path('viewuser/',TemplateView.as_view(template_name='plotuser/viewuser.html')),
    path('viewuserdetails/',views.viewUserDetails,name = 'viewuserdetails'),
    path('showdeluserid/',TemplateView.as_view(template_name='plotuser/viewdeluserid.html'),name='showdeluser'),
    path('showdeluserdetails/',views.showDelUserDetails,name = 'showdeluserdetails'),
    path('conformdeluser/',views.conformDelUser,name = 'conformdeluser')

]