import socket
from machine import Pin
import network 

pin=Pin(16,Pin.OUT)
pin1=Pin(5,Pin.OUT)  
pin.on()
pin1.on()
mes1="fan turned on"
mes2="fan turned off"
mes3="light turned on"
mes4="light turned off"
mes5="invalid command"
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Your_WiFi_Name', 'Your_WiFi_Password')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

   
do_connect()
host="Put_Server_IP_address_here"
port=9999

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
    data=str(s.recv(1024),"utf-8")
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



