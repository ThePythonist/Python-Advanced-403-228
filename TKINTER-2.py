import tkinter


def login():
    print("Logged in successfully")


root = tkinter.Tk()
root.title('Test Window')
root.geometry("400x400")
root.resizable(width=False, height=True)
root.configure(background="#11a192")

btn = tkinter.Button(root, font=("consolas", 17, "bold"), fg="black", text="Login", command=login)
btn.pack(pady=20, padx=20, fill="x")

root.mainloop()