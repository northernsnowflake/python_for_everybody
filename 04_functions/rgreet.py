def greet(neco):
    if neco == "es":
        return 'Hola'
    elif neco == "fr":
        return 'Bonjour'
    elif neco == "de":
        return 'Gutten tag'
    else:
        return 'Hello'


print(greet('en'), 'Glenn')
print(greet('es'), 'Pablo')
print(greet('de'), 'Heinrich')
print(greet('fr'), 'Francis')