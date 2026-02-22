import re

filename = input('enter file name')
if len(filename) <1: filename = 'regex_sum_42.txt'
total = 0

fhandle = open(filename)
for line in fhandle:
    line.rstrip()
    nb = re.findall('[0-9]+', line)
    if len(nb) <1: continue
    for n in nb:
        total = total+int(n)
        print(nb)
        print(total)

print(total)

    
