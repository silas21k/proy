import pymysql

class DAOPagos:
    def connect(self):
        return pymysql.connect("localhost","root","","uirusu" )

    def read(self, id):
        con = DAOPagos.connect(self)
        cursor2 = con.cursor()

        try:
            if id == None:
                cursor2.execute("SELECT * FROM pagos order by cvv asc")
            else:
                cursor2.execute("SELECT * FROM pagos where id = %s order by cvv asc", (id,))
            return cursor2.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,datad):
        con = DAOPagos.connect(self)
        cursor2 = con.cursor()

        try:
            cursor2.execute("INSERT INTO pagos(Via_Pago,Nro,cvv,Fecha_vencimiento,Tipo) VALUES(%s, %s, %s, %s, %s)", (data['ViadePago'],data['NTarjeta'],data['cvv'],data['FechadeVencimiento'],data['Tipo'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, datad):
        con = DAOPagos.connect(self)
        cursor2 = con.cursor()

        try:
            cursor2.execute("UPDATE pagos set Via_Pago = %s, Nro = %s, cvv = %s, Fecha_vencimiento = %s, Tipo = %s where id = %s", (data['ViadePago'],data['NTarjeta'],data['cvv'],data['FechadeVencimiento'],data['Tipo'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOPagos.connect(self)
        cursor2 = con.cursor()

        try:
            cursor2.execute("DELETE FROM pagos where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()