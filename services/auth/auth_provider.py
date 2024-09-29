from dotenv import load_dotenv
import os

load_dotenv()
auth_email = os.getenv('email')
auth_password = os.getenv('password')

def authenticate(email, password):
    if email == auth_email and password == auth_password:
        return {
            'username': 'admin',
            'email': 'dev@vqlion.fr',
            'roles': []
        }
    else:
        return False