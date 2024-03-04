import secrets
import string as s
from secrets import SystemRandom as Sr

senha_10caracteres = ''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=10))

print(senha_10caracteres)
