from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        total = cantidad * 9000

        if 18 <= edad <= 30:
            descuento = total * 0.15
        elif edad > 30:
            descuento = total * 0.25
        else:
            descuento = 0
        total_descuento = total - descuento
        return render_template('ejercicio1.html', descuento=descuento,
                               total=total, total_descuento=total_descuento, nombre=nombre)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']
        if nombre == "juan" and contraseña == "admin":
            mensaje = "bienvenido juan"
            return render_template('ejercicio2.html', mensaje=mensaje)
        elif nombre == "pepe" and contraseña == "user":
            mensaje = "bienbenido pepe"
            return render_template('ejercicio2.html', mensaje=mensaje)
        else:
            mensaje = "contraseña incorrecta"
            return render_template('ejercicio2.html', mensaje=mensaje)



    return render_template('ejercicio2.html')




if __name__ == '__main__':
    app.run(debug=True)
