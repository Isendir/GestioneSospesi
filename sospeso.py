__author__ = 'acherubini'

import datetime

from datetime import date

class Sospeso():

    def __init__(self,descrizione='',scadenza=datetime.date.today(),importo=0):

        self.descrizione = descrizione
        self.scadenza = scadenza
        self.importo = importo

    def __cmp__(self, other):

        if self.scadenza < other.scadenza:
            return -1
        if self.scadenza > other.scadenza:
            return 1
        if self.scadenza == other.scadenza:
            if self.importo > other.importo:
                return -1
            if self.importo < other.importo:
                return 1
            else:
                return 0


