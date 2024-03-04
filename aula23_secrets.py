import secrets

random = secrets.SystemRandom()


lista = ['Felipe', 'Carol', 'Nick', 'Elimar', 'Ivanete']

print(random.choice(lista))
print(random.randrange(0, 20))
print(secrets.choice(lista))