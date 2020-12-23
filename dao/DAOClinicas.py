import pymysql

class DAOClinicas:
    def connect(self):
        return pymysql.connect("localhost","root","","uirusu" )

    def read(self, id):
        con = DAOClinicas.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM clinicas order by Nombre asc")
            else:
                cursor.execute("SELECT * FROM clinicas where id = %s order by Nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()