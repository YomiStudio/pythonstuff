#checks if a number is a prime number by iterating from 2 to the number minus 1
def checkIfPrime(num: int):
    exclude = {1,2}
    #if num in exclude:
    #    print(num, "is ")
    for i in range(2,num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

#function calls
checkIfPrime()
