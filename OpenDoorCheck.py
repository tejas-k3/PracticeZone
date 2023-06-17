"""
For a stadium, fans are coming in from open doors &
if they see an unguarded door, they sneak in from it
check if there was a moment when more than k doors
where open where k is number of guards & there arr
26 doors labelled A to Z. 
Input format :
n k where n is total number of fans and k is the
number of hired guards
S where S is fans & S1, S2 represent door numbers
first charater means door is open and 2nd count of
same char means door
Output format :
YES if people sneaked else NO
"""
inputVal = input()
n, k = [int(x) for x in inputVal.split()]
gates = {}
print(ipl(inputString, k))

def checkCountIsMore(listVal, allowedCount):
    totalCount = 0
    for i in listVal:
        totalCount+=i
    if totalCount > allowedCount:
        return True
    return False

def fansSneaking(inputString, k):
    for char in inputString:
        val = gates.get(char)
        if val is None:
            gates[char]=1
        elif val == 1:
            gates[char] = 0 # Gate was open, close it
        elif val == 0:
            gates[char] = 1 # Gate was closed, open it
        if checkCountIsMore(gates.values(), k):
            return "YES"
    return "NO"

