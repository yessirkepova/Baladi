import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import myapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frelancer.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            myapp.routing.websocket_urlpatterns
        )
    ),
})
