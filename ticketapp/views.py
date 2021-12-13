from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import concertModel, locationModel, timefieldModel
from .forms import searchform
from jalali_date import datetime2jalali, date2jalali
from .forms import ConcertForm


def Concert_View (request):
    oursearch= searchform (request.GET)
    if oursearch.is_valid():
        searchtext=oursearch.cleaned_data["searchtext"]
        concert=concertModel.objects.filter(Name__contains=searchtext)
    else:
        concert =concertModel.objects.all()
    return render(request, 'ticketapp/concert.html',{'concert_Model':concert,"searchform":oursearch})


def Location_View (request):
    location =locationModel.objects.all()
    return render(request, 'ticketapp/location_concert.html',{'locationlist':location})


def Detail_Concert_View (request,consert_id):
    detail_concert=concertModel.objects.get(id=consert_id)
    return render (request,'ticketapp/detail_concert.html',{'concertdetails':detail_concert})


def Time_Concert_View (request):
    time =timefieldModel.objects.all()
    return render(request, 'ticketapp/time_concert.html',{'time_Model':time})


def Concert_Edit_View(request,concert_id):
    concert=concertModel.objects.get(pk=concert_id)
    if request.method=="POST":
        concertForm=ConcertForm(request.POST,request.FILES, instance=concert)
        if concertForm.is_valid:
            concertForm.save()
            return redirect("/detail/<int:consert_id>")
    else:
        concertForm=ConcertForm(instance=concert)

    context={

        "concertForm":concertForm,
        "PosterImage":concert.Poster
    }

    return render(request,"ticketapp/concertEdit.html",context)