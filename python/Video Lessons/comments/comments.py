# Author: Code Dog
# Date: 3-13-2019
# Objective: This program uses an object to find the number of prime numbers between two numbers.

class Prime:
    """ 
    class prime creates an object that can keep track of the prime numbers between 0 and the specified upper limit
    """
    primes = 0

    # this is the initializing function which takes the number it will search for prime numbers through
    def __init__(self, upperLimit: int):
        self.upperLimit = upperLimit

    # this function will print the prime numbers between zero and the upper limit
    def findPrimes(self):
        timesDivided = 0
        for i in range(2, self.upperLimit + 1):
            for b in range(1, self.upperLimit + 1):
                if i % b == 0:
                    timesDivided += 1
            if timesDivided == 2:
                print(i, 'is a prime number')
                self.primes += 1
            timesDivided = 0
        print('there are', self.primes, 'prime numbers between 0 and', self.upperLimit)

tester = Prime(20)

tester.findPrimes()

