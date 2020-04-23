import speech_recognition as sr 
import socket 

host="put_you_computer_address_here" #Put the Computer IPv4 address here within double quotes
port=9999
s=socket.socket() #Creating Server Socket
s.bind((host,port)) #Binding Socket
s.listen(5) #Server starts listening to Client connections and can accept upto 5 Connections in this case.
conn,addr=s.accept() #Server accepts Client connections and can now send data to Client
print("connected to "+addr[0]+" and port= "+str(addr[1]))

s1=sr.Recognizer() #Creating Speech-Recogniser object

while True:
     #Recording Voice
     with sr.Microphone() as source:
         s1.adjust_for_ambient_noise(source)
         voice=s1.listen(source)
     #Using Google Speech-Recognition API to convert Voice to Text
     try:
        command=s1.recognize_google(voice)
        conn.send(str.encode(command)) #Sending Obtained Speech-to-text String to Client
        clresp=str(conn.recv(1024),"utf-8") #Receiving Client response
        print(clresp+"\n") #Printing Client Response for debugging purpose
        del voice
     except:
        continue

conn.close()
print("connection ended")
