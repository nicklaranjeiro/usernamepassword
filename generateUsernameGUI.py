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
top.title("Username Generator")
top.geometry("400x300")

button = tkinter.Button(top, text="Generate", width=10, command=callback)

listBox = tkinter.Listbox(width=30)

button.pack()
listBox.pack()
top.mainloop()

