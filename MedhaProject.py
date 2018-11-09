
# coding: utf-8

# In[156]:


import os
import socket
import subprocess as s
from tkinter import *

ip_addr=socket.gethostbyname(socket.gethostname())
ip_add_list=socket.gethostbyname(socket.gethostname()).split(".")
myip=ip_addr
print(ip_addr)
print(ip_add_list)


# In[157]:


ip_addr=".".join(ip_add_list[:len(ip_add_list)-1])

#ip_addr="192.168.121" for LAB
print(ip_addr)


# In[158]:


root=Tk()

c=Canvas(root,height=550,width=500)
c.configure(background="#a1dbcd")
root.title("NCU LAB")
l=[]
oval=[] 
b1=[]
b2=['-1']*30


# In[159]:


#PINGing first 10 Pc's for first row
def r1():
    for i in range(10):
        x=ip_addr+"."+str(i)
        l.append(x)
        if(s.call(["ping",x])==0):
            print(x+" "+"ON")
            b1.append("1")
        else:
            print(x+" "+"OFF")
            b1.append("0")


# In[160]:


#To print first row
def row1():
    z=0
    for t in range(410,30,-40):                
        x1=30
        x2=45
        if b1[z]=='1':
            oval.append(c.create_oval(x1,t,x2,t+15,fill="green"))
            c.create_text(x1-20,t+5,text=str(z))
            z=z+1
      
        elif b1[z]=='0':
            oval.append(c.create_oval(x1,t,x2,t+15,fill="red"))
            c.create_text(x1-20,t+5,text=str(z))
            z=z+1


# In[161]:


#When selectively checking row 1
def row11():
    z=0
    for t in range(410,30,-40):                
        x1=30
        x2=45
        if b2[z]=='1':
            oval.append(c.create_oval(x1,t,x2,t+15,fill="green"))
            c.create_text(x1-20,t+5,text=str(z+1))
            z=z+1
      
        elif b2[z]=='0' :
            oval.append(c.create_oval(x1,t,x2,t+15,fill="red"))
            c.create_text(x1-10,t+5,text=str(z+1))
            z=z+1
        elif b2[z]=="-1":
            oval.append(c.create_oval(x1,t,x2,t+15,fill="white"))
            c.create_text(x1-10,t+5,text=str(z+1))
            z=z+1


# In[162]:


def r2():
        for i in range(10,21):
            x=ip_addr+"."+str(i)
            l.append(x)
            if(s.call(["ping",x])==0):
                 print(x+" "+"ON")
                 b1.append("1")
                    
            else:
                 print(x+" "+"OFF")
                 b1.append("0")


# In[163]:


def row2():
    z=10
    for i in range(70,450,40):
        y1=30
        y2=45
        if b1[z]=="1":
            oval.append(c.create_oval(i,y1,i+15,y2,fill="green"))
            c.create_text(i,y1-10,text=str(z))
            z=z+1
            print(z)
        elif b1[z]=="0":
            oval.append(c.create_oval(i,y1,i+15,y2,fill="red"))
            c.create_text(i,y1-10,text=str(z))
            z=z+1
            print(z)  


# In[164]:


def row22():
    z=10
    #t=65
    for i in range(70,450,40):
        y1=30
        y2=45
        if b2[z]=='1':
            oval.append(c.create_oval(i,y1,i+15,y2,fill="green"))
            c.create_text(i,y1-10,text=str(z+1))
            z=z+1
        elif b2[z]=='0':
            oval.append(c.create_oval(i,y1,i+15,y2,fill="red"))
            c.create_text(i,y1-10,text=str(z+1))
            z=z+1
            print(z)  
        elif b2[z]=="-1":
            oval.append(c.create_oval(i,y1,i+15,y2,fill="white"))
            c.create_text(i,y1-10,text=str(z+1))
            z=z+1


# In[165]:


def r3():
        for i in range(21,30):
            x=ip_addr+"."+str(i)
            l.append(x)
            if(s.call(["ping",x])==0):
                 print(x+" "+"ON")
                 b1.append("1")
                    
            else:
                 print(x+" "+"OFF")
                 b1.append("0")


# In[166]:


def row3():
    z=20
    for i in range(54,434,40):
        x1=465
        x2=480
        if b1[z]=="1":
            oval.append(c.create_oval(x1,i,x2,i+15,fill="green"))
            c.create_text(x1+25,i+5,text=str(z))
            z=z+1
        elif b1[z]=="0":
            oval.append(c.create_oval(x1,i,x2,i+15,fill="red"))
            c.create_text(x1+25,i+5,text=str(z))
            z=z+1


# In[167]:


def row33():
    z=20
    for i in range(54,434,40):
        x1=465
        x2=480
        if b2[z]=='1':
            oval.append(c.create_oval(x1,i,x2,i+15,fill="green"))
            c.create_text(x1+25,i+5,text=str(z+1))
            z=z+1
        elif b2[z]=='0':
            oval.append(c.create_oval(x1,i,x2,i+15,fill="red"))
            c.create_text(x1+25,i+5,text=str(z+1))
            z=z+1
        elif b2[z]=="-1":
            oval.append(c.create_oval(x1,i,x2,i+15,fill="white"))
            c.create_text(x1+25,i+5,text=str(z+1))
            z=z+1


# In[168]:


#when selectively checking for the PC's
def show_entry_fields():
    x=e1.get()
    ip_list=x.split(",")
    print(ip_list)
    j=0
    for i in range(len(ip_list)):
        a=ip_list[i]
        try:
            socket.inet_aton(a) #if invalid ip
            
            ipl=ip_list[i].split(".")
            r=int(ipl[-1])
            if(s.call(["ping",ip_list[i]])==0):
                print(ip_list[i]+" "+"ON")
                b2[r-1]="1"
                print(r)
                i=i+1
            elif(s.call(["ping",ip_list[i]])==1):
                print(ip_list[i]+" "+"OFF")
                b2[r-1]="0"
                print(r)
                i=i+1
        except socket.error:
                c.create_text(250,220,text="INVALID IP ADDRESS FORMAT- ")
                c.create_text(250,240,text=a[:])
        
        print(b2)    
    
    row11()
    row22()
    row33()
            
e1 = Entry(root)
e1.place(x=200,y=350)


# In[169]:


#Checking all 30 PC's
def show_entry():
                r1()
                row1()
                r2()
                row2()
                r3()
                row3()


# In[170]:


c.create_text(500 / 2,
              550 / 2,font="Times 15 bold",fill="dark blue",
              text="PYTHON LAB RN 124")
c.create_text(500 / 2,
              300,font="Times 12 bold",fill="grey",
              text="YOUR SYSTEM'S IP ADDRESS IS- "+myip)

c.create_text(250,
              340,
              text="Enter the PC IP's to check if they are ON/OFF")
Button(root, text="CHECK for these PC's ",command=show_entry_fields,bg="white").place(x=200,y=375)
Button(root, text='CLICK TO CHECK FOR THE WHOLE LAB',command=show_entry,bg="yellow").place(x=150,y=430)
c.pack()

root.mainloop()

