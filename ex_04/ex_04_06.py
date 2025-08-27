hrs = input ("enter hours")
rate = input ("enter rate")
fh = float(hrs)
fr = float(rate)
print (fh)
print (fr)
gpay = fh * fr
print (gpay)
if fh > 40:
    reg = fh * fr
    abo = 0.5*fr*(fh-40)
    gpay = reg + abo
print ("Pay:", gpay)
#commentaire
