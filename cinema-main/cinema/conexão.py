import sqlite3
from sqlite3 import Error

from classes.Combo import Combo

class conexao():
    def __init__(self, db_file='cinema-main\cinema\BancoCinemaBD.db'):
        self.conn = sqlite3.connect(db_file)
    
