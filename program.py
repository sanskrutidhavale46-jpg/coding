n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()





n=4
for i in range(1,n+1):
    print("* " *i)





n=5
for i in range(n):
    print("* "*n)     

     





n=10
for i in range(n,0,-1):
    print("* "*i)







n=1
for i in range(1,5):
    for i in range(i):
        print(n,end=" ")
        n+=1
    print()        







n=11
sum=0
for i in range(1,n):
    sum=sum+1
print(sum)





n=int(input("Enter a number:"))
a=0
b=1

for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
