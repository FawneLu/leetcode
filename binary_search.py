def binarySearch1(array, key, low, high):
    if high<low:
    	return -1

    mid=low+(high-low)//2

    if array[mid]==key:
    	return mid
    elif array[mid]>key:
    	return binarySearch1(array,key,low,mid-1)
    elif array[mid]<key:
    	return binarySearch1(array,key,mid+1,high)



def binarySearch2(array, key):
	low,high=0,len(array)-1

	while low<=high:
		mid=low+(high-low)//2
		if array[mid]==key:
			return mid
		elif array[mid]>key:
			high=mid-1
		elif array[mid]<key:
			low=mid+1

	return -1


def binarySearch3(array, key, low, high):
	if low>high:
		return -1
	mid=low+(high-low)//2

	if array[mid]>key:
		return binarySearch3(array,key,low,mid-1)
	elif array[mid]<key:
		return binarySearch3(array,key,mid+1,high)
	else:
		if mid==0 or array[mid-1]!=key:
			return mid
		else:
			return binarySearch3(array,key,low,mid-1)

def binarySearch4(array, key, low, high):
	if low>high:
		return -1
	mid=low+(high-low)//2

	if array[mid]>key:
		return binarySearch4(array,key,low,mid-1)
	elif array[mid]<key:
		return binarySearch4(array,key,mid+1,high)
	else:
		if mid==len(array)-1 or array[mid+1]!=key:
			return mid
		else:
			return binarySearch4(array,key,mid+1,high)


def binarySearch5(array, key, low, high):
	if low>high:
		return -1

	mid=low+(high-low)//2

	if array[mid]<key:
		return binarySearch5(array,key,mid+1,high)
	else:
		if mid==0 or array[mid-1]<key:
			return mid
		else:
			return binarySearch5(array,key,low,mid-1)


def binarySearch6(array, key, low, high):
	if low>high:
		return -1
	mid=low+(high-low)//2

	if array[mid]>key:
		return binarySearch6(array,key,low,mid-1)
	else:
		if mid==len(arrau)-1 or array[mid+1]>key:
			return mid
		else:
			return binarySearch6(array,key,mid+1,high)



def tripleSearch1(array, key, low, high):
	if low>high:
		return -1

	tmp1=low+(high-low)//3
	tmp2=low+((high-low)//3)*2

	if array[tmp1]==key:
		return tmp1
	elif array[tmp2]==key:
		return tmp2
	elif array[tmp1]>key:
		return tripleSearch1(array,key,low,tmp1-1)
	elif array[tmp2]<key:
		return tripleSearch1(array,key,tmp2+1,high)
	else:
		return tripleSearch1(array,key,tmp1+1,tmp2-1)







if __name__ == '__main__':
	a=[2,3,4,4,5,6,7]
	print(binarySearch1(a,5,0,len(a)-1))
	print(binarySearch2(a,5))
	print(binarySearch3(a,5,0,len(a)-1))
	print(binarySearch4(a,5,0,len(a)-1))
	print(binarySearch5(a,5,0,len(a)-1))
	print(binarySearch5(a,3,0,len(a)-1))
	print(tripleSearch1(a,2,0,len(a)-1))



