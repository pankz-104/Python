# two string as permutation of one another 

s1 = input("Enter s1 \n")
s2 = input("Enter s2 \n")

s1str = ([ord(c) for c in s1])
s2str = ([ord(c) for c in s2])
s1str.sort()
s2str.sort()
if s1str == s2str:
    print("match found")
else:
    print("no match found")
    
