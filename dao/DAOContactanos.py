import pymysql

class DAOContactanos:
    def connect(self):
        return pymysql.connect("localhost","root","","uirusu" )

    def read(self, id):
        con = DAOContactanos.connect(self)
        cursor1 = con.cursor()

        try:
            if id == None:
                cursor1.execute("SELECT * FROM mensaje order by Nombre asc")
            else:
                cursor1.execute("SELECT * FROM mensaje where id = %s order by Nombre asc", (id,))
            return cursor1.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOContactanos.connect(self)
        cursor1 = con.cursor()

        try:
            cursor1.execute("INSERT INTO mensaje(Nombre,Apellidos,Correo,Telefono,Mensaje) VALUES(%s, %s, %s, %s, %s)", (data['Nombre'],data['Apellidos'],data['Correo'],data['Telefono'],data['Mensaje'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOContactanos.connect(self)
        cursor1 = con.cursor()

        try:
            cursor1.execute("UPDATE mensaje set Nombre = %s, Apellidos = %s, Correo = %s, Telefono = %s, Mensaje = %s where id = %s", (data['Nombre'],data['Apellidos'],data['Correo'],data['Telefono'],data['Mensaje'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOContactanos.connect(self)
        cursor1 = con.cursor()

        try:
            cursor1.execute("DELETE FROM mensaje where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()