from timeit import default_timer
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
import datetime
import serial
import time
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView, CreateView
import serial 
from .forms import StationForm
from .models import Station

# Create your views here.

class ArduinoSerialView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        serial_port = 'COM4'
        serial_baud  =  9600
        files = "output.txt"
        ser = serial.Serial(serial_port,serial_baud)
        while True:
            line = ser.readline()
            line = line.decode('utf-8')
            print(line)
            with open(files, 'w') as file:
                file.write(line)
        with open("output.txt", "r") as file:
            for line in file:               
                return render(request, 'informationapp/info-arduino.html', line=line)

class InfoIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        stations = [
            ('Новая НС', 28),
            ('Аткарск', 30),
            ('Саратов-1', 28),
        ]
        context = {
            'stations': stations,
        }
        return render(request, 'informationapp/info-index.html', context=context)
    

class StationListView(ListView):
    template_name = "informationapp/info-list.html"
    context_object_name = "stations"
    queryset = Station.objects.all()
    
def station_create(self, request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("informationapp/info-list.html")
            return redirect(url)
    else:
        form = StationForm()
    context = {
        "form": form,
    }
    return render(request, "informationapp/info-create.html", context=context)

class StationCreateView(CreateView):
    model = Station
    fields = "name", "temperature_info"
    template_name = 'informationapp/info-create.html'
    success_url = reverse_lazy("informationapp:info-create")
    
    
#def receive_arduino_data(request):
#    try:
#        sensor_data = SensorData=received_value()
#        sensor_data.save()
#        return HttpResponse("Даные приняты")
#    except Exception as e:
#        return HttpResponse("Ошибка данные не приянты")