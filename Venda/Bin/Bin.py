from tkinter import *
from tkinter import ttk
from Database import Database
import time
time_ = time.localtime()
date = ("{}/{}/{}".format(time_[2], time_[1], time_[0]))
hour = ("{}:{}".format(time_[3], time_[4]))


def login(user, passw):
    if Database.login(user, passw):
        return True
    else:
        return False


def cargo(user):
    return Database.cargo(user)


def menu(user, cargo):
    root = Tk()
    root.title('Vendas')
    codigo = Entry(root)
    Label(root, text=("{}:{}\n{} {}".format(cargo.title(), user.title(), hour, date))).grid(row=0, columnspan=4, sticky=W+E)
    produto = ttk.Treeview(root, columns=("#0", "#1"))
    produto.heading('#0', text='Codigo')
    produto.heading('#1', text='Produto')
    produto.heading('#2', text='Quantidade')

    pagamento = ttk.Treeview(root)
    pagamento.heading('#0', text='Valor')
    codigo.grid(row=2, columnspan=2, sticky=W+E)
    total = Label(root, text='R$ 0,00')
    total.grid(row=2, column=5)

    produto.grid(row=1, columnspan=4)
    pagamento.grid(row=1, column=5)
    root.mainloop()
