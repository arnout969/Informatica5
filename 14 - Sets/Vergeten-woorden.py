def vergeten_woorden(tekst, verplicht):
    kaas = set(tekst.split())
    woorden = kaas.intersection(verplicht)

    return len(verplicht), len(verplicht) - len(woorden), len(woorden)






print(vergeten_woorden('hello world world world', {'python', 'world', 'hello', 'java'}))
#(4, 2, 2)
print(vergeten_woorden('',{'python', 'world', 'hello', 'java'}))