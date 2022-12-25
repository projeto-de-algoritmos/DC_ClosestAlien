import random
import sys
sys.setrecursionlimit(100000)

def getMedians(array):
	blocks = [array[i:i+5] for i in range(0, len(array), 5)]
	sortedBlocks = [sorted(block) for block in blocks]
	medians = [block[len(block)//2] for block in sortedBlocks]
	return medians

def chosePivot(array, k):
	medians = getMedians(array)
	# median of medians
	m = medians[len(medians)//2]
	return m

def partition(array, m):
	left = 0
	right = len(array) - 1
	i = 0

	while i <= right:
		if array[i] == m:
			i += 1
		elif array[i] < m:
			array[left], array[i] = array[i], array[left]
			left += 1
			i += 1
		else:
			array[right], array[i] = array[i], array[right]
			right -= 1

	return left

def medianOfMedians(array, k):
	m = chosePivot(array, k)
	left = partition(array, m)

	if left == (k):
		return m
	elif left > (k):
		return medianOfMedians(array[0:left], k)
	else:
		return medianOfMedians(array[left + 1:len(array)], k - left - 1)

# vetor = [2,5,9,19,24,54,5,87,9,10,44,32,18,13,2,4,23,26,16,19,25,39,47,56,71]
vetor = [(random.random()*100*random.random()*100*random.random()*100) for i in range(1000000)]
print('Mediana Real: ', sorted(vetor)[len(vetor)//2])
mm = medianOfMedians(vetor, len(vetor)//2)
print('Mediana Oráculo: ', mm)