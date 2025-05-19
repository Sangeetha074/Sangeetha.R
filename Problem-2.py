a=int(input("enter value of a:"))

odd_numbers=[2*i-1 for i in range(1,a+1)]
print(','.join(map(str,odd_numbers)))

