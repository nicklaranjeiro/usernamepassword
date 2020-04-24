import random
import tkinter

def generateUsername():
    with open("words.txt", 'r') as file:
        data = file.read().splitlines()

    userNumber = random.randint(0,1000)
    if random.randint(0,2) == 1:
        username = random.choice(data)
        return username + str(userNumber)
    else:
        username = random.choice(data) + random.choice(data)
        return username + str(userNumber)

def callback():
    listBox.delete(0, "end")
    username = generateUsername()
    listBox.insert("end", username)

top = tkinter.Tk()
# Creates title and size
top.title("Username Generator")
top.geometry("350x300")

L1 = tkinter.Label(top, text="")

# Creates the submit button with the command callback when it is clicked
MyButton1 = tkinter.Button(top, text="Generate", width=10, command=callback)

# Creates the listbox
listBox = tkinter.Listbox(width=40)

# Packing loads all of the thing creates above in order of how you pack them
L1.pack()
MyButton1.pack()
listBox.pack()
top.mainloop()