import os

##This gives us the ability to have the secret key be usable easily, flask needs it for 
## user input sometimes or it breaks. TODO more research
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'just-a-random-key-:)'
