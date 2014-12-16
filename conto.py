__author__ = 'acherubini'


class Conto:

    def __init__(self,nome,saldo=0):
        self.nome = nome
        self.saldo = saldo
        self.ops = []

    def preleva(self,importo):
        pass

    def versa(self,importo):
        pass

    def trasferisci(self,importo, src, dest):
        pass

    class Operazione:

        def __init__(self,data=datetime.date.today(),descrizione='',dare=0,avere=0):
            pass








