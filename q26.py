n = int(input("enter the number"))
reversed_number=0
while n>0:
    last_digit = n%10
    reversed_number = (reversed_number *10 +last_digit)
    n//=10
print("Reversed number:",reversed_number)    