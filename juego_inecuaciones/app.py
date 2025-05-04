from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de preguntas del juego con sus respuestas correctas y opciones
preguntas = [
    {"pregunta": "2x + 3 < 7", "respuesta": "x < 2", "opciones": ["x < 2", "x > 2", "x = 2"]},
    {"pregunta": "3x - 5 > 1", "respuesta": "x > 2", "opciones": ["x < 2", "x = 2", "x > 2"]},
    {"pregunta": "-2x ≤ 6", "respuesta": "x ≥ -3", "opciones": ["x ≤ -3", "x = -3", "x ≥ -3"]}
]

@app.route('/')
def index():
    """Página de inicio del juego"""
    return render_template('index.html')

@app.route('/fin_del_juego')
def fin_del_juego():
    """Página de fin de juego"""
    return render_template('fin_del_juego.html')

@app.route('/juego', methods=['GET', 'POST'])
def juego():
    """Página del juego donde se muestra la pregunta y se recibe la respuesta"""
    resultado = ''  # Variable para mostrar el resultado (correcto o incorrecto)
    nivel = int(request.args.get("nivel", 0))  # Obtener el nivel actual (0 por defecto)

    # Si el formulario ha sido enviado
    if request.method == 'POST':
        # Obtener la respuesta del usuario, limpiar espacios en blanco
        respuesta_usuario = request.form['respuesta'].strip().replace(" ", "")

        # Obtener la respuesta correcta para la pregunta actual
        correcta = preguntas[nivel]["respuesta"].replace(" ", "")

        # Comprobar si la respuesta es correcta
        if respuesta_usuario == correcta:
            resultado = "✅ ¡Correcto!"  # Si la respuesta es correcta
            nivel += 1  # Avanzar al siguiente nivel

            # Si ya no hay más preguntas (fin del juego)
            if nivel >= len(preguntas):
                return redirect(url_for('fin_del_juego'))  # Redirige a la página de fin del juego

        else:
            resultado = "❌ Incorrecto. Intenta de nuevo."  # Si la respuesta es incorrecta

    # Obtener las opciones para la pregunta del nivel actual
    opciones = preguntas[nivel]["opciones"]

    # Mostrar la pregunta y el resultado del intento
    return render_template('juego.html', pregunta=preguntas[nivel]["pregunta"], nivel=nivel, resultado=resultado, opciones=opciones)

if __name__ == '__main__':
    app.run(debug=True)
