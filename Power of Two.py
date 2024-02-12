def power(n):
    if n==0:
        return False
    while n!=1:
        if n%2 !=0:
            return False
        n=n//2
    return True
if power(int(input('Enter a number:'))):
    print(True)
else:
    print(False)