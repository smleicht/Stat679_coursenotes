#!/usr/bin/env python
""" The purpose of thos module is to computes the binomial cofficient of 'n choose k' for all positive, integers of n and k 
where n is greater than or equal to k. This computation relies on two functions: the first function logfactorial() computes log(n!/k!)
and the second function choose() computes the binomial cofficient for positive, integer values of n and k """


import argparse
# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="total number of items to choose from")
parser.add_argument("-k", type=int, help="number of items to choose")
parser.add_argument("-l", "--log", action="store_true", help="returns the log binomial coefficient")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()
binomiaL_coeffecient = False if args.log else True

import math

def logfactorial(n=args.n, k=args.k):
        """ returns the log of the factorial of a particular integer
        log(0!)+..... log(n!)
        Examples:

        >>> logfactorial(3, 2)
        1.3862943611198906

        >>> logfactorial(5, 2)
        4.787491742782046
        """
       
        assert n >= 0 and type(n) == int #n should be positive and an integer
        assert k >=0 and type(k) == int #k should be positive and an integer
        assert n >= k
        logfactorialnk = float()
        for i in range(k+1,n+1):
               logfactorialnk += math.log(i + 1)
        return logfactorialnk

def choose(n=args.n, k=args.k,  binomiaL_coeffecient=binomiaL_coeffecient):
        """ returns the log binomial distribution of any integer n given a number of k element
        such that choose(n, k) = n!/(k!(n-k)!)
        Examples:

        >>> choose(10, 3)
        330

        >>> choose(15, 6)
        11440

        >>> choose(20, 8)
        293930
        """

        # log(n!/k!) - log((n-k)!)
        assert n >= 0 and type(n) == int #n should be positive and an integer
        assert k >= 0 and type(k) == int #k should be positive and an integer
        assert n >= k # value of n can be less than or equal to the value of k
        log_nsubractk = float()
        for i in range(k, n):
                log_nsubractk += math.log(i + 1 - k)
        log_value = logfactorial(n, k) - log_nsubractk
        result = int(round(math.exp(log_value))) if binomiaL_coeffecient else log_value
        print(result)

def run_test():
        print("testing the module...")
        if args.n:
                print("ignoring n for testing purposes")
        import doctest
        doctest.testmod()
        print("done with tests.")    

if __name__ == '__main__':
        if args.test:
                run_test()
        else:
                choose()


        

