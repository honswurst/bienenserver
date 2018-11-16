from .models import Hive
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime


def index(request):
    all_hives = Hive.objects.all()
    context = {
        "all_hives": all_hives,
    }
    return render(request, "daten/index.html", context)


def detail(request, hive_name):
    '''try:
        hive = Hive.objects.get(name=hive_name)
    except Hive.DoesNotExist:
        raise Http404("Diesen Stocknamen gibt es nicht")
    '''

    hive = get_object_or_404(Hive, name= hive_name)
    return render(request, "daten/detail.html", {"hive" : hive})

def measure(request, hive_name):
    try:
        hive = Hive.objects.get(name=hive_name)
    except Hive.DoesNotExist:
        raise Http404("Diesen Stocknamen gibt es nicht")

    now = datetime.datetime.now()
    pressure = int(request.GET["p"])
    weight = int(request.GET["w"])
    temperature = int(request.GET["t"])

    hive.measurement_set.create(day=now.day, month=now.month, year=now.year, pressure=pressure, weight=weight, temperature=temperature)

    response = HttpResponse("got: " + str(pressure) + ", " + str(weight) + ", " + str(temperature) + " and saved it to the db")
    return response