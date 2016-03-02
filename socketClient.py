__author__ = 'Kibur'

# Basic chat client for testing

from socketIO_client import SocketIO, BaseNamespace
import time, threading

class BackgroundWorker(threading.Thread):
    def getObject(self):
        return self._obj

    def getWait(self):
        return self._wait

    def run(self):
        while not self.stopped():
            try:
                time.sleep(self._wait)
                self.doWork()
            except:
                raise
                self.stop()

        self._obj.disconnect()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def __init__(self, w, obj):
        self._wait = w
        self._obj = obj

        super(BackgroundWorker, self).__init__()
        self._stop = threading.Event()

    def doWork(self):
        value = raw_input()
        if value == '/leave': self.stop()
        else: self._obj.send_chat_message(value)

class ChatNamespace(BaseNamespace):
    def on_connect(self):
        print '[Connected]'

        global writeMessages
        writeMessages = BackgroundWorker(1, self)
        writeMessages.daemon = False
        writeMessages.start()

    def on_disconnect(self):
        print '[Disconnected]'
        socketIO.disconnect()

    def on_chat_message(self, data):
        print data

    def send_chat_message(self, data):
        self.emit('chat_message', data)

if __name__ == '__main__':
    writeMessages = None

    socketIO = SocketIO('http://localhost', 8080)
    chat_namespace = socketIO.define(ChatNamespace, '/chat')

    socketIO.wait(for_connect=True, seconds=1)
    writeMessages.join()
