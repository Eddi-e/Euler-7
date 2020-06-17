#Euler project 7
#Eddie
print("hello")
primeCount = 0
numCount = 2
primeList = [2]
numList = [2]
numberLoop = True
while numberLoop is True:
    primeTest = False
    nListLength = len(numList)
    numCount = numCount + 1
    if numCount % 2 != 0:
        primeCheck = True
    if primeCheck is True:
        primeTest = True
        for i in range (0,nListLength):
            if numCount % numList[i] == 0:
                primeTest = False
        if primeTest == True:
            primeList.append(numCount)
    numList.append(numCount)
    if len(primeList) == (10001):
        print (numCount)
        numberLoop = False
