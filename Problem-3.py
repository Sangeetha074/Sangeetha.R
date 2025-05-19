a=int(input("enter value of a:"))
if a%2==0:
    a-=1
odd_numbers=[2*i-1 for i in range(1,a+1)]
print(','.join(map(str,odd_numbers)))