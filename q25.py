n = int(input("Enter the number: "))  
a = 0  
b = 1
for i in range(n):
    if i == 0:
        print(a, end=" ")  
    elif i == 1:
        print(b, end=" ")  
    else:
        c = a + b  
        print(c, end=" ")  
        a = b  
        b = c  
