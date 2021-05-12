import secrets


def private_key(p):
    secretsGenerator = secrets.SystemRandom()
    return secretsGenerator.randrange(2, p)


def public_key(p, g, private):
    return g ** private % p


def secret(p, public, private):
    return public ** private % p

