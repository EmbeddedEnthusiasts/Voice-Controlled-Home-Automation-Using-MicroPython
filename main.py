import socket
from machine import Pin
import network 

pin=Pin(16,Pin.OUT) #Configuring D0 as Output 
pin1=Pin(5,Pin.OUT)  #Configuring D1 as Output 
#Setting pins to OFF state as pins of NodeMCU are active low
pin.on() 
pin1.on()
mes1="fan turned on"
mes2="fan turned off"
mes3="light turned on"
mes4="light turned off"
mes5="invalid command"
#Function to connect NodeMCU to WiFi
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Your_WiFi_Name', 'Your_WiFi_Password') #Replace your WiFi name and Password accordingly, here within single quotes for both
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

   
do_connect()
host="Put_Server_IP_address_here" #put your Server IP address in Double quotes
port=9999

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Creating Client Socket
s.connect((host,port)) #Client connects to Server

while True:
    data=str(s.recv(1024),"utf-8") #Receiving data from Server
    #Actions performed based on received data, can be configured as per your choice
    if "on fan" in data:
      s.send(str.encode(mes1))
      pin.off()
      print(data)
      
    elif "off fan" in data:
        s.send(str.encode(mes2))
        pin.on()
        print(data)
    elif "on light" in data:
        s.send(str.encode(mes3))
        pin1.off()
        print(data)
    elif "off light" in data:
        s.send(str.encode(mes4))
        pin1.on()
        print(data)
    else:
        print("host entered invalid command")
        s.send(str.encode(mes5))
        continue



