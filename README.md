
# Pixie Whatsapp

It is project for create with python a bot for whatsapp

![Captura de pantalla 2024-06-19 a la(s) 12 45 50](https://github.com/PiConsulting/whatsapp_bot/assets/72234490/c26c8763-2d2e-4add-a618-7cf8caa61c66)

## Clone repo

```bash
git clone https://github.com/PiConsulting/wp-pixie-whatsapp
```

## Development

```bash
  cd /wp-pixie-whatsapp

  virtualenv -p 3.10.11 .venv
  source .venv/bin/activate

  pip install -r requirements.txt
  
  python app.py

  # for running server for tunel in https for default with serveo
  # This project not run in http for Meta Developers API
  ssh -R 80:localhost:8000 serveo.net
```
