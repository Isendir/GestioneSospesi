__author__ = 'acherubini'
import datetime
from datetime import date
class ListaSospesi(list):

    def __init__(self):

        self.cdate = datetime.date.today()


