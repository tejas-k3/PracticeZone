def triplet(array, size, value):
	tripletExists = False
	for i in range(0, size-1):
		hashset = set()
		tempValue = value - array[i]
		for j in range(i + 1, size):
			if (tempValue - array[j]) in hashset:
				print("{A} {B} {C}".format(A=array[i], B=array[j], C=tempValue-array[j]))
				tripletExists = True
			hashset.add(array[j])
	return tripletExists

numbers = []
size = int(input("Enter size of elements : "))
for i in range(0, size):
    numbers.append(int(input("Enter element : ")))
value = int(input("Enter value : "))
if triplet(numbers, size, value):
	print("Above triplet sum up to provided value")
else:
	print("No such triplets exist")
