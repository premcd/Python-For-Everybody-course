filename = input('enter file name')
fhandle = open(filename)

mail_list = list()
count = 0

for line in fhandle:
    if not line.startswith('From'): #could have used l[0] != 'From' - this way it's only 1 if
        continue
    if line.startswith('From:'):
        continue
    print(line.rstrip())
    l = line.split()
    mail_list.append(l[1])
    count = count+1
for mail in mail_list:
    print(mail)
print('There were', count, 'lines in the file with From as the first word')
