from django.urls import include, path
from django.contrib import admin
from djapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',views.registration_view),
    path('',views.Login_View),
    path('home/',views.home_view),
    path('contact/',views.contact_view),
    path('services/',views.services_view),
    path('feedback/',views.feedback_view),
    path('gallery/',views.gallery_view)
]
