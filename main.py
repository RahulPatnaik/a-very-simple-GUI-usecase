from tkinter import *
from tkinter import simpledialog

app = Tk()

app.geometry("400x200+400+200")

app.title("A simple GUI app")






def get_info():
       user_input = E1.get()
       try:
              fiblist = [0,1]
              for i in range(0,int(user_input)):
                     fiblist.append(fiblist[i]+fiblist[i+1])
              g_ratio = [fiblist[i]/float(fiblist[i-1]) for i in range(2, len(fiblist))]
              result_label.config(text = "Golden ratio is: " + str(g_ratio))
       except ValueError:
              result_label.config("Invalid input. Enter a number.")

def list_entry():
       try:
              n = int(iterations.get())
              make_list(n)
       except ValueError:
              messagebox.showerror("Error, enter a valid number.")

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
       index = listbox.curselection()
       if index :
               index = index[0]
               value = input_entry.get()
               l.insert(index, value)
               update_listbox(l)

def remove_value():
       index = listbox.curselection()
       if index:
              index = index[0]
              del l[index]
              update_listbox(l)
              
               
               
       
                   
                     

L1 = Label(app, text = "Numerical Input for Golden ratio")
L1.pack(pady = 20)

B1 = Button(app, text = "Enter", command = get_info)
B1.pack(pady = 20)

E1 = Entry(app, bd = 5)
E1.pack(pady = 20)

result_label = Label(app)
result_label.pack()

iter_label = Label(app, text = "Number of iterations: ")
iter_label.pack()

iterations = Entry(app, bd = 5)
iterations.pack()

done = Button(app, text = "Done", command = list_entry)
done.pack()

listbox = Listbox(app)
listbox.pack(pady = 10)

input_label = Label(app, text = "Enter a value: ")
input_label.pack()

input_entry = Entry(app, bd = 10)
input_entry.pack()

append = Button(app, text = "Append value", command = append_value)
append.pack()

insert = Button(app, text = "Insert Value", command = insert_value)
insert.pack()

remove = Button(app, text = "Remove Value", command = remove_value)
remove.pack()

l = []
