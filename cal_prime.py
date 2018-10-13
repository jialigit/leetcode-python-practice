#! /bin/env python
#-*-coding:utf-8

#this is the function to calculate the primes less than n
import math
import sys
 
def prime(n):
    if n <= 1:
        return 0
    #for i in range(2,int(math.sqrt(n)+1)):
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1

 

if __name__ == "__main__":
	n = int(sys.argv[1])

	for i in range(2,n+1):
		if prime(i):
 			print(i)





