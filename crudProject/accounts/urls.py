from django.urls import path
from django.views.generic import TemplateView

from accounts import views

urlpatterns = [
    path('home/',TemplateView.as_view(template_name='accounts/index.html'),name='home'),
    path('register/',views.signUpView,name = 'register'),
    path('login/',views.loginCheck,name='login'),
    path("logout/",views.logout,name="logout"),

]