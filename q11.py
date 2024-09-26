# n=int(input("entre the number"))
# i=1
# while i*i <=n:
#     print(i*i,end=" ")
#     i+=1



n=int(input("entre the number"))
for i in range(1,n+1):
    square=i*i
    if square <=n:
         print(square,end=" ")
    else:
        break