from tkinter import *
from tkinter import simpledialog, messagebox

app = Tk()
app.title("A simple GUI app")

# Set a custom color scheme
app.configure(bg='#E0E0E0')
label_color = '#333333'
button_color = '#4CAF50'
entry_color = '#FFFFFF'

app.geometry("500x400+400+200")

# Function to calculate the golden ratio
def get_info():
    user_input = E1.get()
    try:
        fiblist = [0, 1]
        for i in range(0, int(user_input)):
            fiblist.append(fiblist[i] + fiblist[i + 1])
        g_ratio = [fiblist[i] / float(fiblist[i - 1]) for i in range(2, len(fiblist))]
        result_label.config(text="Golden ratio is: " + str(g_ratio))
    except ValueError:
        result_label.config(text="Invalid input. Enter a number.")

# Function to handle list operations
def list_entry():
    try:
        n = int(iterations.get())
        make_list(n)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

# Function to create a list
def make_list(n):
    l = [" "]*n
    update_listbox(l)

# Function to update the listbox
def update_listbox(u_list):
    listbox.delete(0, END)
    for i in u_list:
        listbox.insert(END, i)

# Function to append a value to the list
def append_value():
    val = input_entry.get()
    l.append(val)
    update_listbox(l)

# Function to insert a value into the list
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

# Function to remove a value from the list
def remove_value():
    global l
    index = listbox.curselection()
    if index:
        index = index[0]
        del l[index]
        update_listbox(l)
    else:
        messagebox.showerror("Error", "Please select an item in the listbox.")

# Labels and buttons with the updated style
L1 = Label(app, text="Numerical Input for Golden Ratio", bg=label_color, fg='white', font=('Arial', 12))
L1.pack(pady=20)

B1 = Button(app, text="Calculate Golden Ratio", command=get_info, bg=button_color, fg='white', font=('Arial', 12))
B1.pack(pady=20)

E1 = Entry(app, bg=entry_color, font=('Arial', 12))
E1.pack(pady=20)

result_label = Label(app, text="", bg=label_color, fg='white', font=('Arial', 12))
result_label.pack()

iter_label = Label(app, text="Number of iterations:", bg=label_color, fg='white', font=('Arial', 12))
iter_label.pack()

iterations = Entry(app, bg=entry_color, font=('Arial', 12))
iterations.pack()

done = Button(app, text="Done", command=list_entry, bg=button_color, fg='white', font=('Arial', 12))
done.pack()

listbox = Listbox(app)
listbox.pack(pady=10)

input_label = Label(app, text="Enter a value:", bg=label_color, fg='white', font=('Arial', 12))
input_label.pack()

input_entry = Entry(app, bg=entry_color, font=('Arial', 12))
input_entry.pack()

append = Button(app, text="Append Value", command=append_value, bg=button_color, fg='white', font=('Arial', 12))
append.pack()

insert = Button(app, text="Insert Value", command=insert_value, bg=button_color, fg='white', font=('Arial', 12))
insert.pack()

remove = Button(app, text="Remove Value", command=remove_value, bg=button_color, fg='white', font=('Arial', 12))
remove.pack()

l = []
app.mainloop()
