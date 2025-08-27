#this program asks for numbers to the user and return the biggest and the smallest of these numbers
#if it is not a number, return a message and not a traceback
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        nb = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = nb
    if largest is None:
        largest = nb
    elif nb > largest:
        largest = nb
    elif nb < smallest:
        smallest = nb 
    elif num == "done":
        break
   
print("Maximum is", largest)
print ("Minimum is", smallest)
