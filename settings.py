import os
import dotenv


dotenv.load_dotenv('.env')
LOGIN_STANDARD = os.environ['LOGIN_STANDARD']
LOGIN_LOCKED = os.environ['LOGIN_LOCKED']
LOGIN_PROBLEM = os.environ['LOGIN_PROBLEM']
LOGIN_GLITCH = os.environ['LOGIN_GLITCH']
LOGIN_LIST = [LOGIN_STANDARD, LOGIN_LOCKED, LOGIN_PROBLEM, LOGIN_GLITCH]
PASSWORD = os.environ['PASSWORD']
TOKEN = os.environ['TOKEN']

