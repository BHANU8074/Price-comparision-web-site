

from tkinter import *
import os
import sqlite3
root = Tk()
display = Label(root)
root.configure(bg='light green')
root.title("HANGMAN GAME")
root.geometry('900x500')
Email=StringVar()
Password=StringVar()      

def database():
            email=Email.get()
            password=Password.get()
            conn=sqlite3.connect("DATA.db")
            #conn.execute("create table data(Email varchar(50), Password text);")
            conn.execute("insert into data(Email,Password)values(?,?)",(email,password,))
            c=conn.execute("select * from data")
            for i in c:
                print("email",i[0])
                print("password",i[1])
                conn.commit()
            root.destroy()  

def shop():
        
        

        database()

        root=Tk()
        root.geometry("1600x8000")
        root.title("WISHLIST WEBSITE")
        root.configure(bg='light green')

     

        NAME= StringVar()

        def additem(*args):
            with open('test.txt', 'a+') as f:
               f.write(NAME.get()+'\n')
               f.write("\n")

        l1=Label(root,font=('Times',35,'bold'),text="CHOOSE YOUR ITEM ",fg="Black",bg="bisque2",bd=15,anchor='w')
        l1.pack()
        l1=Label(root,bd=16,fg="black",font=('Times',16,'bold'),width=12,text="MOBILE",bg="goldenrod").place(x=10,y=100)
        l2=Label(root,bd=16,fg="black",font=('Times',16,'bold'),width=12,text="FURNITURE",bg="goldenrod").place(x=300,y=100)
        l3=Label(root,bd=16,fg="black",font=('Times',16,'bold'),width=12,text="GROCERY",bg="goldenrod").place(x=600,y=100)
        l4=Label(root,bd=16,fg="black",font=('Times',16,'bold'),width=12,text="BOOKS",bg="goldenrod").place(x=900,y=100)
        l5=Label(root,bd=16,fg="black",font=('Times',16,'bold'),width=12,text="APPLIANCES",bg="goldenrod").place(x=1150,y=100)

        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Iphone_Xr").place(x=50,y=200)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Samsung_M30").place(x=50,y=240)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Redmi_Y3").place(x=50,y=280)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Redmi_7A").place(x=50,y=320)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Realme_U1").place(x=50,y=360)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Xiomi_A3").place(x=50,y=400)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Coolpad_3").place(x=50,y=440)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="One_plus_7T").place(x=50,y=480)


        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Chair").place(x=320,y=200)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Table").place(x=320,y=240)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Sofa").place(x=320,y=280)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Almirah").place(x=320,y=320)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Single_Bed").place(x=320,y=360)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Double_bed").place(x=320,y=400)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Stool").place(x=320,y=440)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Rack").place(x=320,y=480)

        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Sugar").place(x=620,y=200)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Tea").place(x=620,y=240)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Rice").place(x=620,y=280)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="wheat").place(x=620,y=320)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Rajma").place(x=620,y=360)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Nutry").place(x=620,y=400)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Tomato").place(x=620,y=440)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Onion").place(x=620,y=480)

        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Novel").place(x=920,y=200)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Science").place(x=920,y=240)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Adventure").place(x=920,y=280)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Action").place(x=920,y=320)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Scify").place(x=920,y=360)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Romance").place(x=920,y=400)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Fiction").place(x=920,y=440)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Text_Book").place(x=920,y=480)

        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Refrigirator").place(x=1170,y=200)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="AC").place(x=1170,y=240)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Fan").place(x=1170,y=280)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Cooler").place(x=1170,y=320)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="LED").place(x=1170,y=360)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Tubelight").place(x=1170,y=400)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="Washing Machine").place(x=31170,y=440)
        Label(root,bd=16,bg="light green",fg="black",font=('Times',12,'bold'),width=10,text="RO").place(x=1170,y=480)

        Label(root,bd=16,fg="black",font=('Times',16,'bold'),width=15,text="SELECT ITEM",bg="white").place(x=100,y=550)
        
        e1=Entry(root,textvariable=NAME,bd=10,bg="cyan", font=('times new roman', 20,"bold")).place(x=350,y=550)

        Button(root,bd=16,fg="black",font=('Times',16,'bold'),width=12,text="WISHLIST",bg="goldenrod",command=additem).place(x=700,y=550)
        
        Button(root,bd=16,fg="black",font=('Times',16,'bold'),width=14,text="COMPARE DATA",bg="goldenrod",command=new).place(x=1000,y=550)

        root.mainloop()


        
        



        
def new():
       
       import tkinter as tk
       from tkinter import messagebox
       import os
       f=open("proj.txt",'a+')

       root = Tk()
       root.title("Stationary ShopManagment System")
       root.configure(width=1500,height=600,bg="Grey")
       root.geometry("1600x8000")
       var=-1
       #All functions
       def deleteitem():
           e1=entry1.get()
           with open(r"proj.txt") as f, open(r"proj1.txt", "w") as working:
               for line in f:
                  if str(e1) not in line:
                     working.write(line)
           entry1.delete(0, END)
           entry2.delete(0, END)
           entry3.delete(0, END)
           entry4.delete(0, END)
           entry5.delete(0, END)
           os.remove(r"proj.txt")
           os.rename(r"proj1.txt", r"proj.txt")
           f.close()
           working.close()

       def list1():
           f=open("test.txt",'a+')
           global var
           var=0
           f.seek(var)
           root1 = Tk()
           root1.configure(bg="Grey")
           root1.title("Mobile Store Database")
           root1.geometry("1600x7000")
           scrollbar = Scrollbar(root1)
           scrollbar.pack( side = RIGHT, fill = Y)
           mytext = Text(root1, yscrollcommand = scrollbar.set ,width=130,height= 100 ,bg= "gray",fg="black", font=("Times", 16))
           string = f.read()
           mytext.insert(END,string)
           mytext.pack( side = LEFT, fill = BOTH )
           scrollbar.config( command = mytext.yview ) 
        
       def searchitem():
           entry1.delete(0, END)
           entry2.delete(0, END)
           entry3.delete(0, END)
           entry4.delete(0, END)
           entry5.delete(0, END)
           i=0
           flag = 1
           e1 = entry6.get()
           with open(r"proj.txt") as working:
               for line in working:
                  i=i+1
                  if str(e1) in line:
                    flag = 0
                    break
               try:
                   if flag != 1:
                      v = list(line.split(" "))
                      entry1.delete(0, END)
                      entry2.delete(0, END)
                      entry3.delete(0, END)
                      entry4.delete(0, END)
                      entry5.delete(0, END)
                      entry1.insert(0, str(v[0]))
                      entry2.insert(0, str(v[1]))
                      entry3.insert(0, str(v[2]))
                      entry4.insert(0, str(v[3]))
                      entry5.insert(0, str(v[4]))

               except:
                   messagebox.showinfo("Title", "error end of file")

               if flag !=0:
                   messagebox.showinfo("Title", "NOT FOUND")
           working.close()
        
            
       def clearitem():
             entry1.delete(0, END)
             entry2.delete(0, END)
             entry3.delete(0, END)
             entry4.delete(0, END)
             entry5.delete(0, END)
             entry6.delete(0, END)


       def qExit():
             qExit= messagebox.askyesno("Quit The System","Do you want to quit(y/n)?")
             if qExit > 0:
                root.destroy()
                return

         #All labels Entrys Button grid place
       label0= Label(root,text=" PRICE COMPARISSION ",bg="Black",fg="#F9FAE9",font=("Times", 40))
       label1=Label(root,text="ENTER ITEM NAME",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 15),width=25)
       entry1=Entry(root , font=("Times", 14),bd=8,width=25,bg="white")
       label2=Label(root, text="Flipkart",relief="ridge",height="1",bg="black",bd=8,fg="white", font=("Times", 15),width=25)
       entry2= Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
       label3=Label(root, text="Amazon",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 15),width=25)
       entry3= Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
       label4=Label(root, text="Ebay",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 15),width=25)
       entry4= Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
       label5=Label(root, text="Myntra",bg="black",relief="ridge",fg="white",bd=8, font=("Times", 15),width=25)
       entry5= Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
       buttoncolor="#49D810"
       buttonfg="black"

       
       button3= Button(root,highlightcolor="red",activebackground="green", text="VIEW DATABASE",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=list1)
       button4= Button(root,highlightcolor="red",activebackground="green", text="SEARCH ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=searchitem)
       button5= Button(root,highlightcolor="red",activebackground="green", text="CLEAR SCREEN",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=clearitem)
       button6= Button(root,highlightcolor="blue",activebackground="red", text="Exit",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 40),command=qExit)
       entry6= Entry(root, font=("Times", 14),justify='left',bd=8,width=25,bg="#EEEEF1")

       label0.grid(columnspan=6, padx=1, pady=10)
       label1.grid(row=1,column=0, padx=10, pady=10)
       label2.grid(row=2,column=0, padx=10, pady=10)
       label3.grid(row=3,column=0, padx=10, pady=10)
       label4.grid(row=4,column=0, padx=10, pady=10)
       label5.grid(row=5,column=0, padx=10, pady=10)
       entry1.grid(row=1,column=1, padx=40, pady=10)
       entry2.grid(row=2,column=1, padx=10, pady=10)
       entry3.grid(row=3,column=1, padx=10, pady=10)
       entry4.grid(row=4,column=1, padx=10, pady=10)
       entry5.grid(row=5,column=1, padx=10, pady=10)
       entry6.grid(row=1,column=3, padx=10, pady=10)

      
       button3.grid(row=3,column=3, padx=40, pady=10)
       button4.grid(row=2,column=3, padx=40, pady=10)
       button5.grid(row=4,column=3, padx=40, pady=10)
       button6.place(x=675,y=337,height= 102,width=245)

       root.mainloop()

       

##############
Label(root,text="Email",bg="light green", font=('times new roman', 20,"bold")).place(x=100,y=100)
Entry(root,textvar=Email,bg="goldenrod",bd=10, font=('times new roman', 20,"bold")).place(x=300,y=100)
Label(root,text="Password",bg="light green", font=('times new roman', 20,"bold")).place(x=100,y=200)
Entry(root,textvar=Password,bg="goldenrod",bd=10, font=('times new roman', 20,"bold")).place(x=300,y=200)
Button(root,text="Submit",bg="light green",bd=10, font=('times new roman', 20,"bold"),command=shop).place(x=400,y=300)       

        














