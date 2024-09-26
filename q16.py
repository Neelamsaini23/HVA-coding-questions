# n=int(input("enter the number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")

n=int(input("enter the number"))
i=1
while i<=n:
    if n%i==0:
        print(i ,end=" ")
    i+=1