"""
Simple Calculator (Tkinter GUI)
--------------------------------
A custom-built desktop calculator created using Python and Tkinter.
This calculator supports basic arithmetic operations including addition,
subtraction, multiplication, and division, with real-time display updates
and error handling.

Features:
• Fully interactive Tkinter GUI
• Handles multi-digit and decimal inputs
• Supports +, -, *, / operations
• Running calculation display (history bar)
• Zero-division error protection with UI lock
• Memory functions: MC, MR, M+, M-, MS
• Negation, square, square root, reciprocal, percentage
• Smart input system that resets after showing results

Author: Kyaw Min Khant
"""

# Tutorial by Codemy.com, continued the code as suggested to make a calculator

from tkinter import *

# Initialising
root=Tk()
root.title("Simple Calculator")

# Setting up small fram at row 2, column 0 for memory related keys
memoryFrame=Frame(root)
memoryFrame.grid(row=2, column=0, columnspan=3, sticky="w", padx=5, pady=2)

d=Entry(root, width=20, borderwidth=5, font=("Adobe-Garamond-Pro", 12)) # To show previous calculations
d.grid(row=0, column=0, columnspan=5, padx=8, pady=(8, 2), sticky="w")

e=Entry(root, width=30, borderwidth=5, font="Adobe-Garamond-Pro") # Inputs
e.grid(row=1, column=0, columnspan=5, padx=8, sticky="w")

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
    if element=="Zerror": # Zero Error Case, shut all other key except AC
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
    else: # If not record it as usual
        current=d.get()
        d.delete(0, END)
        d.insert(0, str(current)+roundFind(element))

# Equating values
def equal():
    global num1Exist, resultShown
    result=None
    
    try:
        if math!="" and e.get()!="": # If there is an arithmetic operator assigned
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
        
        elif math=="" and e.get()!="": # If there is no operations but just a number
            current=e.get()
            d.delete(0, END)
            e.delete(0, END)
            if any(op in current for op in ["+", "-", "*", "/", "^", "√"]):
                if "^" in current:
                    current2=current.replace("^", "**") # Replace ^ with ** so it can function properly
                elif "√" in current:
                    currentA=current.replace("√", "") # Temporary store 
                    current2=f"({currentA})**0.5"
                result=str(roundFind(eval(current2))) # Evaluate the equation normally if there is no power
                e.insert(0, result)
            else:
                e.insert(0, current)   
            record(current)
            record("=")
            resultShown=True
            
    except ZeroDivisionError: # Zero Error case
        e.delete(0, END)
        result="Zero Division Error!"
        e.insert(0, result)
        record("Zerror")
        num1Exist=False
    
    
    
# Arithemetic Operators
def addition():
    global num1Exist, resultShown
    
    resultShown=False
    if num1Exist==False: # If there is no first number
        if e.get()!="": # If there is an input
            first_num=e.get()
            global f_num
            global math
            math="+" # Assign the Arthmetic Operator
            f_num=float(first_num) # Number can be float
            num1Exist=True # First number now exist
            d.delete(0, END) # Clear previous record
            e.delete(0, END) # Clear input
            record(f_num) # Record the first number
            record(math) # Record the operator
    else: # If there is first number
        f_num=equal() # New first number will be the result of the calculation for further calculation
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
button_1=Button(root, text="1", width=12, height=4, command=lambda: click(1), borderwidth=2)
button_2=Button(root, text="2", width=12, height=4, command=lambda: click(2), borderwidth=2)
button_3=Button(root, text="3", width=12, height=4, command=lambda: click(3), borderwidth=2)
button_4=Button(root, text="4", width=12, height=4, command=lambda: click(4), borderwidth=2)
button_5=Button(root, text="5", width=12, height=4, command=lambda: click(5), borderwidth=2)
button_6=Button(root, text="6", width=12, height=4, command=lambda: click(6), borderwidth=2)
button_7=Button(root, text="7", width=12, height=4, command=lambda: click(7), borderwidth=2)
button_8=Button(root, text="8", width=12, height=4, command=lambda: click(8), borderwidth=2)
button_9=Button(root, text="9", width=12, height=4, command=lambda: click(9), borderwidth=2)
button_0=Button(root, text="0", width=12, height=4, command=lambda: click(0), borderwidth=2)

button_negate=Button(root, text="+/-", width=12, height=4, command=negate, borderwidth=2)
button_decimal=Button(root, text=".", width=12, height=4, command=decimal, borderwidth=2)

button_add=Button(root, text="+", width=12, height=4, command=addition, borderwidth=2)
button_minus=Button(root, text="-", width=12, height=4, command=subtraction, borderwidth=2)
button_multiply=Button(root, text="*", width=12, height=4, command=multiplication, borderwidth=2)
button_divide=Button(root, text="/", width=12, height=4, command=division, borderwidth=2)

button_reciprocal=Button(root, text="⅟x", width=12, height=4, command=reciprocal, borderwidth=2)
button_square=Button(root, text="x²", width=12, height=4, command=square, borderwidth=2)
button_root=Button(root, text="√x", width=12, height=4, command=square_root, borderwidth=2)

button_percentage=Button(root, text="%", width=12, height=4, command=percent, borderwidth=2)

button_clear_entry=Button(root, text="CE", width=12, height=4, command=ce, borderwidth=2)
button_clear=Button(root, text="AC", width=12, height=4, command=ac, borderwidth=2)
button_backspace=Button(root, text="<⊏", width=12, height=4, command=backspace, borderwidth=2)
button_equal=Button(root, text="=", width=12, height=4, command=equal, borderwidth=2)

button_mC=Button(memoryFrame, text="MC", font=("Adobe-Garamond-Pro", 8), width=7, height=2, command=MC, borderwidth=2, state=DISABLED)
button_mR=Button(memoryFrame, text="MR", font=("Adobe-Garamond-Pro", 8), width=7, height=2, command=MR, borderwidth=2, state=DISABLED)
button_mP=Button(memoryFrame, text="M+", font=("Adobe-Garamond-Pro", 8), width=7, height=2, command=MP, borderwidth=2)
button_mN=Button(memoryFrame, text="M-", font=("Adobe-Garamond-Pro", 8), width=7, height=2, command=MN, borderwidth=2)
button_ms=Button(memoryFrame, text="MS", font=("Adobe-Garamond-Pro", 8), width=7, height=2, command=MS, borderwidth=2)



#Buttons Placement
button_mC.grid(row=0, column=0, padx=1)
button_mR.grid(row=0, column=1, padx=1)
button_mP.grid(row=0, column=2, padx=1)
button_mN.grid(row=0, column=3, padx=1)
button_ms.grid(row=0, column=4, padx=1)

button_percentage.grid(row=3, column=0, padx=(5, 1))
button_clear_entry.grid(row=3, column=1)
button_clear.grid(row=3, column=2)
button_backspace.grid(row=3, column=3, padx=(1, 5))

button_reciprocal.grid(row=4, column=0, padx=(5, 1))
button_square.grid(row=4, column=1, padx=(0, 1))
button_root.grid(row=4, column=2)
button_divide.grid(row=4, column=3, padx=(1, 5))

button_7.grid(row=5, column=0, padx=(5, 1))
button_8.grid(row=5, column=1, padx=(0, 1))
button_9.grid(row=5, column=2)
button_multiply.grid(row=5, column=3, padx=(1, 5))

button_4.grid(row=6, column=0, padx=(5, 1))
button_5.grid(row=6, column=1, padx=(0, 1))
button_6.grid(row=6, column=2)
button_minus.grid(row=6, column=3, padx=(1, 5))

button_1.grid(row=7, column=0, padx=(5, 1))
button_2.grid(row=7, column=1, padx=(0, 1))
button_3.grid(row=7, column=2)
button_add.grid(row=7, column=3, padx=(1, 5))

button_negate.grid(row=8, column=0, padx=(5, 1), pady=(0, 5))
button_0.grid(row=8, column=1, padx=(0, 1), pady=(0, 5))
button_decimal.grid(row=8, column=2, pady=(0, 5))

button_equal.grid(row=8, column=3, padx=(1, 5), pady=(0, 5))


root.mainloop()
