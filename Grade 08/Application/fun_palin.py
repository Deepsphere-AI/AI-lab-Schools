def prime(b):
    c='prime number'
    for i in range(2,b):
        if b%i==0:
            c='not a prime number'
    return c
def palin(b):
    a=""
    for i in b:
        a=i+a
    if a==b:
        vAR_c="is palindrome"
    else:
        vAR_c="not a palindrome"
    return vAR_c
