a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
lcm = a
while lcm % b != 0:
    lcm += a  
print("The LCM is:", lcm)
