from tkinter import *

#Create New Window

window = Tk()
window.title("Miles to Km Converter")
window.minsize(150,100)

def convert_miles_to_km():
    miles = int(miles_entry.get())
    km = miles*1.61
    #change km result
    Km_result_label.config(text = str(km) )
#Labels
equal_label = Label(text = "equals:")
equal_label.grid(row=1, column = 0)

miles_label = Label(text= "Miles")
miles_label.grid(row=0, column = 2)

Km_label = Label(text="Km")
Km_label.grid(row=1,column=2)

#result
Km_result_label = Label(text = "0")
Km_result_label.grid(row=1, column=1)


#Miles Entry
miles_entry = Entry(width=10)
miles_entry.insert(END, string = "0")
miles_entry.grid(row=0, column=1)

#Calc Button
calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()