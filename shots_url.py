# --- Shots_URL --- a URL Shortener application designed by Kumara


from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import *

from tkinter import messagebox
import random
import string

root = Tk()
# Giving Title to the root window
root.title("Shots-URL")
# Setting the window width, height and position on the user screen
root.geometry("600x400+400+150")
# This makes a non-resizable window
root.resizable(0, 0)

# Assigning the image as an object of PhotoImage class.
p1 = PhotoImage(file="logo.png")
# Setting icon to the window using iconphoto() method
root.iconphoto(False, p1)


# Function which is triggered by the clear_all_button
def clear_all_entry():
    entry_label1.delete(0, END)
    entry_label3.delete(0, END)
    entry_variable2.set("")
    # clears all values from entries


# Function which is triggered by the copy_button and it copies the output of entry_label2 to clipboard.
def clear_all_copy():
    if entry_variable2.get() == "":
        messagebox.showerror(
            "Error", "Sorry, there is no URL to copy")
        return
        # if there is no value to copy it shows the above message.

    value_entry_label2 = entry_variable2.get()
    root.clipboard_clear()  # clear clipboard contents
    root.clipboard_append(value_entry_label2)

    # This creates a new button which clears the all the entries with the help of clear_all_entry funtion
    clear_all_button = Button(root, text="Clear all",
                              width=8, style="W.TButton", command=clear_all_entry)
    clear_all_button.place(relx=0.8, rely=0.33, anchor=CENTER)

    # This button automatically destroys in 10 seconds
    clear_all_button.after(10000, clear_all_button.destroy)


# Function which is triggered by the create_button
def create_custom_copy():
    if entry_variable3.get() == "":
        messagebox.showerror(
            "Required", "Please enter custom name and try again")
        return
        # if the entry is empty it shows the above message.

    entry4 = entry_variable3.get()
    # Creates new url by adding the user's custom input with the generated random alphabets
    entry_variable2.set("https://"+str(entry4)+"/" + str(random_letter1)+str(random_letter2) +
                        str(random_letter3)+str(random_letter4)+str(random_letter5)+str(random_letter6))


# Function which is triggered by the entry_label3 and this creates a string of giving hint to the user what to type inside it
def label_custom(event):
    label3 = Label(root, text="( eg : https://Shots_URL.in/ABCDF , you can get this by type 'Shots_URL.in' ", font=(
        "montserrat", 8, "bold", "italic"), background="#C9DAEA", foreground="#22333B")
    label3.place(relx=0.38, rely=0.95, anchor=S)


# Function which is triggered by the shots_button
def shots_button_entry_label1():
    if entry_label1.get() == "":
        messagebox.showerror("Required", "Please paste your URL and try again")
        return
        # if the entry is empty it shows the above message.

    value_entry_label1 = entry_label1.get()
    print(value_entry_label1)
    # Creates new url by adding the predefined strings with the generated random alphabets
    entry_variable2.set(
        "http//:Shots_URL.in/" + str(random_letter1)+str(random_letter2)+str(random_letter3)+str(random_letter4)+str(random_letter5)+str(random_letter6))


# Function which is triggered by the clear_button
def clear_entry_label1():
    entry_label1.delete(0, END)


# Function which is triggered by the entry_label1
def clear(event):
    # Creating some strings, showing information
    label3 = Label(root, text="( eg : https://Shots_URL.in )", font=(
        "montserrat", 8, "bold", "italic"), background="#C9DAEA", foreground="#22333B")
    label3.place(x=245, y=20)
    label3.after(20000, label3.destroy)

    # It creates a button with function which clears the value inside the entry_label1
    clear_button = Button(root, text="Clear", width=5,
                          style="W.TButton", command=clear_entry_label1)
    clear_button.place(relx=0.2, rely=0.33, anchor=CENTER)
    clear_button.after(10000, clear_button.destroy)


# gets random alphabets for creating a new url
lower_upper_alphabet = string.ascii_letters
random_letter1 = random.choice(lower_upper_alphabet)

lower_upper_alphabet = string.ascii_letters
random_letter2 = random.choice(lower_upper_alphabet)

lower_upper_alphabet = string.ascii_letters
random_letter3 = random.choice(lower_upper_alphabet)

lower_upper_alphabet = string.ascii_letters
random_letter4 = random.choice(lower_upper_alphabet)

lower_upper_alphabet = string.ascii_letters
random_letter5 = random.choice(lower_upper_alphabet)

lower_upper_alphabet = string.ascii_letters
random_letter6 = random.choice(lower_upper_alphabet)


# Setting the background color
window_background = Canvas(root, width=600, height=400, bg="#C9DAEA")
window_background.grid()


# Creating labels using Label class and position it with one of the geometry management method
label1 = Label(root, text="paste your 'url' here", font=(
    "montserrat", 14, "bold", "italic"), background="#C9DAEA", foreground="#22333B")  # montserrat,caveat
label1.place(x=25, y=15)

label2 = Label(root, text="To make your custom URL", font=(
    "montserrat", 13, "bold", "italic"), background="#C9DAEA", foreground="#22333B")
label2.place(relx=0.22, rely=0.75, anchor=S)


# Creating entries using Entry class and position it with one of the geometry management method
entry_variable1 = StringVar()
entry_label1 = Entry(root, width=50, justify=LEFT,
                     foreground="#912F56", font=("caveat", 15, "bold"), textvariable=entry_variable1)

# Setting the primary focus to this label using focus_set() method
entry_label1.focus_set()
entry_label1.bind("<Button-1>", clear)
entry_label1.place(relx=0.5, rely=0.18, anchor=CENTER)

entry_variable2 = StringVar()
entry_label2 = Entry(root, width=40, justify=LEFT,
                     foreground="#912F56", font=("caveat", 15, "bold"), textvariable=entry_variable2, state=DISABLED)
entry_label2.place(relx=0.04, rely=0.5, anchor=W)

entry_variable3 = StringVar()
entry_label3 = Entry(root, width=36, justify=LEFT,
                     foreground="#912F56", font=("caveat", 15, "bold"), textvariable=entry_variable3)
entry_label3.bind("<Button-1>", label_custom)
entry_label3.place(relx=0.05, rely=0.85, anchor=W)


# Styling buttons
shots_button_style = Style()
shots_button_style.configure("W.TButton", font=("calibri", 15, "bold", "italic"),
                             foreground="#22333B", background="#FFF9A5")
custom_button_style = Style()
custom_button_style.configure("TButton", font=("calibri", 12, "bold", "italic"),
                              foreground="#22333B", background="#FFF9A5")

# Creating Buttons and fixing it's position
shots_button = Button(root, text="Shots-URL", width=10,
                      style="W.TButton", command=shots_button_entry_label1)
shots_button.place(relx=0.5, rely=0.33, anchor=CENTER)

copy_button = Button(root, text="copy", width=9,
                     style="W.TButton", command=clear_all_copy)
copy_button.place(relx=0.96, rely=0.5, anchor=E)

create_button = Button(root, text="create", width=10,
                       style="W.TButton", command=create_custom_copy)
create_button.place(relx=0.96, rely=0.85, anchor=E)


root.mainloop()
