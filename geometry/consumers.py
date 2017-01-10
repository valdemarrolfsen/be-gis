import json

from channels import Group, Channel
from channels.sessions import channel_session

def _close_reply_channel(message):
    message.reply_channel.send({'close': True})

# Connected to websocket.connect
@channel_session
def ws_add(message, room):
    message.channel_session['room'] = room
    Group("chat-{0}".format(room)).add(message.reply_channel)


@channel_session
def ws_message(message):
    # Stick the message onto the processing queue
    Channel("chat-messages").send({
        "room": message.channel_session['room'],
        "text": message.text,
        "user_id": message.user.id
    })


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    room = message.channel_session.get('room')
    # Check for the room. This is not set if the connection failed due to the validation of the JWT token.
    # Simply return. As the message is not in any group.
    if not room:
        return

    Group("chat-{0}".format(room)).discard(message.reply_channel)
