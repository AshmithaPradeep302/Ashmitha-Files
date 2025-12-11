def solve():
    n=int(input("Enter the integer for multiplication table:"))
    i=1
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
        
solve()
