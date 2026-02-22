#here we are again creating a dict with values of a list, but the old value is always set in the first round (c not in d)
#d[c]= 1
#alors que dans l exemple de la correction de l'exercice 09_04, on utilise oldvalue pour la first value de many[w]

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
