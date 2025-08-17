Se genero un proyecto para mostrar conocimiento de DJango.
Para esto creamos dos aplicaciones como llmara este framewor a los directorios:
libro:
    contiene lo solicitado en los requerimientos con dos tablas: "libro" y "editorial." (http://127.0.0.1:8000/crear_libro/ y http://127.0.0.1:8000/crear_editorial/)
    Se creo la logica para que se puedan guardar datos en la base de datos de la mismas.
    en db.sqlite3 se puede reflejar los datos que se guardan a la hora de la carga en estas tablas en las direcciones mostradas mas arriba.
    De esta forma se cumple con el punto de lo que se solicito como ejercicio.
myapp: 
    tiene la logica para mostrar manejo de rutas de un proyecto, llegando a la conclucion de que cada aplicacion maneja su rutas y despues se manda a la aplicacion main.py, que es este seria (mysite).
    de esta forma se llega a la conclucion que con esta estrucutura el archivo urls.py del main no colapse.

Por ultimo definimos como se dijo mas arriba al directorio "mysite" como el main de salida.