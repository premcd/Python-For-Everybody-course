# store the text file given by the user into a variable
file_name = input ('what is the name of the file?')
#store the file handle (giving access to the content of the file) to a variable
fhandle = open(file_name)

#create the list that will contain all the words once - it is empty first
word_list =list()

#create a loop to go through the lines of the file
for line in fhandle:
    #display each line of the file, without newline characters
    print(line.rstrip())
    #create a list containing all the  words of that line
    words = line.split()

    #go through each word of that list and compare it with word_list (the list that will contain all the words once)
    for word in words:
        #if the word is already in the list, skip and go to next word
        if word in word_list:
            continue
        #if word is not already in the list, append this word to the word_list
        word_list.append(word)
        #sort the words of word_list
        word_list.sort()
        
print(word_list)
