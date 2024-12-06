# prueba-tecnica
Página:
http://127.0.0.1:5000/data

Construcción de imagen docker:  
docker build --tag prueba-docker .

Ejecución docker:
docker run -d -p 5000:5000 prueba-docker

Ejecución de pruebas:
python -m unittest test_app.py

Ruta de documentación:
http://localhost:5000/apidocs/#/
