import pymysql

class DAOReservas:
    def connect(self):
        return pymysql.connect("localhost","root","","uirusu" )

    def read(self, id):
        conc = DAOReservas.connect(self)
        cursorc = conc.cursor()

        try:
            if id == None:
                cursorc.execute("SELECT * FROM reservas order by Nombre asc")
            else:
                cursorc.execute("SELECT * FROM reservas where id = %s order by Nombre asc", (id,))
            return cursorc.fetchall()
        except:
            return ()
        finally:
            conc.close()

    def insert(self,data):
        conc = DAOReservas.connect(self)
        cursorc = conc.cursor()

        try:
            cursorc.execute("INSERT INTO reservas(Nombre,Apellidos,Telefono,Correo,Establecimiento,Prueba,Fecha,Horario) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (data['Nombre'],data['Apellidos'],data['Telefono'],data['Correo'],data['Establecimiento'],data['Prueba'],data['Fecha'],data['Horario'],))
            conc.commit()
            return True
        except:
            conc.rollback()
            return False
        finally:
            conc.close()

    def update(self, id, data):
        conc = DAOReservas.connect(self)
        cursorc = conc.cursor()

        try:
            cursorc.execute("UPDATE reservas set Nombre = %s, Apellidos = %s, Telefono = %s, Correo = %s, Establecimiento = %s, Prueba = %s, Fecha = %s, Horario = %s where id = %s", (data['Nombre'],data['Apellidos'],data['Telefono'],data['Correo'],data['Establecimiento'],data['Prueba'],data['Fecha'],data['Horario'],id,))
            conc.commit()
            return True
        except:
            conc.rollback()
            return False
        finally:
            conc.close()

    def delete(self, id):
        conc = DAOReservas.connect(self)
        cursorc = conc.cursor()

        try:
            cursor.execute("DELETE FROM reservas where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()