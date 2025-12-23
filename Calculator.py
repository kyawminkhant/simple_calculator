# Tutorial by Codemy.com, continued the code as suggested to make a calculator

from tkinter import *

root=Tk()
root.title("Simple Calculator")

d=Entry(root, width=20, borderwidth=5, font=("Adobe-Garamond-Pro", 12)) # To show previous calculations
d.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

e=Entry(root, width=35, borderwidth=5, font="Adobe-Garamond-Pro") # Inputs
e.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

math="" # Undefined math variable
resultShown=False # No result on screen
num1Exist=False # Undefined f_num variable



#Commands
def click(number):
    global resultShown
    
    if resultShown: # Clear screen if new number is input while there is result
        e.delete(0, END)
        d.delete(0, END)
        resultShown = False
        
    current=e.get()
    e.delete(0, END)
    e.insert(0, current+str(number))

# If value is such that 6.0, the value will return 6
def roundFind(number): 
    FstCheck=str(number) # Turn into string to allow if "." is in the number
    if "."in FstCheck:
        check=str(number).split(".")
        if check[1]=="0":
            numberToReturn=str(check[0])
        else:
            numberToReturn=str(number)
    else:
        numberToReturn=str(number) 
    return numberToReturn

# Record data into top text box to allow user to see the calculations
def record(element):
    if element=="Zerror":
        d.delete(0, END)
        button_0.config(state=DISABLED)
        button_1.config(state=DISABLED)
        button_2.config(state=DISABLED)
        button_3.config(state=DISABLED)
        button_4.config(state=DISABLED)
        button_5.config(state=DISABLED)
        button_6.config(state=DISABLED)
        button_7.config(state=DISABLED)
        button_8.config(state=DISABLED)
        button_9.config(state=DISABLED)
        button_divide.config(state=DISABLED)
        button_multiply.config(state=DISABLED)
        button_minus.config(state=DISABLED)
        button_add.config(state=DISABLED)
        button_equal.config(state=DISABLED)
        button_negate.config(state=DISABLED)
        button_decimal.config(state=DISABLED)
        button_reciprocal.config(state=DISABLED)
        button_square.config(state=DISABLED)
        button_root.config(state=DISABLED)
        button_percentage.config(state=DISABLED)
        button_clear_entry.config(state=DISABLED)
        button_backspace.config(state=DISABLED)
        button_mC.config(state=DISABLED)
        button_mR.config(state=DISABLED)
        button_mP.config(state=DISABLED)
        button_mN.config(state=DISABLED)
        button_ms.config(state=DISABLED)
    else:
        current=d.get()
        d.delete(0, END)
        d.insert(0, str(current)+roundFind(element))

# Equating values
def equal():
    global num1Exist, resultShown
    result=None
    
    try:
        if math!="" and e.get()!="":
            second_number=e.get()
            e.delete(0, END)
            if math=="+":
                result=roundFind(float(f_num)+float(second_number))
            elif math=="-":
                result=roundFind(float(f_num)-float(second_number))
            elif math=="*":
                result=roundFind(float(f_num)*float(second_number))
            elif math=="/":
                result=roundFind(float(f_num)/float(second_number))
            record(second_number)
            
            e.insert(0, result)
            record("=")
            resultShown=True
            num1Exist=False
            return result
        
        elif math=="" and e.get()!="":
            current=e.get()
            d.delete(0, END)
            e.delete(0, END)
            e.insert(0, current)
            record(current)
            record("=")
            resultShown=True
            
    except ZeroDivisionError:
        e.delete(0, END)
        result="Zero Division Error!"
        e.insert(0, result)
        record("Zerror")
        num1Exist=False
    
    
    
# Arithemetic Operators
def addition():
    global num1Exist, resultShown
    
    resultShown=False
    if num1Exist==False:
        if e.get()!="":
            first_num=e.get()
            global f_num
            global math
            math="+"
            f_num=float(first_num)
            num1Exist=True
            d.delete(0, END)
            e.delete(0, END)
            record(f_num)
            record(math)
    else:
        f_num=equal()
        d.delete(0, END)
        e.delete(0, END)
        math="+"
        record(f_num)
        record(math)
    
def subtraction():
    global num1Exist, resultShown
    
    resultShown=False
    if num1Exist==False:
        if e.get()!="":
            first_num=e.get()
            global f_num
            global math
            math="-"
            f_num=float(first_num)
            num1Exist=True
            d.delete(0, END)
            e.delete(0, END)
            record(f_num)
            record(math)
    else:
        f_num=equal()
        d.delete(0, END)
        e.delete(0, END)
        math="-"
        record(f_num)
        record(math)

def multiplication():
    global num1Exist, resultShown
    
    resultShown=False
    if num1Exist==False:
        if e.get()!="":
            first_num=e.get()
            global f_num
            global math
            math="*"
            f_num=float(first_num)
            num1Exist=True
            d.delete(0, END)
            e.delete(0, END)
            record(f_num)
            record(math)
    else:
        f_num=equal()
        d.delete(0, END)
        e.delete(0, END)
        math="*"
        record(f_num)
        record(math)
    
def division():
    global num1Exist, resultShown
    
    resultShown=False
    if num1Exist==False:
        if e.get()!="":
            first_num=e.get()
            global f_num
            global math
            math="/"
            f_num=float(first_num)
            num1Exist=True
            d.delete(0, END)
            e.delete(0, END)
            record(f_num)
            record(math)
    else:
        f_num=equal()
        d.delete(0, END)
        e.delete(0, END)
        math="/"
        record(f_num)
        record(math)
        
   
    
# x related
def reciprocal():
    try:
        if e.get()!="":
            current=float(e.get())
            e.delete(0, END)
            e.insert(0, roundFind(1/current))
            
    except ZeroDivisionError:
        e.delete(0, END)
        result="Zero Division Error!"
        e.insert(0, result)
        record("Zerror")

def square():
    if e.get()!="":
        current=float(e.get())
        e.delete(0, END)
        e.insert(0, roundFind(current**2))
    
def square_root():
    if e.get()!="":
        current=float(e.get())
        e.delete(0, END)
        e.insert(0, roundFind(current**0.5))
    
    
    
# Tweak number
def negate():
    if e.get()!="":
        current=-float(e.get())
        e.delete(0, END)
        e.insert(0, roundFind(current))
    
def decimal():
    if e.get()!="":
        current=e.get()
        if "." not in e.get():
            current=e.get()+"."
        e.delete(0, END)
        e.insert(0, str(current))

def percent():
    if e.get()!="":
        if math!="":
            current=float(e.get())
            e.delete(0, END)
            e.insert(0, str(current/100))
        else:
            e.delete(0, END)
  
  
  
# Functions      
def ce():
    e.delete(0, END)
    
def ac():
    global memory
    e.delete(0, END)
    d.delete(0, END)
    global f_num, second_number, num1Exist, resultShown
    f_num=""
    second_number=""
    num1Exist=False
    resultShown=False
    button_0.config(state=ACTIVE)
    button_1.config(state=ACTIVE)
    button_2.config(state=ACTIVE)
    button_3.config(state=ACTIVE)
    button_4.config(state=ACTIVE)
    button_5.config(state=ACTIVE)
    button_6.config(state=ACTIVE)
    button_7.config(state=ACTIVE)
    button_8.config(state=ACTIVE)
    button_9.config(state=ACTIVE)
    button_divide.config(state=ACTIVE)
    button_multiply.config(state=ACTIVE)
    button_minus.config(state=ACTIVE)
    button_add.config(state=ACTIVE)
    button_equal.config(state=ACTIVE)
    button_negate.config(state=ACTIVE)
    button_decimal.config(state=ACTIVE)
    button_reciprocal.config(state=ACTIVE)
    button_square.config(state=ACTIVE)
    button_root.config(state=ACTIVE)
    button_percentage.config(state=ACTIVE)
    button_clear_entry.config(state=ACTIVE)
    button_backspace.config(state=ACTIVE)
    try:
        if memory!=0:
            button_mC.config(state=ACTIVE)
            button_mR.config(state=ACTIVE)
    except NameError:
        button_mC.config(state=DISABLED)
        button_mR.config(state=DISABLED)
    button_mP.config(state=ACTIVE)
    button_mN.config(state=ACTIVE)
    button_ms.config(state=ACTIVE)
    
def backspace():
    if e.get()!="":
        current=e.get()
        e.delete(0, END)
        for i in range(len(current)-1):
            e.insert(END, current[i])
            
def MC():
    global memory
    memory=0
    button_mC.config(state=DISABLED)
    button_mR.config(state=DISABLED)
    
def MR():
    global memory
    e.delete(0, END)
    memory=roundFind(memory)
    e.insert(0, str(memory))
    
def MP():
    global memory
    if e.get()!="":
        memory=memory+float(e.get())
        button_mC.config(state=NORMAL)
        button_mR.config(state=NORMAL)

def MN():
    global memory
    if e.get()!="":
        memory=memory-float(e.get())
        button_mC.config(state=NORMAL)
        button_mR.config(state=NORMAL)

def MS():
    global memory
    if e.get()!="":
        memory=float(e.get())
        button_mC.config(state=NORMAL)
        button_mR.config(state=NORMAL)
            
    
    
#Buttons
button_1=Button(root, text="1", padx=40, pady=20, command=lambda: click(1), borderwidth=2)
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: click(2), borderwidth=2)
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: click(3), borderwidth=2)
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: click(4), borderwidth=2)
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: click(5), borderwidth=2)
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: click(6), borderwidth=2)
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: click(7), borderwidth=2)
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: click(8), borderwidth=2)
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: click(9), borderwidth=2)
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: click(0), borderwidth=2)

button_negate=Button(root, text="+/-", padx=34, pady=20, command=negate, borderwidth=2)
button_decimal=Button(root, text=".", padx=41, pady=20, command=decimal, borderwidth=2)

button_add=Button(root, text="+", padx=39, pady=20, command=addition, borderwidth=2)
button_minus=Button(root, text="-", padx=40, pady=20, command=subtraction, borderwidth=2)
button_multiply=Button(root, text="*", padx=40, pady=20, command=multiplication, borderwidth=2)
button_divide=Button(root, text="/", padx=40, pady=20, command=division, borderwidth=2)

button_reciprocal=Button(root, text="⅟x", padx=37, pady=20, command=reciprocal, borderwidth=2)
button_square=Button(root, text="x²", padx=38, pady=20, command=square, borderwidth=2)
button_root=Button(root, text="√x", padx=36, pady=20, command=square_root, borderwidth=2)

button_percentage=Button(root, text="%", padx=38, pady=20, command=percent, borderwidth=2)

button_clear_entry=Button(root, text="CE", padx=36, pady=20, command=ce, borderwidth=2)
button_clear=Button(root, text="AC", padx=35, pady=20, command=ac, borderwidth=2)
button_backspace=Button(root, text="<⊏", padx=33, pady=20, command=backspace, borderwidth=2)
button_equal=Button(root, text="=", padx=39, pady=20, command=equal, borderwidth=2)

button_mC=Button(root, text="MC", padx=34, pady=20, command=MC, borderwidth=2, state=DISABLED)
button_mR=Button(root, text="MR", padx=34, pady=20, command=MR, borderwidth=2, state=DISABLED)
button_mP=Button(root, text="M+", padx=34, pady=20, command=MP, borderwidth=2)
button_mN=Button(root, text="M-", padx=34, pady=20, command=MN, borderwidth=2)
button_ms=Button(root, text="MS", padx=34, pady=20, command=MS, borderwidth=2)



#Buttons Placement
button_mC.grid(row=2, column=0)
button_mR.grid(row=2, column=1)
button_mP.grid(row=2, column=2)
button_mN.grid(row=2, column=3)
button_ms.grid(row=2, column=4)

button_percentage.grid(row=3, column=0)
button_clear_entry.grid(row=3, column=1)
button_clear.grid(row=3, column=2)
button_backspace.grid(row=3, column=3)

button_reciprocal.grid(row=4, column=0)
button_square.grid(row=4, column=1)
button_root.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)
button_multiply.grid(row=5, column=3)

button_4.grid(row=6, column=0)
button_5.grid(row=6, column=1)
button_6.grid(row=6, column=2)
button_minus.grid(row=6, column=3)

button_1.grid(row=7, column=0)
button_2.grid(row=7, column=1)
button_3.grid(row=7, column=2)
button_add.grid(row=7, column=3)

button_negate.grid(row=8, column=0)
button_0.grid(row=8, column=1)
button_decimal.grid(row=8, column=2)

button_equal.grid(row=8, column=3)


root.mainloop()