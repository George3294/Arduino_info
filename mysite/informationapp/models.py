from django.db import models
from django.utils import timezone
# Create your models here.

class Station(models.Model):
    """
    Модель Station представялет иноформацию
    о станции и анализировать эти данные
    """
    objects = None
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    temperature_info = models.IntegerField(default=0)
    data_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Station'
        
class Arduino(models.Model):
    """
    Модель Arduino предоставляет информацию о состоянии 
    темперартуры на станции
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    station  = models.ForeignKey(Station, on_delete=models.CASCADE)
    temperature_info  = models.IntegerField(default=0)
    update_data = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = 'Arduino'