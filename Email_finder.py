str = '''

'''

import re
list1=re.findall(r'\w+@\S+\w',str)

op=open("email_store.txt","w")

j=1
for i in list1:
    op.write(f"Email {j} : {i}\n")
    j=j+1

print(f"Email's are:{list1}")
print(f"Total Email's are:{j-1}")
op.close()
