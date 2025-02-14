# Pixie WhatsApp Bot

Pixie WhatsApp es un proyecto desarrollado en Python para crear un bot de WhatsApp.

![Captura de pantalla 2024-06-19 a la(s) 12 45 50](https://github.com/PiConsulting/whatsapp_bot/assets/72234490/c26c8763-2d2e-4add-a618-7cf8caa61c66)


## 🚀 Instalación

Para empezar, clona el repositorio y configura el entorno de desarrollo.

### 1. Clonar el repositorio

```
git clone https://github.com/PiConsulting/wp-pixie-whatsapp
cd wp-pixie-whatsapp
```

### 2. Crear y activar un entorno virtual

```
virtualenv -p python3.10.11 .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```
pip install -r requirements.txt
```

#### 🛠 Uso

Ejecuta la aplicación con el siguiente comando:

```
python app.py
```

#### 🔗 Servidor HTTPS con Serveo

Este proyecto requiere HTTPS debido a las restricciones de la API de Meta Developers. Para exponer el servidor local a internet mediante Serveo, usa:

```
ssh -R 80:localhost:8000 serveo.net
```

#### 📌 Notas

Asegúrate de que tu cuenta de WhatsApp Business está configurada correctamente.

Verifica que los permisos de la API de Meta estén habilitados para tu aplicación.

#### 📜 Licencia

Este proyecto está bajo la licencia MIT.

#### 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en el repositorio.

#### 🌿 Convención para Branches

Si realizas una implementación, asegúrate de que las ramas comiencen con feature/.

##### ✨ Proyecto desarrollado por PiConsulting