'''a = float(input("Enter 1st number: "))
op = input("Enter operator (+, -, *, /, %, //, ^, square): ")

if op != "square":
    b = float(input("Enter 2nd number: "))

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    print("Result:", a / b if b != 0 else "Cannot divide by zero")
elif op == '%':
    print("Result:", a % b)
elif op == '//':
    print("Result:", a // b)
elif op == '^':
    print("Result:", a ** b)
elif op == 'square':
    print("Result:", a ** 2)
else:
    print("Invalid operator")'''

from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        # Convert ^ to ** for power evaluation
        expression = equation_text.replace('^', '**')
        total = str(eval(expression))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator Program")
window.geometry("500x600")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

# Number buttons
button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

# Operator buttons
plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

# Decimal and equal buttons
decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

equal = Button(frame, text='=', height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

mod = Button(frame, text='%', height=4, width=9, font=35, command=lambda: button_press('%'))
mod.grid(row=4, column=0)

floor_div = Button(frame, text='//', height=4, width=9, font=35, command=lambda: button_press('//'))
floor_div.grid(row=4, column=1)

square = Button(frame, text='x²', height=4, width=9, font=35, command=lambda: button_press('**2'))
square.grid(row=4, column=2)

power = Button(frame, text='^', height=4, width=9, font=35, command=lambda: button_press('^'))
power.grid(row=4, column=3)

# Clear button
clear = Button(window, text='CLEAR', height=4, width=12, font=35, command=clear)
clear.pack()

window.mainloop()
