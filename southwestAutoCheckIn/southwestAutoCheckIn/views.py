from django.shortcuts import render
from django.http import Http404, HttpResponse



def index(request):
    return render(request, 'index.html')


def checkIn(request):
    confirmation_number = request.POST.get("confirmationNumber")
    first_name = request.POST.get("firstName")
    last_name = request.POST.get("lastName")
    flight_time = request.POST.get("flight_time")
    compliance = request.POST.get("compliance")
    

    context = {
        'confirmation_number': confirmation_number,
        'first_name': first_name,
        'last_name': last_name,
        'compliance': compliance,
        'flight_time': flight_time,
    }
    return render(request, 'check_in.html', context)
    
    