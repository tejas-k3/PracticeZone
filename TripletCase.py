def triplet(array, size, value):
	array.sort()
	tripletExists=False
	#print("Here")
	i = 0
	while i < size:
		left = i + 1
		right = size - 1
		while left < right:
		    #print("Valy")
			if int(array[i] + array[left] + array[right]) == value:
			    print("{A} {B} {C}".format(A=array[i], B=array[left], C=array[right]))
			    left+=1
			    right-=1
			    tripletExists=True
			elif int(array[i] + array[left] + array[right]) < value:
				left+=1
			else:
				right-=1
		i+=1
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
