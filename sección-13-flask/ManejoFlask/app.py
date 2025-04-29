from flask import Flask, render_template, request, redirect, url_for
from cliente import Cliente
from cliente_dao import ClienteDAO

app = Flask(__name__)
titulo_app = 'Zona Fit HFD'

@app.route('/')
@app.route('/index.html')
def index():
    # Obtener todos los clientes de la base de datos
    clientes = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app, miembros=clientes)

@app.route('/guardar', methods=['POST'])
def guardar():
    # Obtener datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    membresia = int(request.form['membresia'])
    
    # Crear nuevo cliente (sin ID, la base de datos lo asignará)
    nuevo_cliente = Cliente(nombre = nombre, apellido = apellido, membresia = membresia)
    
    # Insertar en la base de datos
    ClienteDAO.insertar(nuevo_cliente)
    
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        membresia = int(request.form['membresia'])
        
        # Crear objeto cliente con los datos actualizados
        cliente = Cliente(id=id, nombre=nombre, apellido=apellido, membresia=membresia)
        
        # Actualizar en la base de datos
        ClienteDAO.actualizar(cliente)
        return redirect(url_for('index'))
    else:
        # Para GET, necesitamos obtener el cliente de la base de datos
        # Como no tenemos un método para obtener un cliente por ID en ClienteDAO,
        # obtenemos todos y filtramos
        clientes = ClienteDAO.seleccionar()
        cliente = next((c for c in clientes if c.id == id), None)
        
        if cliente is None:
            return redirect(url_for('index'))
        
        return render_template('editar.html', titulo=titulo_app, miembro=cliente)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    # Crear un objeto cliente solo con el ID para eliminar
    cliente = Cliente(id=id)
    
    # Eliminar de la base de datos
    ClienteDAO.eliminar(cliente)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)