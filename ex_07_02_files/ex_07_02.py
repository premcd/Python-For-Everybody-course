filename = input('enter file name')
fhandle =  open(filename)

count = 0
total = 0

for line in fhandle:
    #skip lines without the float we want (does not contain X-DSPAM-Confidence)
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    print (line.rstrip())

    #compute the number of lines
    count = count +1

    #compute the sum of floats
    pos = line.find(':')
    nb = float(line[pos+1:])
    total = total + nb
    #on peut mettre directement float() dans le calcul du total ci dessus  
        
print('nombre de lignes', count)
print ('total', total)
#afficher la moyenne des floats DSPAM du document
print ('Average spam confidence:', total/count)

fhandle.close()
#youpi
