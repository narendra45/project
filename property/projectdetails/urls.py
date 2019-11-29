from django.urls import path
from django.views.generic import TemplateView

from projectdetails import views

urlpatterns = [
    #plot urls
    path('new_plot/',views.newPlot,name = 'new_plot'),
    path('saveplot/',views.savePlot,name = 'saveplot',),
    path('editplot/',views.editPlot,name = 'editplot'),
    path('updateplot/',views.updatePlot,name = 'updateplot'),
    path('viewplot/',views.viewPlot,name = 'viewplot'),
    path('viewall/',views.viewAll,),
    path('viewalldetails/',views.viewAllDetails,name = 'viewalldetails'),
    #Appartment urls
    path('new_appment/',TemplateView.as_view(template_name='appartment/newappart.html')),
    path('saveappartment/',views.saveAppartment,name ='saveappartment'),
    path('view_appment/', TemplateView.as_view(template_name='appartment/viewappno.html')),
    path('viewappdetails/',views.viewAppDetails,name = 'viewappdetails'),
    path('view_all_appment/',views.viewAllAppments,name ='view_all_appment'),

]