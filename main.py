from tkinter import *
from tkinter import simpledialog, messagebox

app = Tk()
app.title("My GUI App")

app.configure(bg='#1E1E1E')
label_color = '#FFFFFF'
button_color = '#4CAF50'
entry_color = '#333333'
font_style = ('Arial', 14, 'bold')  
user_input_color = 'white'

app.geometry("700x600+300+150") 

def get_info():
    user_input = E1.get()
    try:
        fiblist = [0, 1]
        for i in range(0, int(user_input)):
            fiblist.append(fiblist[i] + fiblist[i + 1])
        g_ratio = [fiblist[i] / float(fiblist[i - 1]) for i in range(2, len(fiblist))]
        result_label.config(text="Golden ratio is: " + str(g_ratio[-1]), fg=user_input_color)
        fibonacci_label.config(text="Fibonacci series: " + str(fiblist), fg=user_input_color)
    except ValueError:
        result_label.config(text="Invalid input. Enter a number.", fg='red')

def list_entry():
    try:
        n = int(E1.get())  
        make_list(n)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

def make_list(n):
    l = [" "]*n
    update_listbox(l)

def update_listbox(u_list):
    listbox.delete(0, END)
    for i in u_list:
        listbox.insert(END, i)

def append_value():
    val = input_entry.get()
    l.append(val)
    update_listbox(l)

def insert_value():
    global l
    index = listbox.curselection()
    if index:
        index = index[0]
        value = input_entry.get()
        l.insert(index, value)
        update_listbox(l)
    else:
        messagebox.showerror("Error", "Please select an item in the listbox.")

def remove_value():
    global l
    index = listbox.curselection()
    if index:
        index = index[0]
        del l[index]
        update_listbox(l)
    else:
        messagebox.showerror("Error", "Please select an item in the listbox.")

instructions = """
Welcome to My GUI App!

1. Enter a number in the field below and click 'Calculate Golden Ratio' to see the golden ratio sequence.

2. Use the list operations section:
   - Enter a value in 'Enter a value' field.
   - Click 'Append Value' to add it to the list.
   - Select an item in the listbox and click 'Insert Value' to insert a value.
   - Select an item in the listbox and click 'Remove Value' to remove it.

Have fun exploring the app!
"""

instructions_label = Label(app, text=instructions, bg='#1E1E1E', fg=label_color, font=font_style, justify=LEFT)
instructions_label.pack(pady=15)

L1 = Label(app, text="Numerical Input for Golden Ratio", bg='#1E1E1E', fg=label_color, font=font_style)
L1.pack(pady=5)

B1 = Button(app, text="Calculate Golden Ratio", command=get_info, bg=button_color, fg='white', font=font_style, relief=FLAT)
B1.pack(pady=5)

E1 = Entry(app, bg=entry_color, font=font_style, relief=FLAT, bd=2, fg=user_input_color)
E1.pack(pady=5)

result_label = Label(app, text="", bg='#1E1E1E', fg=label_color, font=font_style)
result_label.pack()

fibonacci_label = Label(app, text="", bg='#1E1E1E', fg=label_color, font=font_style)
fibonacci_label.pack()


list_heading = Label(app, text="List Manipulation", bg='#1E1E1E', fg=label_color, font=font_style)
list_heading.pack(pady=10)

listbox = Listbox(app, bg=entry_color, font=font_style, relief=FLAT, bd=2, fg=user_input_color)
listbox.pack(pady=5)

input_label = Label(app, text="Enter a value:", bg='#1E1E1E', fg=label_color, font=font_style)
input_label.pack()

input_entry = Entry(app, bg=entry_color, font=font_style, relief=FLAT, bd=2, fg=user_input_color)
input_entry.pack(pady=5)

append = Button(app, text="Append Value", command=append_value, bg=button_color, fg='white', font=font_style, relief=FLAT)
append.pack(pady=5)

insert = Button(app, text="Insert Value", command=insert_value, bg=button_color, fg='white', font=font_style, relief=FLAT)
insert.pack(pady=5)

remove = Button(app, text="Remove Value", command=remove_value, bg=button_color, fg='white', font=font_style, relief=FLAT)
remove.pack(pady=5)

l = []
app.mainloop()
