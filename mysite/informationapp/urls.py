from django.urls import path
from .views import InfoIndexView, StationCreateView, StationListView, ArduinoSerialView


app_name = 'informationapp'


urlpatterns = [
    path("",InfoIndexView.as_view(), name="info-index"),
    path("arduino/", ArduinoSerialView.as_view(), name="info-arduino"),
    path("stations/", StationListView.as_view(), name="info-list"),
    path("station/create", StationCreateView.as_view(), name="info-create"),
]