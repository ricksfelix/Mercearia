import sqlite3
import time
time_ = time.localtime()
date = ("{}/{}/{}".format(time_[2], time_[1], time_[0]))
hour = ("{}:{}".format(time_[3], time_[4]))


########################################################################################################################
con = sqlite3.connect('Database.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Login(user text, passw text, cargo text)")
c.execute("""
CREATE TABLE IF NOT EXISTS Vendas(cargo text, user text, cod text, prod text, quant text, valor text, data text, hora text)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS PreVendas(cargo text, user text, cod text, prod text, quant text, valor text, date text, hour text)
""")
c.execute("CREATE TABLE IF NOT EXISTS Log(user text, passw text,data text,hora text)")
########################################################################################################################


########################################################################################################################
prod_con = sqlite3.connect("Estoque.db")
prod_c = prod_con.cursor()
prod_c.execute("""
CREATE TABLE IF NOT EXISTS Padaria(cod text, nome text,v_liquido text,v_bruto text, quant text)
""")
prod_c.execute("""
CREATE TABLE IF NOT EXISTS Mercearia(cod text, nome text,v_liquido text,v_bruto text, quant text)
""")
prod_c.execute("""
CREATE TABLE IF NOT EXISTS Padaria(cod text, nome text,v_liquido text,v_bruto text, quant text)
""")
########################################################################################################################


########################################################################################################################
dia_con = sqlite3.connect('{}-{}-{}.db'.format(time_[2], time_[1], time_[0]))
dia_c = dia_con.cursor()
dia_c.execute("""
CREATE TABLE IF NOT EXISTS Vendas(data text,hora text,cod text,produto text,user text)
""")
########################################################################################################################


def cad(user, passw):
    c.execute("INSERT INTO Login(user, passw, cargo) WHERE = (?,?,?)", (user, passw, 'admin'))
    con.commit()


def login(user, passw):
    c.execute("SELECT * FROM Login WHERE user = ?", (user,))
    auth = c.fetchone()
    if auth == None:
        return False
    else:
        if (user, passw) == (auth[0], auth[1]):
            return True
        else:
            return False


def cargo(user):
    c.execute("SELECT * FROM Login WHERE user = ?", (user,))
    auth = c.fetchone()
    return auth[2]


def vendas(cargo, user, cod, prod, quant, valor):
    pass
