from tkinter import*
from tkinter import messagebox as ms
from tkinter import messagebox
import random
import time;
import datetime
import sqlite3
from tkinter import Tk, StringVar, ttk

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

#class main
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)
        
root=Tk()
root.title("Login Form")
main(root)
root.mainloop()
root=Tk()
root.geometry("1350x750+0+0")
root.title("Bake Shop Cashier")

Tops = Frame (root, width = 1350 , height=100, bd= 6, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, fg ='deep pink',  background = 'SteelBlue1',  font=('times new roman' ,  50,  'bold','italic'), text="\tBake Shop Cashier\t\t\t")
lblTitle.grid(row=0, column=0)

BottomMainFrame = Frame (root, background = 'RoyalBlue1', width =1350, height=650, bd= 6, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame (BottomMainFrame, background = 'khaki1', width = 450 , height=650, bd= 2, relief="raise")
f1.pack(side=LEFT)
f2 = Frame (BottomMainFrame,background = 'khaki2', width = 450 , height=650, bd= 2, relief="raise")
f2.pack(side=LEFT)
f2TOP = Frame (f2,background = 'khaki3', width = 450 , height=350, bd= 2, relief="raise")
f2TOP .pack(side=TOP)
f2BOTTOM = Frame (f2,background = 'khaki4', width = 450 , height=300, bd= 1, relief="raise")
f2BOTTOM.pack(side=BOTTOM)

f3 = Frame (BottomMainFrame,background = 'LightGoldenRod1' , width = 450 , height=650, bd= 0, relief="raise")
f3 .pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=StringVar()
var23=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)

varWater = StringVar()
varJuice = StringVar()
varSpanishbread = StringVar()
varCheesebun = StringVar()
varCheesemilk = StringVar()
varEnsaymada = StringVar()
varMiniEnsaymada = StringVar()
varChocoGerman = StringVar()

varPandecoco = StringVar()
varUberoll = StringVar()
varCookies = StringVar()
varUbebar = StringVar()
varChickenmeatroll = StringVar()

varTea = StringVar()
varCola = StringVar()
varCoffee = StringVar()
varOrange = StringVar()
varLemon = StringVar()

varVanillaCone = StringVar()
varVanillaShake = StringVar()
varStrawberryShake = StringVar()

varTax=StringVar()
varChange = StringVar()
varSubTotal = StringVar()
varVAT = StringVar()
varTotal = StringVar()
varPayment = IntVar()

varWater.set("0")
varJuice.set("0")
varSpanishbread .set("0")
varCheesebun .set("0")
varCheesemilk .set("0")
varEnsaymada .set("0")
varMiniEnsaymada .set("0")
varChocoGerman .set("0")
varPayment.set(" ")

varPandecoco.set("0")
varUberoll.set("0")
varCookies.set("0")
varUbebar.set("0")
varChickenmeatroll .set("0")


varTea.set("0")
varCola.set("0")
varCoffee.set("0")
varOrange.set("0")
varLemon.set("0")

varVanillaCone.set("0")
varVanillaShake.set("0")
varStrawberryShake.set("0")

varTax.set("0")
varVAT.set(" ")
varChange.set("0")
varSubTotal.set("0")
varTotal.set("0")


def iExit():
        qExit= messagebox.askyesno("Bake Shop", "Do you want to quit the cashier?")
        if qExit  >  0:
            root.destroy()
            return

def Reset():

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        var22.set(0)
        var23.set(0)
        
        varWater.set("0")
        varJuice.set("0")
        varSpanishbread .set("0")
        varCheesebun .set("0")
        varCheesemilk .set("0")
        varEnsaymada .set("0")
        varMiniEnsaymada .set("0")
        varChocoGerman .set("0")

        varPandecoco.set("0")
        varUberoll.set("0")
        varCookies.set("0")
        varUbebar.set("0")
        varChickenmeatroll .set("0")


        varTea.set("0")
        varCola.set("0")
        varCoffee.set("0")
        varOrange.set("0")
        varLemon.set("0")

        varVanillaCone.set("0")
        varVanillaShake.set("0")
        varStrawberryShake.set("0")

        varTax.set("0")
        varVAT.set(" ")
        varChange.set("0")
        varSubTotal.set(" ")
        varTotal.set("0")
        varPayment.set(" ")

        txtWater.configure(state =DISABLED)
        txtJuice.configure(state =DISABLED)
        txtSpanishbread.configure(state =DISABLED)
        txtCheesebun.configure(state =DISABLED)
        txtCheesemilk.configure(state =DISABLED)
        txtEnsaymada.configure(state =DISABLED)
        txtMiniEnsaymada.configure(state =DISABLED)
        txtChocoGerman.configure(state =DISABLED)
        txtPandecoco.configure(state =DISABLED)
        txtUberoll.configure(state =DISABLED)
        txtCookies.configure(state =DISABLED)
        txtUbebar.configure(state =DISABLED)
        txtChickenmeatroll.configure(state =DISABLED)
        txtTea.configure(state =DISABLED)
        txtCola.configure(state =DISABLED)
        txtCoffee.configure(state =DISABLED)
        txtOrange.configure(state =DISABLED)
        txtLemon.configure(state =DISABLED)
        txtVanillaCone.configure(state =DISABLED)
        txtVanillaShake.configure(state =DISABLED)
        txtStrawberryShake.configure(state =DISABLED)
        txtTax.configure(state =DISABLED)
        txtVAT.configure(state =DISABLED)
        txtChange.configure(state =DISABLED)
        txtSubTotal.configure(state =DISABLED)
        txtTotal.configure(state =DISABLED)
        #txtPayment.configure(state=DISABLED)
        var8.get()==0


def chkWater():
    if (var1.get()==1):
        txtWater.configure(state=NORMAL)
        varWater.set("")
    elif(var1.get() ==0):
        txtWater.configure(state=DISABLED)
        varWater.set("0")

def chkJuice ():
    if (var2.get()==1):
        txtJuice .configure(state=NORMAL)
        varJuice.set("")
    elif(var2.get() ==0):
        txtJuice .configure(state=DISABLED)
        varJuice .set("0")
        
def chkSpanishbread():
    if (var3.get()==1):
        txtSpanishbread.configure(state=NORMAL)
        varSpanishbread.set("")
    elif(var3.get() ==0):
        txtSpanishbread.configure(state=DISABLED)
        varSpanishbread.set("0")
        
def chkCheesebun ():
    if (var4.get()==1):
        txtCheesebun .configure(state=NORMAL)
        varCheesebun .set("")
    elif(var4.get() ==0):
        txtCheesebun .configure(state=DISABLED)
        varCheesebun .set("0")
        
def chkCheesemilk ():
    if (var5.get()==1):
        txtCheesemilk .configure(state=NORMAL)
        varCheesemilk .set("")
    elif(var5.get() ==0):
        txtCheesemilk .configure(state=DISABLED)
        varCheesemilk .set("0")
        
def chkEnsaymada ():
    if (var6.get()==1):
        txtEnsaymada .configure(state=NORMAL)
        varEnsaymada .set("")
    elif(var6.get() ==0):
        txtEnsaymada .configure(state=DISABLED)
        varEnsaymada .set("0")
        
def chkMiniEnsaymada():
    if (var7.get()==1):
        txtMiniEnsaymada.configure(state=NORMAL)
        varMiniEnsaymada.set("")
    elif(var7.get() ==0):
        txtMiniEnsaymada.configure(state=DISABLED)
        varMiniEnsaymada.set("0")
        
def chkChocoGerman ():
    if (var8.get()==1):
        txtChocoGerman .configure(state=NORMAL)
        varChocoGerman .set("")
    elif(var8.get() ==0):
        txtChocoGerman .configure(state=DISABLED)
        varChocoGerman .set("0")
        
def chkPandecoco  ():
    if (var9.get()==1):
        txtPandecoco .configure(state=NORMAL)
        varPandecoco .set("")
    elif(var9.get() ==0):
        txtPandecoco .configure(state=DISABLED)
        varPandecoco .set("0")
        
def chkUberoll ():
    if (var10.get()==1):
        txtUberoll .configure(state=NORMAL)
        varUberoll .set("")
    elif(var10.get() ==0):
        txtUberoll .configure(state=DISABLED)
        varUberoll .set("0")
        
def chkCookies():
    if (var11.get()==1):
        txtCookies.configure(state=NORMAL)
        varCookies.set("")
    elif(var11.get() ==0):
        txtCookies.configure(state=DISABLED)
        varCookies.set("0")
        
def chkUbebar ():
    if (var12.get()==1):
        txtUbebar .configure(state=NORMAL)
        varUbebar .set("")
    elif(var12.get() ==0):
        txtUbebar .configure(state=DISABLED)
        varUbebar .set("0")
        
def chkChickenmeatroll():
    if (var13.get()==1):
        txtChickenmeatroll.configure(state=NORMAL)
        varChickenmeatroll.set("")
    elif(var13.get() ==0):
        txtChickenmeatroll.configure(state=DISABLED)
        varChickenmeatroll.set("0")
        
def chkTea ():
    if (var14.get()==1):
        txtTea .configure(state=NORMAL)
        varTea .set("")
    elif(var14.get() ==0):
        txtTea .configure(state=DISABLED)
        varTea .set("0")
        
def chkCola():
    if (var15.get()==1):
        txtCola.configure(state=NORMAL)
        varCola.set("")
    elif(var15.get() ==0):
        txtCola.configure(state=DISABLED)
        varCola.set("0")
        
def chkCoffee ():
    if (var16.get()==1):
        txtCoffee .configure(state=NORMAL)
        varCoffee .set("")
    elif(var16.get() ==0):
        txtCoffee .configure(state=DISABLED)
        varCoffee .set("0")
        
def chkOrange():
    if (var17.get()==1):
        txtOrange.configure(state=NORMAL)
        varOrange.set("")
    elif(var17.get() ==0):
        txtOrange.configure(state=DISABLED)
        varOrange.set("0")
        
def chkLemon():
    if (var18.get()==1):
        txtLemon.configure(state=NORMAL)
        varLemon.set("")
    elif(var18.get() ==0):
        txtLemon.configure(state=DISABLED)
        varLemon.set("0")
        
def chkVanillaCone():
    if (var19.get()==1):
        txtVanillaCone.configure(state=NORMAL)
        varVanillaCone.set("")
    elif(var19.get() ==0):
        txtVanillaCone.configure(state=DISABLED)
        varVanillaCone.set("0")
        
def chkVanillaShake():
    if (var20.get()==1):
        txtVanillaShake.configure(state=NORMAL)
        varVanillaShake.set("")
    elif(var20.get() ==0):
        txtVanillaShake.configure(state=DISABLED)
        varVanillaShake.set("0")

def chkStrawberryShake ():
    if (var21.get()==1):
        txtStrawberryShake .configure(state=NORMAL)
        varStrawberryShake .set("")
    elif(var21.get() ==0):
        txtStrawberryShake .configure(state=DISABLED)
        varStrawberryShake .set("0")

def costofmeal():
        meal1 = float(varWater.get())
        meal2= float(varJuice.get())
        meal3= float(varSpanishbread.get())
        meal4= float(varCheesebun.get())
        meal5= float(varCheesemilk.get())
        meal6= float(varEnsaymada.get())
        meal7= float(varMiniEnsaymada.get())
        meal8= float(varChocoGerman.get())
        meal9= float(varPandecoco.get())
        meal10= float(varUberoll.get())
        meal11= float(varCookies.get())
        meal12 = float(varUbebar.get())
        meal13 = float(varChickenmeatroll.get())
        meal14 = float(varTea.get())
        meal15 = float(varCola.get())
        meal16 = float(varCoffee.get())
        meal17 = float(varOrange.get())
        meal18 = float(varLemon.get())
        meal19 = float(varVanillaCone.get())
        meal20 = float(varVanillaShake.get())
        meal21 = float(varStrawberryShake.get())

        iTotal1=((meal1 * 35) + (meal2 * 70) + (meal3 * 8) + (meal4 * 8))
        iTotal2=((meal5 * 8) + (meal6 * 17) + (meal7 * 8) + (meal8 * 8))
        iTotal3=((meal9 * 8) + (meal10 * 8) + (meal11 * 15) + (meal12 * 17))
        iTotal4=((meal13 * 12) + (meal14 * 80) + (meal15 * 35) + (meal16 * 100))
        iTotal5=((meal17 * 75) + (meal18 * 75) + (meal19 * 100) + (meal20 * 100) + (meal21 * 100))


        if (var22.get() == "Cash"):
                iChange = float(varPayment.get())
                iCost = (iTotal1+  iTotal2 +  iTotal3 +  iTotal4 +  iTotal5)
                iTax = (iCost * 3.4)/100
                iTaxq = "P", str('%.12f'%(iTax))
                varTax.set(iTaxq)

                iCostq ="P", str('%.12f'%(iCost))
                varSubTotal.set(iCostq)
                iTotalq = "P", str('%.12f'%((iCost + iTax)))
                varTotal.set(iTotalq)
                cChange = (iChange - (iCost + iTax))
                cChangeq = "P", str('%.12f'%(cChange))
                varChange.set(cChangeq)
        
        elif(var22.get() == "Master Card" or "Visa Card" or "Debit Card"):
                varPayment.set("")
                iCost=(iTotal1 +  iTotal2 +  iTotal3 +  iTotal4 +  iTotal5)
                iTax = (iCost * 3.4)/100
                iTaxq = "P", str('%.12f'%(iTax))
                varTax.set(iTaxq)
                iCostq ="P", str('%.12f'%(iCost))
                varSubTotal.set(iCostq)
                iTotalq = "P", str('%.12f'%((iCost + iTax)))
                varTotal.set(iTotalq)
                varChange.set("")
        
#=================================================Frame 1=======================
lblMeal = Label(f1, fg ='gray33',  background = 'khaki1', font=('Courier New' ,  20,  'bold','italic'), text="Breads That Taste Good")
lblMeal.grid(row=0, column=0)

Water =Checkbutton(f1, text="Water \tPHP35", variable=var1, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkWater).grid(row=1, column=0, sticky=W)
txtWater = Entry(f1, font=('arial',18,'bold'), textvariable = varWater, width=6, justify='right', state=DISABLED)
txtWater.grid(row =1, column =1)

Juice =Checkbutton(f1, text="Juice\tPHP70", variable=var2, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkJuice).grid(row=2, column=0, sticky=W)
txtJuice = Entry(f1, font=('arial',18,'bold'), textvariable = varJuice, width=6, justify='right', state=DISABLED)
txtJuice.grid(row =2, column =1)

Spanishbread =Checkbutton(f1, text="Spanish Bread\tPHP8", variable=var3, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkSpanishbread).grid(row=3, column=0, sticky=W)
txtSpanishbread = Entry(f1, font=('arial',18,'bold'), textvariable = varSpanishbread, width=6, justify='right', state=DISABLED)
txtSpanishbread.grid(row =3, column =1)

Cheesebun =Checkbutton(f1, text="Cheese Bun\tPHP8", variable=var4, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkCheesebun).grid(row=4, column=0, sticky=W)
txtCheesebun = Entry(f1, font=('arial',18,'bold'), textvariable = varCheesebun, width=6, justify='right', state=DISABLED)
txtCheesebun.grid(row =4, column =1)

Cheesemilk =Checkbutton(f1, text="Cheese Milk\tPHP8", variable=var5, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkCheesemilk ).grid(row=5, column=0, sticky=W)
txtCheesemilk = Entry(f1, font=('arial',18,'bold'), textvariable = varCheesemilk, width=6, justify='right', state=DISABLED)
txtCheesemilk.grid(row =5, column =1)

Ensaymada =Checkbutton(f1, text="Ensaymada\tPHP17", variable=var6, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkEnsaymada).grid(row=6, column=0, sticky=W)
txtEnsaymada = Entry(f1, font=('arial',18,'bold'), textvariable = varEnsaymada, width=6, justify='right', state=DISABLED)
txtEnsaymada.grid(row =6, column =1)

MiniEnsaymada =Checkbutton(f1, text="Mini Ensaymada\tPHP8", variable=var7, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkMiniEnsaymada).grid(row=7, column=0, sticky=W)
txtMiniEnsaymada = Entry(f1, font=('arial',18,'bold'), textvariable = varMiniEnsaymada, width=6, justify='right', state=DISABLED)
txtMiniEnsaymada.grid(row =7, column =1)

ChocoGerman =Checkbutton(f1, text="Choco German\tPHP8", variable=var8, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkChocoGerman ).grid(row=8, column=0, sticky=W)
txtChocoGerman = Entry(f1, font=('arial',18,'bold'), textvariable = varChocoGerman, width=6, justify='right', state=DISABLED)
txtChocoGerman.grid(row =8, column =1)

lblspace=Label( f1, text="\n\n\n\n\n\n\n\n")
lblspace.grid(row = 9, column=0)

#=================================================Frame 2=================================
lblMeal = Label(f2TOP,fg ='gray33',  background = 'khaki3', font=('Courier New' ,  20,  'bold','italic'), text="Other Breads That Taste Good")
lblMeal.grid(row=0, column=0)

Pandecoco =Checkbutton(f2TOP, text="Pan de Coco\tPHP8", variable=var9, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkPandecoco).grid(row=1, column=0, sticky=W)
txtPandecoco = Entry(f2TOP, font=('arial',18,'bold'), textvariable = varPandecoco, width=6, justify='right', state=DISABLED)
txtPandecoco.grid(row =1, column =1)

Uberoll =Checkbutton(f2TOP, text="Ube Roll\t\tPHP8", variable=var10, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkUberoll).grid(row=2, column=0, sticky=W)
txtUberoll = Entry(f2TOP, font=('arial',18,'bold'), textvariable = varUberoll, width=6, justify='right', state=DISABLED)
txtUberoll.grid(row =2, column =1)

Cookies =Checkbutton(f2TOP, text="Cookies\t\tPHP15", variable=var11, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkCookies).grid(row=3, column=0, sticky=W)
txtCookies = Entry(f2TOP, font=('arial',18,'bold'), textvariable = varCookies, width=6, justify='right', state=DISABLED)
txtCookies.grid(row =3, column =1)

Ubebar =Checkbutton(f2TOP, text="Ube Bar\t\tPHP17", variable=var12, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkUbebar).grid(row=4, column=0, sticky=W)
txtUbebar = Entry(f2TOP, font=('arial',18,'bold'), textvariable = varUbebar, width=6, justify='right', state=DISABLED)
txtUbebar.grid(row =4, column =1)

Chickenmeatroll =Checkbutton(f2TOP, text="Chicken Meat Roll PHP12", variable=var13, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkChickenmeatroll).grid(row=5, column=0, sticky=W)
txtChickenmeatroll = Entry(f2TOP, font=('arial',18,'bold'), textvariable = varChickenmeatroll, width=6, justify='right', state=DISABLED)
txtChickenmeatroll.grid(row =5, column =1)

#=================================================Frame 3=================================
lblMeal = Label(f3,fg ='gray33',  background = 'LightGoldenRod1',font=('Courier New' ,  20,  'bold','italic'), text="Beverages")
lblMeal.grid(row=0, column=0)

Tea =Checkbutton(f3, text="Tea \tPHP80", variable=var14, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkTea).grid(row=1, column=0, sticky=W)
txtTea = Entry(f3, font=('arial',18,'bold'), textvariable = varTea, width=6, state=DISABLED)
txtTea.grid(row =1, column =1)

Cola =Checkbutton(f3, text="Cola \tPHP35", variable=var15, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkCola).grid(row=2, column=0, sticky=W)
txtCola = Entry(f3, font=('arial',18,'bold'), textvariable = varCola, width=6, state=DISABLED)
txtCola.grid(row =2, column =1)

Coffee =Checkbutton(f3, text="Coffee \tPHP100", variable=var16, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkCoffee).grid(row=3, column=0, sticky=W)
txtCoffee = Entry(f3, font=('arial',18,'bold'), textvariable = varCoffee, width=6, state=DISABLED)
txtCoffee.grid(row =3, column =1)

Orange =Checkbutton(f3, text="Orange \tPHP75", variable=var17, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkOrange).grid(row=4, column=0, sticky=W)
txtOrange = Entry(f3, font=('arial',18,'bold'), textvariable = varOrange, width=6, state=DISABLED)
txtOrange.grid(row =4, column =1)

Lemon =Checkbutton(f3, text="Lemon \tPHP75", variable=var18, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkLemon ).grid(row=5, column=0, sticky=W)
txtLemon = Entry(f3, font=('arial',18,'bold'), textvariable = varLemon, width=6, state=DISABLED)
txtLemon.grid(row =5, column =1)

VanillaCone =Checkbutton(f3, text="Vanilla Cone\nPHP100", variable=var19, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkVanillaCone).grid(row=6, column=0, sticky=W)
txtVanillaCone = Entry(f3, font=('arial',18,'bold'), textvariable = varVanillaCone, width=6, state=DISABLED)
txtVanillaCone.grid(row =6, column =1)

VanillaShake =Checkbutton(f3, text="Vanilla Shake\nPHP100", variable=var20, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkVanillaShake).grid(row=7, column=0, sticky=W)
txtVanillaShake = Entry(f3, font=('arial',18,'bold'), textvariable = varVanillaShake, width=6, state=DISABLED)
txtVanillaShake.grid(row =7, column =1)

StrawberryShake =Checkbutton(f3, text="Strawberry Shake\nPHP100", variable=var21, onvalue=1, offvalue=0,
                   font=('arial',18,'bold'), command=chkStrawberryShake ).grid(row=8, column=0, sticky=W)
txtStrawberryShake = Entry(f3, font=('arial',18,'bold'), textvariable = varStrawberryShake, width=6,state=DISABLED)
txtStrawberryShake.grid(row =8, column =1)

lblspace=Label( f3, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row = 10, column=0)

#=================================================Frame 2 bottom=================================

lblPaymentMethod = Label(f2BOTTOM ,fg ='gray33',  background = 'khaki4', font=('Courier New' ,  20,  'bold','italic'), text="Payment Method", bd=10, width= 16, anchor='w')
lblPaymentMethod.grid(row=0,column=0)

lblChange = Label(f2BOTTOM , font=('arial',14,'bold'), text="Change", bd=10, anchor='w')
lblChange.grid(row=0,column=1)
txtChange = Entry(f2BOTTOM, font=('arial',18,'bold'), textvariable =varChange, width =6, state = DISABLED)
txtChange.grid(row=0, column=2)

cmbPaymentMethod = ttk.Combobox(f2BOTTOM, textvariable = var22, state='readonly', font=('arial',10,'bold'), width= 20)
cmbPaymentMethod['value']=('Cash','Master Card','Visa Card','Debit card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1,column=0)

lblTax = Label(f2BOTTOM , font=('arial',14,'bold'), text="Tax", bd=10, anchor='w')
lblTax.grid(row=1,column=1)
txtTax = Entry(f2BOTTOM, font=('arial',18,'bold'), textvariable =varTax, width =6,  justify='left', state = DISABLED)
txtTax.grid(row=1, column=2)

txtPayment = Entry(f2BOTTOM,font=('arial',18,'bold'), textvariable =varPayment, width =6,  justify='left')
txtPayment.grid(row =2, column =0)
lblSubTotal =Label(f2BOTTOM , font=('arial',14,'bold'), text="Sub Total", bd=10,width = 8, anchor='w')
lblSubTotal.grid(row =2, column=1)
txtSubTotal =  Entry(f2BOTTOM,font=('arial',18,'bold'), textvariable =varSubTotal, width =6,  justify='left', state = DISABLED)
txtSubTotal.grid(row =2, column=2)

lblTotal = Label(f2BOTTOM , font=('arial',14,'bold'), text="Total", bd=10, width =6, anchor='w')
lblTotal.grid(row=3,column=1)
txtTotal = Entry(f2BOTTOM, font=('arial',18,'bold'), textvariable =varTotal, width =6, justify='left' ,state = DISABLED)
txtTotal.grid(row=3, column=2)

#===============================================Button=================================
btnTotal=Button(f2BOTTOM,padx=16, pady=1, bd=4, fg="Black", font=('arial', 16,'bold'), width=5, text="Total", command=costofmeal).grid(row=4, column=0)
btnReset=Button(f2BOTTOM,padx=16, pady=1, bd=4, fg="Black", font=('arial', 16,'bold'), width=5, text="Reset", command=Reset).grid(row=4, column=1)
btnExit=Button(f2BOTTOM,padx=16, pady=1, bd=4, fg="Black", font=('arial', 16,'bold'), width=5, text="Exit",command=lambda:  iExit()).grid(row=4, column=2)

lblspace=Label(f2BOTTOM, text="\n\n\n\n\n\n\n")
lblspace.grid(row =5, column=0)
#root.mainloop()
