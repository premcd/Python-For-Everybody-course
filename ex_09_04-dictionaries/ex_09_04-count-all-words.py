#filename = input ("enter the file name")
filename = 'mbox-short.txt'
fhandle = open(filename)
#this is the dict that will contain the counts for each mail sender
words_count = dict()
#this is the list that will contain all the mail senders encountered in the file
words_list = list()

for line in fhandle:
    words = line.split()
    #here we could also start to build the dict for each line: we would not need to build a full list words_list
    print(line)
    for w in words:
        words_list.append(w)
print(words_list)
    
#go though the list of words and create a dict with their count
for word in words_list:
#it is possible here to use a variable oldvalue to get the count going for each word, but this version is shorter
    words_count[word] = words_count.get(word,0) +1
    
print(words_count)

max_count = None
for cle,valeur in words_count.items():
    if max_count is None or max_count < valeur:
        max_count = valeur
        max_word = cle


#    if max_count is None:
#        max_count = sender_count[key]
#    elif max_count < sender_count[key]:
#        max_count = sender_count[key]
#        max_key = key
      
print(max_word, max_count)
