import speech_recognition as sr 
import socket 

host="put_you_computer_address_here"
port=9999
s=socket.socket()
s.bind((host,port))
s.listen(5)
conn,addr=s.accept()
print("connected to "+addr[0]+" and port= "+str(addr[1]))

s1=sr.Recognizer()

while True:
     with sr.Microphone() as source:
         s1.adjust_for_ambient_noise(source)
         voice=s1.listen(source)
     try:
        command=s1.recognize_google(voice)
        conn.send(str.encode(command))
        clresp=str(conn.recv(1024),"utf-8")
        print(clresp+"\n")
        del voice
     except:
        continue

conn.close()
print("connection ended")
