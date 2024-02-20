# pass generator
import secrets
import string
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

root = Tk()

root.title("Password Generator")
root.geometry("300x150")

style=ttk.Style()
style.configure("BW.TLabel", foreground="white", background="blue")
label1 = ttk.Label(root, text='', width=35, borderwidth=5, style="BW.TLabel")
label1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# pass length
pwd_length = 12

# generate pass
# secrets.choice(alphabet) returns one character
# separator will be '', because we don't want whitespace
def gen():
	pwd = ''
	for i in range(pwd_length):
		pwd += ''.join(secrets.choice(alphabet))
	label1.config(text=pwd)

# with constraints: 1) one special char  2) two digits
def gen2():
	while True:
		pwd=''
		for i in range(pwd_length):
			pwd += ''.join(secrets.choice(alphabet))
		if (any(char in special_chars for char in pwd) and sum(char in digits for char in pwd)>=2):
			break
	label1.config(text=pwd)

style.map("BW.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

button_1 = ttk.Button(root, text="Simple Pass", style="BW.TButton",command=lambda: gen())
button_1.grid(row=3, column=0)

button_2 = ttk.Button(root, text="Constraints Pass", style="BW.TButton",command=lambda: gen2())
button_2.grid(row=3, column=1)


root.mainloop()