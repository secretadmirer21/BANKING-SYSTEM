from cProfile import label
from functools import WRAPPER_ASSIGNMENTS
from tkinter import*
from tkinter import messagebox
from turtle import left
from PIL import ImageTk
import mysql.connector


class banking:
    ## main screen of window :-
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")
        self.root.resizable(False,False)
        self.root.iconbitmap("icon.ico")
        self.root.title("Bank management system")
        self.photo=ImageTk.PhotoImage(file='backimg.jpg')
        self.back=Label(image=self.photo)
        self.back.pack()

        ## menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        self.file_menu = Menu(self.menubar)
        self.menubar.add_cascade(label="OPEN NEW ACCOUNT",command=self.open_ac)
        self.menubar.add_cascade(label="DEPOSITE AMOUNT",command=self.deposite_am)
        self.menubar.add_cascade(label="WITHDRAW AMOUNT",command=self.withdraw_am)
        self.menubar.add_cascade(label="DISPLAY CUSTOMER DETAILS",command=self.display_cd)
        self.menubar.add_cascade(label="DELETE ACCOUNT",command=self.delete_ac)

        ## img frame
        self.f=Frame(self.root,width=800,height=500)
        self.f.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.photo1=ImageTk.PhotoImage(file='frame.jpg')
        self.frame_img = Label(self.f, image = self.photo1)
        self.frame_img.pack()
        
        self.root.wm_attributes('-transparentcolor', '#ab23ff')
        self.m=Label(self.f,text="Welcome to Bank Mangement System",font=("times 25 bold"),relief=SUNKEN,fg="white",bg="#ab23ff",padx=10,pady=40)
        self.m.place(relx=0.5,rely=0.5,anchor=CENTER)

    ## NEW ACCOUNT OPENING
    def open_ac(self):
        self.f=Frame(self.root,width=800,height=500)
        self.f.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.photo1=ImageTk.PhotoImage(file='frame.jpg')
        self.frame_img = Label(self.f, image = self.photo1)
        self.frame_img.pack()
        
        self.l=Label(self.f,text="Open New Account",fg="orange",font=("times 22 bold"),bg="white",relief=GROOVE)
        self.l.place(x=10,y=5)

        # declaring Variable
        self.Email=StringVar()
        self.pass_word=StringVar()
        self.c_pass=StringVar()
        self.name=StringVar()
        self.age=IntVar()
        self.contact=IntVar()
        self.gen=StringVar()
        self.amt=IntVar()

        # labels and entries:-
        self.l1=Label(self.f,text="Email:",font=("arial 16 bold"),bg="#c7d7f1")
        self.l1.place(x=275,y=50)
        self.e1=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.Email)
        self.e1.place(x=350,y=50)

        self.l2=Label(self.f,text="Password:",font=("arial 16 bold"),bg="#cfdaf0")
        self.l2.place(x=234,y=90)
        self.e2=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.pass_word)
        self.e2.place(x=350,y=90)

        self.l3=Label(self.f,text="Confirm Password:",font=("arial 16 bold"),bg="#cedbee")
        self.l3.place(x=150,y=130)
        self.e3=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.c_pass)
        self.e3.place(x=350,y=130)

        self.l4=Label(self.f,text="Name:",font=("arial 16 bold"),bg="#dee5f5")
        self.l4.place(x=276,y=170)
        self.e5=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.name)
        self.e5.place(x=350,y=170)

        self.l5=Label(self.f,text="Address:",font=("arial 16 bold"),bg="#dfe7f4")
        self.l5.place(x=250,y=210)
        self.e5=Text(self.f,font=("arial 14 bold"),width=20,height=3)
        self.e5.place(x=350,y=210)

        self.l6=Label(self.f,text="            Contact No:",font=("arial 16 bold"),bg="#e3edf9")
        self.l6.place(x=150,y=300)
        self.e6=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.contact)
        self.e6.place(x=350,y=300)

        self.l7=Label(self.f,text="                        Age:",font=("arial 16 bold"),bg="#deecf9")
        self.l7.place(x=150,y=340)
        self.e7=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.age)
        self.e7.place(x=350,y=340)
        
        self.l8=Label(self.f,text="Gender:",font=("arial 16 bold"),bg="#e0eaf4")
        self.l8.place(x=260,y=390)
        self.r1=Radiobutton(self.f,text="Male",variable=self.gen,value="male",font=("times 10"),bg="#c2d3ed")
        self.r1.place(x=350,y=395)
        self.r2=Radiobutton(self.f,text="Female",variable=self.gen,value="female",font=("times 10"),bg="#b5cae7")
        self.r2.place(x=417,y=395)
        self.r3=Radiobutton(self.f,text="TransGender",variable=self.gen,value="transgender",font=("times 10"),bg="#9fb5dc")
        self.r3.place(x=500,y=395)

        self.l9=Label(self.f,text="Amount:",font=("arial 16 bold"),bg="#e0eaf4")
        self.l9.place(x=100,y=450)

        ## Button for submit
        self.b2=Button(self.f,text="Submit",font=("arial 15 bold"),command=self.submit)
        self.b2.place(x=430,y=450)
        self.e8=Entry(self.f,font=("arial 14 bold"),width=10,textvariable=self.amt)
        self.e8.place(x=200,y=450)

    def submit(self):
        Email1=self.Email.get()
        pass_word1=self.pass_word.get()
        c_pass1=self.c_pass.get()
        name1=self.name.get()
        address1=self.e5.get(1.0, "end-1c")
        age1=self.age.get()
        contact1=self.contact.get()
        gen1=self.gen.get()
        amt1=self.amt.get()

        if Email1 == "" or pass_word1 == "" or c_pass1 == "" or name1 == "" or address1 == "" or age1 == 0 or contact1 == 0 or gen1 == "" or amt1 == 0:
            messagebox.showwarning("error","Please fill all the filds")
        elif pass_word1!=c_pass1:
            messagebox.showwarning("warning","password does'nt match")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="VJ@123",database="bank")
            cur = mydb.cursor()
            query = "insert into users(email,Password_,c_password,Name_,Address,age,contact_no,gender,balance) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (Email1, pass_word1, c_pass1, name1, address1, age1, contact1, gen1,amt1)
            try:
                cur.execute(query, val)
                
            except:
                messagebox.showwarning("Error", "This Contact or Email already or contact \nregistered in the system")
            else:
                mydb.commit()
                messagebox.showinfo("Info", "Record submitted sucessfully")


    ## DESPOSITE AMOUNT FUNCTION
    def deposite_am(self):
        self.f=Frame(self.root,width=800,height=500)
        self.f.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.photo1=ImageTk.PhotoImage(file='frame.jpg')
        self.frame_img = Label(self.f, image = self.photo1)
        self.frame_img.pack()

        ## Deposite Amount:-
        self.l=Label(self.f,text="Deposite Amount",fg="orange",font=("times 22 bold"),bg="white",relief=GROOVE)
        self.l.place(x=10,y=5)

        ##declaring valibles
        self.demail=StringVar()
        self.dpassword=StringVar()
        self.damount=IntVar()

        ## LABELS AND ENTRIES
        self.l1=Label(self.f,text="Email:",font=("arial 16 bold"),bg="#e0e6f6")
        self.l1.place(x=295,y=130)
        self.e1=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.demail)
        self.e1.place(x=400,y=130)

        self.l2=Label(self.f,text="Password:",font=("arial 16 bold"),bg="#e0e6f6")
        self.l2.place(x=250,y=170)
        self.e2=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.dpassword)
        self.e2.place(x=400,y=170)

        self.l3=Label(self.f,text="   Amount:",font=("arial 16 bold"),bg="#e0e6f6")
        self.l3.place(x=250,y=220)
        self.e3=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.damount)
        self.e3.place(x=400,y=220)

        ## button
        self.b1=Button(self.f,text="Deposite",font=("arial 15 bold"),width=13,command=self.ddeposite)
        self.b1.place(x=220,y=300)
        self.b2=Button(self.f,text="Check Balance",font=("arial 15 bold"),width=13,command=self.dcheck)
        self.b2.place(x=410,y=300)

        self.l10=Label(self.f,text="",font=("arial 16 bold"),bg="#b5cae7")
        self.l10.place(x=420,y=350)

    def dcheck(self):
        demail1=self.demail.get()
        dpassword1=self.dpassword.get()
        if demail1=="" or dpassword1=="":
            messagebox.showerror("error","please fill the correct data")
        else:
            mydb=mysql.connector.connect(host="localhost",user="root",password="VJ@123",database="bank")
            cur=mydb.cursor()
            query="select balance from users where Email=%s and Password_=%s"
            val=(demail1,dpassword1)
            cur.execute(query,val)
            x=cur.fetchall()
            for k in x:
                self.a,=k
                self.l10['text']=f"Amount:{self.a}"
    
    def ddeposite(self):
        demail1=self.demail.get()
        dpassword1=self.dpassword.get()
        damt1=self.damount.get()

        if demail1=="" or dpassword1=="":
            messagebox.showerror("error","please fill the correct data")
        else:
            mydb=mysql.connector.connect(host="localhost",user="root",password="VJ@123",database="bank")
            cur=mydb.cursor()
            query="update users set balance=%s where email=%s and Password_=%s"
            val=(damt1+self.a,demail1,dpassword1)
            try:
                cur.execute(query,val)
            except:
                messagebox.showerror("error","Please check email or password")
            else:
                mydb.commit()
                query="select balance from users where Email=%s and Password_=%s"
                val=(demail1,dpassword1)
                cur.execute(query,val)
                x=cur.fetchall()
                for i in x:
                    j,=i
                    self.l10['text']=f"Amount:{j}"


    ## WITHDRAW AMOUNT FUNCTION
    def withdraw_am(self):
        self.f=Frame(self.root,width=800,height=500)
        self.f.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.photo1=ImageTk.PhotoImage(file='frame.jpg')
        self.frame_img = Label(self.f, image = self.photo1)
        self.frame_img.pack()

        ## label for withdraw:-
        self.l=Label(self.f,text="Withdraw Amount",fg="orange",font=("times 22 bold"),bg="white",relief=GROOVE)
        self.l.place(x=10,y=5)

        ##declaring valibles
        self.wemail=StringVar()
        self.wpassword=StringVar()
        self.wamount=IntVar()

        ## LABELS AND ENTRIES
        self.l1=Label(self.f,text="Email:",font=("arial 16 bold"),bg="#e0e6f6")
        self.l1.place(x=295,y=130)
        self.e1=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.wemail)
        self.e1.place(x=400,y=130)

        self.l2=Label(self.f,text="Password:",font=("arial 16 bold"),bg="#e0e6f6")
        self.l2.place(x=250,y=170)
        self.e2=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.wpassword)
        self.e2.place(x=400,y=170)

        self.l3=Label(self.f,text="   Amount:",font=("arial 16 bold"),bg="#e0e6f6")
        self.l3.place(x=250,y=220)
        self.e3=Entry(self.f,font=("arial 14 bold"),width=20,textvariable=self.wamount)
        self.e3.place(x=400,y=220)
        
        ## button
        self.b1=Button(self.f,text="Withdraw",font=("arial 15 bold"),width=13,command=self.wwithdraw)
        self.b1.place(x=220,y=300)
        self.b2=Button(self.f,text="Check Balance",font=("arial 15 bold"),width=13,command=self.wcheck)
        self.b2.place(x=410,y=300)

        self.l10=Label(self.f,text="",font=("arial 16 bold"),bg="#b5cae7")
        self.l10.place(x=420,y=350)


    def wcheck(self):
        wemail1=self.wemail.get()
        wpassword1=self.wpassword.get()

        
        if wemail1=="" or wpassword1=="":
            messagebox.showerror("error","please fill the correct data")
        
        else:
            mydb=mysql.connector.connect(host="localhost",user="root",password="VJ@123",database="bank")
            cur=mydb.cursor()
            query="select balance from users where Email=%s and Password_=%s"
            val=(wemail1,wpassword1)
            cur.execute(query,val)
            x=cur.fetchall()
            for i in x:
                j,=i
                self.l10['text']=f"Amount:{j}"

    def wwithdraw(self):
        wemail1=self.wemail.get()
        wpassword1=self.wpassword.get()
        wamt1=self.wamount.get()

        mydb=mysql.connector.connect(host="localhost",user="root",password="VJ@123",database="bank")
        cur=mydb.cursor()
        query="select balance from users where Email=%s and Password_=%s"
        val=(wemail1,wpassword1)
        cur.execute(query,val)
        x=cur.fetchall()
        for i in x:
            self.j,=i
            self.l10['text']=f"Amount:{self.j}"


        if wemail1=="" or wpassword1=="":
            messagebox.showerror("error","please fill the correct data")
        elif wamt1>self.j:
            messagebox.showerror("error","You don't have enough money")
        else:
            mydb=mysql.connector.connect(host="localhost",user="root",password="VJ@123",database="bank")
            cur=mydb.cursor()
            query="update users set balance=%s where email=%s and Password_=%s"
            val=(wamt1-self.j,wemail1,wpassword1)
            try:
                cur.execute(query,val)
            except:
                messagebox.showerror("error","Please check email or password")
            else:
                mydb.commit()
                query="select balance from users where Email=%s and Password_=%s"
                val=(wemail1,wpassword1)
                cur.execute(query,val)
                x=cur.fetchall()
                for i in x:
                    j,=i
                    self.l10['text']=f"Amount:{j}"

    def display_cd(self):
        self.f=Frame(self.root,width=800,height=500)
        self.f.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.photo1=ImageTk.PhotoImage(file='frame.jpg')
        self.frame_img = Label(self.f, image = self.photo1)
        self.frame_img.pack()

        ## label for heading:-
        self.l=Label(self.f,text="Customer details",fg="orange",font=("times 22 bold"),bg="white",relief=GROOVE)
        self.l.place(x=10,y=5)

        ## label for diplaying the coustomer details:-
        self.d=Label(self.f,text="Empty",font=("times 12 bold"),bg="#9fb5dc",padx=20,pady=20,relief=GROOVE,bd=2,justify="left")
        self.d.place(relx=0.5,rely=0.5,anchor=CENTER)

        
        mydb=mysql.connector.connect(host="localhost",user="root",password="VJ@123",database="bank")
        cur=mydb.cursor()
        cur.execute("select * from users")
        x=cur.fetchall()
        for i in x:
            self.d['text']=f":-  {i}\n"

    ## THIS IS DELETE FUNCTION
    def delete_ac(self):
        self.f=Frame(self.root,width=800,height=500)
        self.f.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.photo1=ImageTk.PhotoImage(file='frame.jpg')
        self.frame_img = Label(self.f, image = self.photo1)
        self.frame_img.pack()

        ## label for heading
        self.l=Label(self.f,text="Delete Account",fg="orange",font=("times 22 bold"),bg="white",relief=GROOVE)
        self.l.place(x=10,y=5)

        ## declaring varibles
        self.email=StringVar()
        self.password=StringVar()

        ## lables and entries for delete
        self.l1=Label(self.f,text="       Email:",font=("arial 16 bold"),bg="#d8dff2")
        self.l1.place(x=220,y=150)
        self.e1=Entry(self.f,font=("arial 14 bold"),textvariable=self.email)
        self.e1.place(x=350,y=150)
        
        self.l2=Label(self.f,text="Password:",font=("arial 16 bold"),bg="#d8dff2")
        self.l2.place(x=220,y=200)
        self.e2=Entry(self.f,font=("arial 14 bold"),textvariable=self.password)
        self.e2.place(x=350,y=200)

        ## Button for delete record
        self.b2=Button(self.f,text="Delete",font=("arial 15 bold"),width=10,command=self.delete)
        self.b2.place(x=390,y=250)

    def delete(self):
        Email1=self.email.get()
        Password_=self.password.get()

        mydb = mysql.connector.connect(host="localhost",user="root",password="VJ@123",database="bank")
        cur=mydb.cursor()
        q1="select * from users where email=%s and Password_=%s"
        val1=(Email1,Password_)
        cur.execute(q1,val1)
        x=cur.fetchall()
        if len(x)==0:
            messagebox.showerror("error","This email password doesn't match")
        else: 
            query="delete from users where email=%s and Password_=%s"
            val=(Email1,Password_)
            cur.execute(query,val)
            mydb.commit()
            messagebox.showinfo("succes","Data deleted successfully")
        
        
root=Tk()
obj=banking(root)
root.mainloop()