"""
Question : Given an English word representation of a number (Ex : Twelve thousand Three Hundred Forty Five)
return it into its numerical integer value upto billionth value as input. 
I/O : "TWelve thousand THree HUndred Forty Five", 12345
I/O : "Three Million Only", 3000000
Note : Handle lowercaes uppercase, typo and use of Only/And at the end
"""
def wordToInt(inputValue):
	words = inputValue.lower().split()
	smallNums = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, 
		"eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17,
		"eighteen":18, "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, 
		"seventy":70, "eighty":80, "ninety":90}
	bigNums = {"thousand":1000, "million":1000000, "billion":1000000000}
	tempNum = 0
	finalNum= 0
	for word in words:
		# print(finalNum)
		if word in smallNums:
			tempNum += smallNums[word]
		elif word == "hundred":
			tempNum *= 100
		elif word in bigNums:
			tempNum *= bigNums[word]
			finalNum += tempNum
			tempNum = 0
		else:
			break
	finalNum+=tempNum
	return finalNum

# print(wordToInt("TWelve thousand THree HUndred Forty Five"))