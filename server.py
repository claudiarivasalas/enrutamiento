from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

#Localhost:5000/dojo: haz que diga "¡Dojo!"
@app.route('/dojo')   
def Dojo():      
    return "¡Dojo!"

#localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
@app.route('/repeat')   
def Repite():      
    return "¡Dojo!"

#localhost:5000/say/flask: haz que diga "¡Hola, Flask!"
@app.route('/say/flask')   
def hola_flask():      
    return "¡Hola, Flask!"

@app.route('/hola/<name>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def hola(name):
    print(name)
    return "Hola, " + name

#localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
# @app.route('/repeat/<int:numero>/<string:palabra>')   
# def repite_hola(numero,palabra):      
#     #return f"¡Hola {palabra * numero}"
#     return "Hola, " + palabra * numero

#localhost:5000/repeat/80/bye: haz que diga "adiós" 80 veces
@app.route('/repeat/<int:numero>/<string:palabra>')   
def repite_bye(numero,palabra):      
    #return f"¡Hola {palabra * numero}"
    return palabra * numero

#localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces
# @app.route('/repeat/<int:numero>/<string:palabra>')   
# def repite_dogs(numero,palabra):      
#     #return f"¡Hola {palabra * numero}"
#     return "Hola, " + palabra * numero

if __name__=="__main__":  # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)
