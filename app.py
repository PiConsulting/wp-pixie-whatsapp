# Tipo de archivo: Script Py
# Nombre: app.py
# Area: Dev
# Fecha: 14/02/2025
# Autores: Sergio Casas | Juan Bravin | Andres Cuello 
# Contacto: sergio.casas@piconsulting.com.ar | jbravin@piconsulting.com.ar | andres.cuello@piconsulting.com.ar 
# Version: V1.0
# Descripcion: archivo de configuracion e inicio de Flask

from router import app

if __name__ == '__main__':
    app.run(port=5000)
