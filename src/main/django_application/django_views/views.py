from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request, sensor = 0):
    return HttpResponse("""<!DOCTYPE HTML><html><head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style> html { font-family: Arial; display: inline-block; margin: 0px auto; text-align: center; }
    h2 { font-size: 3.0rem; } p { font-size: 3.0rem; } .units { font-size: 1.2rem; } 
    .ds-labels{ font-size: 1.5rem; vertical-align:middle; padding-bottom: 15px; }
  </style></head><body><h2>ESP32 WebServer</h2>
  <p><i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="ds-labels">Temperature</span>
    <span id="temperature">""" + str(sensor) + """</span>
    <sup class="units">&deg;C</sup>
  </p>
    <p><i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="ds-labels">Temperature</span>
    <span id="temperature">""" + str(round(sensor * (9/5) + 32.0, 2)) + """</span>
    <sup class="units">&deg;F</sup>
  </p></body></html>""")