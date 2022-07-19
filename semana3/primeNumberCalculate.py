

from unicodedata import numeric


def isPrimeNumber(number):
    #return True if number is prime, or False if not.
    if number == 1 or number == 0:
        return False
    isPrime = True
    for divisor in range(2,number):
        if number % divisor == 0:
            isPrime = False
            return isPrime
    return isPrime


contPrimeNumber = 0
numberToEvaluate = 1

while contPrimeNumber < 100:
    if isPrimeNumber(numberToEvaluate):
        contPrimeNumber = contPrimeNumber + 1
        print(numberToEvaluate)

    numberToEvaluate = numberToEvaluate + 1