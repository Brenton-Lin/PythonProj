import tkinter


# UNLIMITED ARGUMENTS
def add(*args):
    sum = 0
    print(args[0])
    for n in args:
        sum += n
    return sum


def calculate(n, **kwargs):
    # Dictionary of keyword arguments and their values
    # for key, value in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


# Python args and Kwargs
# Python has advanced python arguments for a wide range of inputs
# - Arguments with default values
# allows a function to be called with prefilled values for whatever is not provided.
print(calculate(2, add=3, multiply=5))
print(add(1, 2, 3, 4, 5))

# Tkinter Window init
window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=1026, height=720)

# Label component

first_label = tkinter.Label(text="First_Label", font=("Helvetica", 24, "bold"))
first_label.grid(row=0, column=0)

first_label["text"] = "New Text"


def button_clicked():
    first_label.config(text=f"{text_entry.get()}", fg="blue")


# Button
# Event listening, remember function as argument syntax
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = tkinter.Button(text="New!")
new_button.grid(row=0, column=2)

# Entry

text_entry = tkinter.Entry()
text_entry.grid(row=2, column=3)

window.mainloop()
