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

def get_list_values():
       list_input = simpledialog.askstring("Input", "Enter a value: ")
       return list_input
       
def get_info2():
       user_input = E2.get()
       a = []
       for i in range(int(user_input)):
              list_value = get_list_values()
              if list_value is not None:
                     a.append(list_value)
              else:
                     break
       result_label2.config(text = "Filled list:" + str(a))  
                   
                     

L1 = Label(app, text = "Numerical Input for Golden ratio")
L1.pack(pady = 20)

B1 = Button(app, text = "Enter", command = get_info)
B1.pack(pady = 20)

E1 = Entry(app, bd = 5)
E1.pack(pady = 20)

result_label = Label(app)
result_label.pack()

L2 = Label(app, text = "How many numbers do you want a list for? ")
L2.pack(pady = 20)

E2 = Entry(app, bd = 5)
E2.pack(pady = 20)

B2 = Button(app, text = "Enter", command = get_info2)
B2.pack(pady = 20)

result_label2 = Label(app)
result_label.pack()






app.mainloop()


