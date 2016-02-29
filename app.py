__author__ = 'Kibur'

# Running Flask server

import os
from hello_world import app, socketio

socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
