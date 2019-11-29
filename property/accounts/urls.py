from django.urls import path

from accounts import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path('signin/', views.signIn, name='signin'),
    path('login/',views.logIn,name = 'login'),
    path("logout/",views.logout,name="logout"),
    path('change_password/', views.change_Password, name='change_password'),

]