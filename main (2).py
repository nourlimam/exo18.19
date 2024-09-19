'''def parfait(num):
   s = 0
   for i in range(1,num+1):
       if num % i == 0:
           s += i
   return s == 2*num 
print(parfait(6))'''



def factorielle(n):
    fact = 1
    for i in range(1,n+1):
         fact = fact*i
    return fact
print (factorielle(8))