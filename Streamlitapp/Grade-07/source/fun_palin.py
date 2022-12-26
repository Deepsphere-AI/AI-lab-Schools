def prime(b):
    c='prime number'
    for i in range(2,b):
        if b%i==0:
            c='not a prime number'
    return c
def palin(b):
    a=b[::-1]
    if a==b:
        vAR_c="is palindrome"
    else:
        vAR_c="not a palindrome"
    return vAR_c
