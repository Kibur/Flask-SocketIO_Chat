__author__ = 'Kibur'

from flask import session, request
from . import socketio
from flask_socketio import emit, send

@socketio.on('connect', namespace='/chat')
def on_connect():
    print 'Client connected to chat'
    session['clientID'] = request.sid
    emit('chat_message', session.get('clientID') + ' entered chat!', broadcast=True)
    
@socketio.on('disconnect', namespace='/chat')
def on_disconnect():
    print 'Client disconnected from chat'
    emit('chat_message', session.get('clientID') + ' left chat!', broadcast=True)
    
@socketio.on('chat_message', namespace='/chat')
def on_chat_message(data):
    emit('chat_message', session.get('clientID') + ': ' + str(data), broadcast=True)