import tkinter
import random


def generatePasswords(lengthOfPasswords, numberOfPasswords):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@.'
    passwords = []
    # For loop to make number of passwords user wants
    for p in range(numberOfPasswords):
        password = ''
        # For loop to make one password
        for c in range(lengthOfPasswords):
            password += (random.choice(chars))
        # Adds to an array
        passwords.append(password)
    # The array is returned
    return passwords


def callback():
    # Deletes everything inside the listbox
    listBox.delete(0, "end")
    # Gets the length of the inputs fields
    passwordLengths = int(lengthOfPasswords.get())
    numberOfPasswords = int(numOfPasswords.get())
    # Runs it through the generate passwords function to get passwords
    passwords = generatePasswords(passwordLengths, numberOfPasswords)
    # Adds it to the list box by looping through the passwords
    for i in range(len(passwords)):
        listBox.insert("end", passwords[i])


top = tkinter.Tk()
# Creates title and size
top.title("Password Generator")
top.geometry("350x300")

# Creates the input box for length of passwords
L1 = tkinter.Label(top, text="Length of Password")
lengthOfPasswords = tkinter.Entry(top)

# Creates the input box for number of passwords
L2 = tkinter.Label(top, text="Number of Passwords")
numOfPasswords = tkinter.Entry(top)

# Creates the submit button with the command callback when it is clicked
MyButton1 = tkinter.Button(top, text="Generate", width=10, command=callback)

# Creates the listbox
listBox = tkinter.Listbox(width=40)

# Packing loads all of the thing creates above in order of how you pack them
L1.pack()
lengthOfPasswords.pack()
L2.pack()
numOfPasswords.pack()
MyButton1.pack()
listBox.pack()
top.mainloop()
