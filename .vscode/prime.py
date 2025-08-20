def check_prime(n):
    if n>0:
        for num in range(2,n+1):
            if n%num==0:
                return False
            else:
                return True
    else:
        return False
for n in range(1,100):
    if check_prime(n):
        print(n,"is prime")
