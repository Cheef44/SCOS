import sqlite3
from Crypto.Hash import SHA3_512
from language import language

def check_registration():
    try:
        db = sqlite3.connect('logs/user_info.db')
        cursor = db.cursor()
        user_name = cursor.execute("SELECT user_name FROM user").fetchall()
        if user_name:
            return True
        else:
            return False
    except sqlite3.OperationalError:
        return False
    
class data_base:
    def __init__(self, user_name, password, pc_name=None):
        hash_password = SHA3_512.new(bytes(password, 'utf-8')).digest()
        self.user_name = user_name
        self.password = hash_password
        self.pc_name = pc_name
        
    def create_db_and_registration(self):
        db = sqlite3.connect('logs/user_info.db')
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS user(
            user_name TEXT,
            password TEXT,
            pc_name TEXT);
        """)
        if not check_registration():
            cursor.execute("INSERT INTO user(user_name, password, pc_name) VALUES(?, ?, ?);", (self.user_name, self.password, self.pc_name))
            cursor.close()
            db.commit()
            return language.language()['data_base']['registered']
        else:
            return language.language()['data_base']['true_reg']
    
    def login(self):
        db = sqlite3.connect('logs/user_info.db')
        cursor = db.cursor()
        if check_registration():
            password = cursor.execute("SELECT password FROM user;").fetchall()
            if str(self.password) in str(password):
                return True
            else:
                return False
        else:
            return language.language()['data_base']['false_reg']