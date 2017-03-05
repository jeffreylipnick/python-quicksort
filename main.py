# small example of quicksort in use

from quicksort import quicksort

def main():
	A = [1, 4, 2, 3, 7, 5, 10, 6, 9, 8]
	B = ['a', 'q', 'ee', 'niner', 'foo']
	quicksort(A, 0, len(A)-1)
	quicksort(B, 0, len(B)-1)
	print A
	print B

if __name__ == "__main__":
    main()