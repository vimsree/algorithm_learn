__author__ = 'vimsree'

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        print('m:',old_m,',n:',old_n)
        m = old_n #10
        n = old_m % old_n #2
        print('new m:',m,',new n:',n)
    return n

print(gcd(6, 20))