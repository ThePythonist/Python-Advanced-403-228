import tkinter

root = tkinter.Tk()
root.title('Test Window')
root.geometry("400x400")
root.resizable(width=False, height=True)
root.configure(background="#11a192")

# welcome_label = tkinter.Label(root, text='Welcome', font=("consolas", 17, "bold"), bg="#11a192", fg="white")
welcome_label = tkinter.Label(root, text='Welcome', font=("consolas", 17, "bold"), fg="black")
# welcome_label.pack(anchor="n", side="left")
welcome_label.pack(pady=20, padx=20, fill="x")

root.mainloop()
