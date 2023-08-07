from django.db import models

# Create your models here.

class Moisture_sensor_device(models.Model):
    
    Serial_number = models.IntegerField(primary_key=True)
    


class Moisture_sensor_update(models.Model):
    
    Device_Serial_number = models.ForeignKey(Moisture_sensor_device, on_delete=models.CASCADE)
    
    Moisture_level = models.IntegerField()
    Report_date = models.DateTimeField(auto_now=False, auto_now_add=False)
