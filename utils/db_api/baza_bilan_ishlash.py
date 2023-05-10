import sqlite3


class Database:
    def __init__(self,baza_manzili):
        self.path_to_db = baza_manzili

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self,sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql,parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language:str = 'uz'):
        #SQL_EXAMPLE = "INSERT INTO users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO users(id, Name, email, lamguage) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):

        #SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return sql.execute(sql, parameters=parameters, fetchone=True)

    def select_type(self, **kwargs):

        #SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_menu WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)



    def delete_users(self):
        self.execute("DELETE FROM users WHERE TRUE", commit=True)

    def delete_maxsulot_from_korzinka(self, **kwargs):

        #SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "DELETE FROM myfiles_korzinka WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, commit=True)



    def user_sanash(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)


    def user_qoshish(self, ism: str,tg_id:int,date:str, fam: str = None, username:str=None):
        sql = """
           INSERT INTO myfiles_azolar(ism,fam,tg_id,username,date) VALUES(?, ?, ?, ?, ?)
           """

        self.execute(sql, parameters=(ism,fam,tg_id,username,date), commit=True)

    def select_barcha_foydalanuvchilar(self):
        sql = """
           SELECT * FROM myfiles_azolar
           """
        return self.execute(sql, fetchall=True)

    def select_barcha_menular(self):
        sql = """
              SELECT * FROM myfiles_menu
              """
        return self.execute(sql, fetchall=True)

    def select_maxsulotlar(self, **kwargs):

        #SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_maxsulot WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_maxsulot(self, **kwargs):

        #SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_maxsulot WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)


    def select_barcha_maxsulotlar(self):
        sql = """
           SELECT * FROM myfiles_maxsulot
           """
        return self.execute(sql, fetchall=True)

    def add_to_korzinka(self, ism: str,tg_id:int,nomi:str, narxi: int, rasm:str,son:int):
        sql = """
           INSERT INTO myfiles_korzinka(ism,tg_id,nomi,narxi,rasm,son) VALUES(?, ?, ?, ?, ?, ?)
           """
        self.execute(sql, parameters=(ism,tg_id,nomi,narxi,rasm,son), commit=True)

    def update_korzinka(self, son, tg_id, nomi):
        # SQL_EXAMPLE = "UPDATE myfiles_menu SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
           UPDATE myfiles_korzinka SET son=? WHERE tg_id=? and nomi=?
           """
        return self.execute(sql, parameters=(son, tg_id, nomi), commit=True)

    def select_maxsulot_from_korzinka(self, **kwargs):

        #SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "SELECT son FROM myfiles_korzinka WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_maxsulotlar_from_korzinka(self, **kwargs):

        # SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_korzinka WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

def logger(statement):
    print(f"""
    --------------------------------------------------------
    Executing:
    {statement}
    --------------------------------------------------------
""")
