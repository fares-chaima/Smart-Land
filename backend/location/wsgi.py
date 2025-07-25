import os
import sys
import py_eureka_client.eureka_client as eureka_client
from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'location.settings')

application = get_wsgi_application()

EUREKA_SERVER = "http://127.0.0.1:8087/"  # Adresse de Eureka Server
APP_NAME = "location-service"
PORTS = [8004, 8005, 8006]

for port in PORTS:
    eureka_client.init(
        eureka_server=EUREKA_SERVER,
        app_name=APP_NAME,
        instance_host="127.0.0.1",
        instance_port=port
    )
    print(f"✅ Instance {APP_NAME} enregistrée sur le port {port} !")
