from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.db import models

import json

from input.models import *


from django.core.serializers import serialize

import codecs



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def upload(request):
    
    if request.method =='POST':
        data_body = request.body
        print("\n")
        print(data_body)
        print("\n")
        data_json = codecs.decode(data_body, 'UTF-8')
        print(data_json)
        json_data = json.loads(data_json)
        device_obj =Moisture_sensor_device.objects.filter(Serial_number = json_data['ID'])
        if  not len(device_obj):

                
                new_device = Moisture_sensor_device(Serial_number = json_data['ID'])
                new_device.save()
        update = Moisture_sensor_update(#Device_Serial_number= device_obj[0] ,
                                        #Device_Name=json_data['Device_name'], 
                                        #UVC_time=json_data['UVC_time'],
                                        #Fan_speed=json_data['Fan_speed'],
                                        #Report_date=json_data['Report_date'],
                                        #Local_IP=json_data['Local_IP']
                                        
                                        Device_Serial_number = device_obj[0],

                                        Moisture_level = json_data['moisture'],
                                        Report_date = json_data['date']


                                        )
        update.save()
        return HttpResponse("update saved")
    
        
        
        
    if request.method == 'GET':
        return HttpResponse("input/upload reached")
