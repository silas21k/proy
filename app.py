from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOContactanos import DAOContactanos
from dao.DAOClinicas import DAOClinicas
from dao.DAOReservas import DAOReservas
from dao.DAOPagos import DAOPagos

app = Flask(__name__)
app.secret_key = "DS8"
db = DAOContactanos()
dbB=DAOClinicas()
dbc=DAOReservas()
dbd = DAOPagos()
local = '/Clinicas'
servicio = '/Contactanos'
atencion = '/Reservas'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route(local+'/')
def index():
    dataB = dbB.read(None)
    return render_template('TClinicas.html', dataB = dataB)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

@app.route(servicio+'/')
def mensaje():
    data = db.read(None)
    return render_template('Contactanos.html', data = data)

@app.route(atencion+'/')
def cita():
    datac = dbc.read(None)
    return render_template('Reservas.html', datac = datac)

@app.route(servicio+'/addmensaje', methods = ['POST', 'GET'])
def addmensaje():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Mensaje enviado satisfactoriamente")
        else:
            flash("El mensaje no se llego a enviar")

        return redirect(url_for('inicio'))
    else:
        return redirect(url_for('inicio'))

@app.route(atencion+'/addreserva', methods = ['POST', 'GET'])
def addreserva():
    if request.method == 'POST' and request.form['save']:
        if dbc.insert(request.form):
            flash("La reserva fue creada")
        else:
            flash("ERROR, no se pudo registrar su reserva")

        return redirect(url_for('deuda'))
    else:
        return redirect(url_for('deuda'))

@app.route(atencion+'/Pagos/')
def deuda():
    datad = dbd.read(None)
    return render_template('Pagos.html', datad = datad)
    
@app.route(atencion+'/addpagos', methods = ['POST', 'GET'])
def addpagos():
    if request.method == 'POST' and request.form['save']:
        if dbc.insert(request.form):
            flash("Su metodo de pago a quedado registrado")
        else:
            flash("ERROR, vuelva a ingresar su metodo de pago")

        return redirect(url_for('inicio'))
    else:
        return redirect(url_for('inicio')) 

@app.route('/Mapa',methods=['GET','POST'])
def my_maps():

  mapbox_access_token = 'pk.eyJ1Ijoic2lsYXMyMTAxIiwiYSI6ImNraWJzYjZyZTBhcXMydWxnNHcwcHF5a3MifQ.XGyMBYxnMa2Z7P8GBIqBCw'

  return render_template('Mapas.html',
        mapbox_access_token=mapbox_access_token)   

if __name__ == '__main__':
    app.run(port = 3000, host = "0.0.0.0", debug = True)
    #align="center"