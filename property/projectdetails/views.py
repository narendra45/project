from django.contrib import messages
from django.shortcuts import render, redirect
from projectdetails.models import PlotDetails, AppartmentDetails


def newPlot(request):

    return render(request,'plotdata/newplot.html')


def savePlot(request):
    if request.method == 'POST':
        plot_no = request.POST.get('plotno')
        plot_img = request.FILES['plotimg']
        road_no = request.POST.get('roadno')
        survey_no = request.POST.get('surveyno')
        cost_per_sqr = request.POST.get('costpersqd')
        other_exp = request.POST.get('otherexp')
        boundaries = request.POST.get('boundaries')
        face = request.POST.get('face')
        status = request.POST.get('status')
        total_cost = request.POST.get('tcost')
        PlotDetails(plot_no=plot_no, plot_image=plot_img, road_no=road_no, survey_no=survey_no,
                    cost_per_sqd=cost_per_sqr, other_exp=other_exp, boundaries=boundaries, facing=face, status=status,
                    Total_cost=total_cost).save()
        return render(request, 'welcome.html', {'message': 'Plot Details added successfully'})


def editPlot(request):

    return render(request,'plotdata/editplot.html')


def updatePlot(request):
    plot_id =request.GET.get('plotno')
    try:
        plot_data = PlotDetails.objects.get(plot_no=plot_id)
        return render(request,'plotdata/update.html',{'data':plot_data})
    except:
        messages.info(request,'Plot Details not Exists')
        return redirect('/projectdetails/editplot/')


def viewPlot(request):
    return render(request, 'plotdata/viewplot.html')


def viewAll(request):
    plot_id = request.POST.get('plotno')
    try:
        plot_data = PlotDetails.objects.get(plot_no=plot_id)

        return render(request, '/plotdata/viewall.html', {'data': plot_data})
    except:
        messages.info(request,'Plot Details are Not Exist')
        return redirect('/projectdetails/viewplot')


def viewAllDetails(request):
    plot_id = request.GET.get('plot_no')
    plot_data = PlotDetails.objects.get(plot_no=plot_id)

    return render(request, 'plotdata/viewalldata.html', {'data': plot_data})




#apptype appno appimage apparea appfloortype appage appcost otherexp facing status tcost

def saveAppartment(request):
    if request.method == 'POST':
        app_type = request.POST.get('apptype')
        app_no = request.POST.get('appno')
        app_img = request.FILES['appimg']
        app_area = request.POST.get('apparea')
        app_floor_type = request.POST.get('appfloortype')
        app_age = request.POST.get('appage')
        app_cost = request.POST.get('appcost')
        app_other_exp = request.POST.get('otherexp')
        app_facing = request.POST.get('face')
        app_status = request.POST.get('status')
        app_tcost = request.POST.get('tcost')
        AppartmentDetails(app_type=app_type,app_no=app_no,app_image=app_img,app_area=app_area,app_floor_type=app_floor_type,app_age=app_age,
                          app_cost=app_cost,other_exp=app_other_exp,facing=app_facing,status=app_status,total_cost=app_tcost).save()
        return render(request,'welcome.html',{'message':'appartment Detalis are saved'})
    else:
        return redirect('/projectdetails/new_appment/')


def viewAppDetails(request):
    if request.method == 'POST':
        appid = request.POST.get('appid')
        print(appid)
        try:
            appObj = AppartmentDetails.objects.get(app_no=appid)
            print(appObj)
            return render(request,'appartment/viewappdetails.html',{'data':appObj})
        except:
            messages.info(request,'Appartment Details not available')
            return redirect('/projectdetails/view_appment/')
    else:
        return redirect('/projectdetails/view_appment/')


def viewAllAppments(request):
    app_Obj = AppartmentDetails.objects.all()

    return render(request,'appartment/viewallapp.html',{'appdata':app_Obj})