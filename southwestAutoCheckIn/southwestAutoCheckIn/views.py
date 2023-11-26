from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import FlightReservation


def index(request):
    return render(request, 'index.html')


def checkIn(request):
    confirmation_number = request.POST.get("confirmationNumber")
    first_name = request.POST.get("firstName")
    last_name = request.POST.get("lastName")
    flight_time = request.POST.get("flight_time")
    phone_number = request.POST.get("phoneNumber")
    compliance = request.POST.get("compliance")
    
    reservation = FlightReservation(
        confirmation_code=confirmation_number,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        flight_time=flight_time,
    )

    reservation.save()

    context = {
        'confirmation_number': confirmation_number,
        'first_name': first_name,
        'last_name': last_name,
        'compliance': compliance,
        'flight_time': flight_time,
    }
    return render(request, 'check_in.html', context)
    
    