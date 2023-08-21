""" Problem Statement : Calculate sum of given numbers WITHOUT USING LOOP
First line will be number of test cases. 1 <= N <= 100
Next line will contain number of elements. 0 < X <= 100
Next line will be elements with space b/w them
Sample I/P
RULES :
 - NO USE OF LOOPS
 - NO USING OF LIST, SET, DICT
2
4
3 -1 1 14
5
9 6 -53 32 16
Sample O/P
206
1397
"""

def parseNumber(index, string):
    if string[index] == ' ':
        # print("INDEX FOUND ", index)
        return (index, string[:index])
    return parseNumber(index + 1, string)

def parseString(elements, numbersString):
    if elements == 1:
        number = int(numbersString)
        # print("NUMBER " ,number)
        number=number*number if number > 0 else 0
        return number
    # Method to keep going till it finds ' '
    index, number = parseNumber(0, numbersString)
    number = int(number)
    number=number*number if number > 0 else 0
    # print("NUMBER " ,number)
    return number + parseString(elements-1, numbersString[index+1:])
    

def printSumOfElements(testCount):
    if testCount == 0:
        return
    elementsCount = int(input())
    numbersString = input()
    value = 0
    # print(elementsCount, " elements in this string ", numbersString)
    value += parseString(elementsCount, numbersString) 
    print(value)
    printSumOfElements(testCount-1)

if __name__ == "_main_":
    testCases=int(input())
    printSumOfElements(testCases)