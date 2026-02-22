import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall(b'\S+?@\S+?', s)
print(lst)

