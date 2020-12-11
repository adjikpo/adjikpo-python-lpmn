#coding:utf-8

import tkinter

root = tkinter.Tk()
root.geometry("500x500")
root.title("TRAINING MANAGEMENT")

# frame 2
Frame1 = Frame(root, text="TRAINING MANAGEMENT",borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

# frame 2
Frame2 = Frame(root, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

Label(Frame1, text="TRAINING MANAGEMENT").pack(padx=100, pady=100)

def menu():
    for ligne in range(5):
        Button(root, text='L%s' % (ligne), borderwidth=1).grid(row=ligne,)

Label(Frame1, menu() ).pack()

Label(Frame2, text="Result").pack(padx=10, pady=10)


root.mainloop()