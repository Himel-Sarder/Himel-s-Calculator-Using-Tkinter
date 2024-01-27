from tkinter import *

root = Tk()
root.title("Himel's Calculator")
root.maxsize(230, 330)

myEntry = Entry(root, bd=5, width=30, bg="Gray")
myEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=15)  # Span across three columns

def buttonClick(number):
    current = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, str(current) + str(number))

def buttonClear():
    myEntry.delete(0, END)

def buttonADD():
    first_number = myEntry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    myEntry.delete(0, END)

def buttonSub():
    first_number = myEntry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    myEntry.delete(0, END)

def buttonMul():
    first_number = myEntry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    myEntry.delete(0, END)

def buttonDiv():
    first_number = myEntry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    myEntry.delete(0, END)

def buttonPercentage():
    first_number = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, float(first_number) / 100)

def buttonPoint():
    current = myEntry.get()
    if "." not in current:
        myEntry.insert(END, ".")
def buttonEqual():
    second_number = myEntry.get()
    myEntry.delete(0, END)

    if math == "addition":
        result = f_num + float(second_number)
    elif math == "subtraction":
        result = f_num - float(second_number)
    elif math == "multiplication":
        result = f_num * float(second_number)
    elif math == "division":
        result = f_num / float(second_number)

    if result.is_integer():
        myEntry.insert(0, str(int(result)))
    else:
        myEntry.insert(0, str(result))

# Define buttons
myButton7 = Button(root, text="7", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("7"))
myButton8 = Button(root, text="8", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("8"))
myButton9 = Button(root, text="9", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("9"))
myButton4 = Button(root, text="4", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("4"))
myButton5 = Button(root, text="5", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("5"))
myButton6 = Button(root, text="6", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("6"))
myButton1 = Button(root, text="1", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("1"))
myButton2 = Button(root, text="2", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("2"))
myButton3 = Button(root, text="3", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("3"))

myButtonADD = Button(root, text="+", padx=29, pady=10, bg="Gray", command=buttonADD)
myButtonSub = Button(root, text="-", padx=31, pady=10, bg="Gray", command=buttonSub)
myButtonMul = Button(root, text="*", padx=30.5, pady=10, bg="Gray", command=buttonMul)

myButtonDiv = Button(root, text="/", padx=31, pady=10, bg="Gray", command=buttonDiv)
myButtonPercentage = Button(root, text="%", padx=29, pady=10, bg="Gray", command=buttonPercentage)
myButtonPoint = Button(root, text=".", padx=30.5, pady=10, bg="Gray", command=buttonPoint)

myButton0 = Button(root, text="0", padx=30, pady=10, bg="Gray", command=lambda: buttonClick("0"))
myButtonC = Button(root, text="C", padx=29, pady=10, bg="Gray", command=buttonClear)
myButtonE = Button(root, text="=", padx=29, pady=10, bg="Gray", command=buttonEqual)

# Add buttons to the grid
myButton7.grid(row=1, column=0)
myButton8.grid(row=1, column=1)
myButton9.grid(row=1, column=2)
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButton1.grid(row=3, column=0)
myButton2.grid(row=3, column=1)
myButton3.grid(row=3, column=2)

myButtonADD.grid(row=4, column=0)
myButtonSub.grid(row=4, column=1)
myButtonMul.grid(row=4, column=2)

myButtonDiv.grid(row=5, column=0)
myButtonPercentage.grid(row=5, column=1)
myButtonPoint.grid(row=5, column=2)

myButton0.grid(row=6, column=0)
myButtonC.grid(row=6, column=1)
myButtonE.grid(row=6, column=2)

root.mainloop()


#Himel Sarder
#Dept. of CSE, BSFMSTU
#LinkedIn : https://www.linkedin.com/in/himel-sarder/
