# In routing.py
from channels.routing import route, include
from geometry.routing import chat_routing

channel_routing = [
    include(chat_routing, path=r'^/ws/chat')
]