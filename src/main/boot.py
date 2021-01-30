try
  import usocket as socket
except:
  import socket
from time import sleep
from machine import Pin #Serve pra interagir com a GPIO
import onewire, ds18x20
import network #Biblioteca de rede

import esp
esp.osdebug(None) #Desativa as mensagens de depuração do SO
 
import gc #Garbage collector
gc.collect()
 
ds_pin = Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

'''Credenciais da rede'''
ssid =  input("Informe o SSID da rede: ")
password = input("Informe a senha da rede: ")


station = network.WLAN(network.STA_IF) #Definindo a estação wifi do ESP     
 
station.active(True) #Ativa a conexão
station.connect(ssid, password) #Conecta com a rede que eu quero
 
while station.isconnected() == False: #Não permite que o ESP fique sem se conectar
  pass
 
print('Connection successful')
print(station.ifconfig()) #Imprime os parametros da rede do ESP

led = Pin(2, Pin.OUT) #Cria uma saída pra porta indicada do LED 