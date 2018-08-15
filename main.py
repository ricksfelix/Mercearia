from tkinter import *
from Bin import Bin


def login():
    user = et_user.get()
    passw = et_passw.get()
    if Bin.login(user, passw):
        cargo = Bin.cargo(user)
        root.destroy()
        Bin.menu(user, cargo)
    else:
        result['fg'] = 'red'
        result['text'] = 'Usuario ou Senha Incorretos!'


root = Tk()
Label(root, text='User: ').grid(row=0, column=0)
Label(root, text='Passw: ').grid(row=1, column=0)
Button(root, text='Login', command=login).grid(row=3, columnspan=2, sticky=W+E)
result = Label(root, text='')

et_user = Entry(root)
et_passw = Entry(root, show='*')

et_user.grid(row=0, column=1)
et_passw.grid(row=1, column=1)
result.grid(row=2, columnspan=2, sticky=W+E)
root.title("Login")
root.mainloop()
