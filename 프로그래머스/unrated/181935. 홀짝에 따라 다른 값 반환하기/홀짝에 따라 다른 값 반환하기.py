def solution(n):
    total = 0
    if n%2==0:
        for i in range(n+1):
            if i%2 ==0:
                total+=i**2
                
    elif n%2 !=0:
        for i in range(n+1):
            if i%2 !=0:
                total+=i
                
    return total