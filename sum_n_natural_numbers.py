# sum of n natural numebrs

initial = 1
sum = 0 
n = int(input("Enter the number to calculate sum: "))
while initial <= n:
    for i in range(n):
        sum = sum + initial
        initial += 1
        #print("sum is: ",sum)
    print("result =",sum)

        
