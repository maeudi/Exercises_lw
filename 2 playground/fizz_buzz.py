#for n from 1 to 100
#if n is divisible by 3 print frizz
#if n is divisible by 5 print buzz
#else if n is divisible by 3 and 5 print fizzbuzz
#else print n
for n in range(1, 100 + 1):
    print(n)
if (n%3 ==0):
    print ('frizz')
elif (n%5 == 0):
    print('buzz')
elif (n%3!=0) or (n%5 !=0):
    print('frizzbuzz')
else:
    print(n)