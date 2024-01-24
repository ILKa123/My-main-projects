from random import randint
from tkinter import Button, Entry, Label, StringVar, Tk, mainloop  

secret = randint (1, 100)

def user_try():
    usernum = int(enpty_input.get())
    if usernum > secret:
        usernum_text.set(f"{usernum_text.get()}\n{usernum} greater than the secret")
    elif usernum < secret:
        usernum_text.set(f"{usernum} less then the secret")
    else:
        usernum_text.set(f"Congraduation!)  {usernum}  is the secret")

  


root = Tk()
root.geometry("400x400")
root.title("Guess the number")

enpty_input = StringVar()
usernum_text = StringVar()

button = Button(text="cliker", width= 10)
button.pack(pady=30)

label = Label(root, text="Your try: ")
label.place(anchor="center", relx=0.5, rely=0.2)

entry = Entry(root, textvariable=enpty_input)
entry.place(anchor="center", relx=0.5, rely=0.3)


button = Button(root, text = "Try", command=user_try)
button.place(anchor="center", relx=0.5, rely=0.4)

result = Label (root, textvariable=usernum_text)
result.place(anchor="center", relx=0.5, rely=0.8)



mainloop()
