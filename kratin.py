import datetime
import os
import mysql.connector
import playsound

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='TODOTRACKER')

if mydb:
    cur=mydb.cursor()
    #cur.execute("CREATE DATABASE TODOTRACKER")
    #querry="CREATE TABLE Track(trackid integer(10) NOT NULL AUTO_INCREMENT,tdate date NOT NULL,twork varchar(20) NOT NULL,ttime time(0) NOT NULL,tampm varchar(2),PRIMARY KEY (trackid))"
    #cur.execute(querry)
else:
    print("connection not established !!")



def seeTrack():
    Select_Querry="select * from Track"
    cur.execute(Select_Querry)
    result=cur.fetchall()
    for x in result:
        print(x)


print("set your plan for today")

work=[]
time=[]
output=''

while 1:
    n=input("Enter the work")
    work.append(n)
    opt=input("do you want to continue:[y/n]")
    
    if opt.lower()=='n':
        break
    
print("your plan for today")

count=1

for i in work:
    print(count,".",i)
    count+=1
    
for i in work:
    os.system("clear")
    print("Set the timer so tha we can alert you for",i)
    
    hour=int(input("Enter hour"))
    time.append(hour)
    minute=int(input("And what minutes ?"))
    time.append(minute)
    amPm=str(input("am or pm?"))
    
    print("waiting for timer",hour,minute,amPm)
    
    if(amPm=="pm"):
        hour=hour+12
        
    while (1==1):
        if(hour==datetime.datetime.now().hour and minute==datetime.datetime.now().minute):
            playsound.playsound('beep-02.mp3')
            print("Time to start",i)
            Insert_Query="INSERT INTO Track(tdate,twork,ttime,tampm) VALUES(%s,%s,%s,%s)"
            for x in time:
                output+=str(x)
            values=(datetime.date.today(),i,output,amPm)
            cur.execute(Insert_Query,values)
            mydb.commit()
            time.clear()
            break
        
print("plan executed for today")
while 1:
    n=input("1 :- press 1 to see you track \n 2 :- exit\n")
    if n=='1':
        seeTrack()
    else:
        break
