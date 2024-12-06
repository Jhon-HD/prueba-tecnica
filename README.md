# prueba-tecnica

Construcción de imagen docker:  
docker build --tag prueba-docker .

Ejecución:
docker run -d -p 5000:5000 prueba-docker

 Ejecución de pruebas:
 python -m unittest test_app.py
