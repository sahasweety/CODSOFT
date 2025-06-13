'''import string
import random
def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = int(input("Enter the password length\n"))
    
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    

    random.shuffle(s)
    pas = ("".join(s[0:passlen]))
    print(pas)

gen() '''

# Tkinker based GUI
import string
import random
from tkinter import *

# GUI Setup
root = Tk()
root.title("Random Password Generator Tool")
root.geometry("350x250")

# Title Label
label_title = Label(root, text="Choose the Strength of your password", fg='white', bg='black')
label_title.pack()

# Password strength choice
choice = IntVar()
rb1 = Radiobutton(root, text="Poor Password", variable=choice, value=1)
rb1.pack()
rb2 = Radiobutton(root, text="Average Password", variable=choice, value=2)
rb2.pack()
rb3 = Radiobutton(root, text="Strong Password", variable=choice, value=3)
rb3.pack()

# Space and password label
label_space = Label(root)
label_space.pack()
label_password = Label(root, text="Choose the strength of your password")
label_password.pack()

# Password length input
val = IntVar()
spinlength = Spinbox(root, from_=8, to=30, textvariable=val, width=15)
spinlength.pack()

# Password generation logic
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
advance = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))

# Callback for button click
def callback():
    result.config(text=passgen())

# Submit button
button_submit = Button(root, text="Generate Password", command=callback)
button_submit.pack(pady=10)

# Result display
result = Message(root, text="", relief=RAISED, width=200, font=(25))
result.pack(side=BOTTOM)

# Run GUI loop
root.mainloop()
