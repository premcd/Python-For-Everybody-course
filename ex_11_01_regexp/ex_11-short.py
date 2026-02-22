import re
# l'idee ici est d'utiliser les elements suivants:
#read the file as one string: fhandle.read()
#cree une liste de matching elements using fonction re.findall() sur cette string
#use list comprehension to go through these elements (for n in l expression precedente)
#and calculate the sum of these elements using fonction sum()

filename = input('enter file name')
if len(filename) <1: filename = 'regex_sum_42.txt'
fhandle = open(filename)

print(sum([int(n) for n in re.findall('[0-9]+',fhandle.read())]))
