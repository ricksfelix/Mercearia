from tkinter import *
from Database import Database

def cad():
    user = et_user.get()
    passw = et_passw.get()
    Database.cad(user, passw)
    print(Database.cad(user, passw))
    result['text'] = 'Cadastrado Com Sucesso!'
    result['fg'] = 'green'
    et_user.delete(0, END)
    et_passw.delete(0, END)

def login():
    user = et_user.get()
    passw = et_passw.get()
    if (user, passw) == ('admin', '123'):
        et_user.delete(0, END)
        et_passw.delete(0, END)
        result['text'] = 'Cadastrar Novo Usuario E Senha'
        result['fg'] = 'green'
        bt['text'] = 'Cadastrar'
        bt['command'] = 'cad'
    else:
        result['text'] = 'Incorreto!'
        result['fg'] = 'red'

root = Tk()
Label(root, text='User: ').grid(row=0, column=0)
Label(root, text='Passw: ').grid(row=1, column=0)

et_user = Entry(root)
et_passw = Entry(root, show='*')
result = Label(root, text='Voce Precisa Logar Antes de\n Cadastrar')
bt = Button(root, text='Login', command=login)

et_user.grid(row=0, column=1)
et_passw.grid(row=1, column=1)
result.grid(row=2, columnspan=2, sticky=W+E)
bt.grid(row=3, columnspan=2, sticky=W+E)
root.title("Cadastro")
root.mainloop()
