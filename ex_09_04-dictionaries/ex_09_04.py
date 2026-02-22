#filename = input ("enter the file name")
filename = 'mbox-short.txt'
fhandle = open(filename)
#this is the dict that will contain the counts for each mail sender
sender_count = dict()
#this is the list that will contain all the mail senders encountered in the file
email_list = list()

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    #guardian pattern to avoid failing due to empty line - note that lines beginning with "From:" will be skipped too 
    if len(words)<3 or words[0] != 'From':
        continue
    print(line)
    #populate the list of emails with emails found just after 'From'
    email_list.append(words[1])
    
#go though the list created to create a dictionary of counts for each element of the list
for mail in email_list:
    #it is possible here to use a variable oldvalue to get the count going for each word, but this version is shorter:
    sender_count[mail] = sender_count.get(mail,0) +1
print(sender_count)
print(email_list)

max_count = None
max_key = 0
#maybe better to use cle valeur - item - tuples to manipulate key-values here
for cle,valeur in sender_count.items():
    if max_count is None or max_count < valeur:
        max_count = valeur
        max_email = cle


#    if max_count is None:
#        max_count = sender_count[key]
#    elif max_count < sender_count[key]:
#        max_count = sender_count[key]
#        max_key = key
      
print(max_email, max_count)

        
    
    
