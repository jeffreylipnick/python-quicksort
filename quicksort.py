# sorting algorithm with average case O(nlogn), worst cast O(n^2). In place sorting which is nice.
def quicksort(A, p, r):
	if p < r: # if p is not less than r we are at our base case
		q = partition(A, p, r) # q is a pivot value. Partition guarantees the following: 
		# 1) All the values to the left of q are less than or equal to q.
		# 2) All the values to the right of q are greater than q.
		# Call quicksort on the subarrays
		quicksort(A, p, q-1)
		quicksort(A, q+1, r)
		# Due to how partition splits up A, when are base cases are reached, we are guaranteed to have a sorted array.

def partition(A, p, r):
	x = A[r] # use the last element in the subarray for our pivot. Worst case runtime happens when all the elements in the subarray are greater than the pivot. This cases us to make n calls of size n-1 -> O(n^2)
	i = p-1 # i is used to demarcate where the subarray split is between the elements that are greater than x and less than x.
	for j in range(p, r): # iterate through each element of our subarray 
		if A[j] <= x: # if the element is less than or equal to our pivot
			i = i+1 # move our index up one
			exchange(A, i, j) # swap element to place it in the range of the "lesser than" segment
	exchange(A, i+1, r) # move the pivot in between the "greater than" and "lesser than" segments
	return i+1 # return the position of the pivot

# helper function to make swapping cleaner
def exchange(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp





