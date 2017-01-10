# In routing.py
from channels.routing import route
from .consumers import ws_add, ws_disconnect, ws_message

chat_routing = [
    route("websocket.connect", ws_add, path=r"^/(?P<room>[0-9]+)/$"),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect)
]
